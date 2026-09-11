#!/usr/bin/env python3
"""
മാങ്ങ പറി (Mango Pari) - Local Multiplayer Game Server
Zero-dependency HTTP & Realtime Event Server for Laptop & Phone Controllers.
"""

import http.server
import socketserver
import socket
import json
import urllib.parse
import os
import sys
import threading
import time
import webbrowser

# Ensure UTF-8 output on Windows consoles
if hasattr(sys.stdout, 'reconfigure'):
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass

PORT = 8080
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

def get_local_ip():
    """Detects the primary Wi-Fi / LAN IP address of this laptop (skipping VPNs like Cloudflare WARP)."""
    import subprocess
    try:
        out = subprocess.check_output('ipconfig', text=True, stderr=subprocess.DEVNULL)
        current = ''
        ips = []
        for line in out.splitlines():
            line_s = line.strip()
            if 'adapter' in line_s.lower():
                current = line_s
            elif 'ipv4' in line_s.lower() and ':' in line_s:
                ip = line_s.split(':')[-1].strip()
                ips.append((current, ip))
        # 1. Prioritize Wi-Fi / Wireless adapters
        for adapter, ip in ips:
            if 'wi-fi' in adapter.lower() or 'wireless' in adapter.lower():
                return ip
        # 2. Fall back to non-WARP adapter
        for adapter, ip in ips:
            if 'warp' not in adapter.lower() and not ip.startswith('127.'):
                return ip
    except Exception:
        pass

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return '127.0.0.1'

LOCAL_IP = get_local_ip()

# Game & Players State
PLAYER_COLORS = ['#2196F3', '#F44336', '#4CAF50', '#FF9800'] # Blue, Red, Green, Orange/Gold
PLAYER_NAMES = ['Player 1', 'Player 2', 'Player 3', 'Player 4']

game_state = {
    'players': {
        1: {'active': False, 'name': 'Player 1', 'color': PLAYER_COLORS[0], 'pos': 20.0, 'last_seen': 0, 'score': 0, 'eliminated': False},
        2: {'active': False, 'name': 'Player 2', 'color': PLAYER_COLORS[1], 'pos': 40.0, 'last_seen': 0, 'score': 0, 'eliminated': False},
        3: {'active': False, 'name': 'Player 3', 'color': PLAYER_COLORS[2], 'pos': 60.0, 'last_seen': 0, 'score': 0, 'eliminated': False},
        4: {'active': False, 'name': 'Player 4', 'color': PLAYER_COLORS[3], 'pos': 80.0, 'last_seen': 0, 'score': 0, 'eliminated': False},
    },
    'status': 'lobby', # 'lobby' or 'playing' or 'ended'
    'version': 0
}

state_lock = threading.Lock()
subscribers = [] # List of SSE output queues/writers

class MangoServerHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def log_message(self, format, *args):
        # Suppress routine log clutter
        pass

    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        super().end_headers()

    def do_OPTIONS(self):
        self.send_response(200)
        self.end_headers()

    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path

        if path == '/api/ip':
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            data = json.dumps({'ip': LOCAL_IP, 'port': PORT, 'url': f'http://{LOCAL_IP}:{PORT}/controller.html'}).encode('utf-8')
            self.wfile.write(data)
            return

        if path == '/api/state':
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.send_header('Cache-Control', 'no-cache')
            self.end_headers()
            with state_lock:
                data = json.dumps(game_state).encode('utf-8')
            self.wfile.write(data)
            return

        if path == '/api/stream':
            # Server-Sent Events (SSE) for low-latency live position updates
            self.send_response(200)
            self.send_header('Content-Type', 'text/event-stream')
            self.send_header('Cache-Control', 'no-cache')
            self.send_header('Connection', 'keep-alive')
            self.end_headers()

            last_sent_version = -1
            try:
                while True:
                    time.sleep(0.016) # ~60fps
                    with state_lock:
                        ver = game_state['version']
                        if ver != last_sent_version:
                            last_sent_version = ver
                            payload = json.dumps(game_state)
                            msg = f"data: {payload}\n\n".encode('utf-8')
                            self.wfile.write(msg)
                            self.wfile.flush()
            except (ConnectionResetError, BrokenPipeError):
                return
            return

        # Serve static files as normal
        super().do_GET()

    def do_POST(self):
        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path
        length = int(self.headers.get('Content-Length', 0))
        body = self.rfile.read(length).decode('utf-8') if length > 0 else '{}'
        try:
            req = json.loads(body)
        except Exception:
            req = {}

        global game_state

        if path == '/api/join':
            # Phone joins game
            p_slot = None
            preferred = req.get('player')
            with state_lock:
                now = time.time()
                # Clean up inactive players (> 15 seconds without update)
                for pid, pdata in game_state['players'].items():
                    if pdata['active'] and (now - pdata['last_seen'] > 15):
                        pdata['active'] = False

                if preferred and 1 <= preferred <= 4 and not game_state['players'][preferred]['active']:
                    p_slot = preferred
                else:
                    for pid in range(1, 5):
                        if not game_state['players'][pid]['active']:
                            p_slot = pid
                            break

                if p_slot:
                    game_state['players'][p_slot]['active'] = True
                    game_state['players'][p_slot]['name'] = req.get('name', f'Player {p_slot}')
                    game_state['players'][p_slot]['last_seen'] = now
                    game_state['players'][p_slot]['eliminated'] = False
                    game_state['version'] += 1

            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            resp = {
                'success': bool(p_slot),
                'player': p_slot,
                'color': PLAYER_COLORS[p_slot-1] if p_slot else None,
                'name': PLAYER_NAMES[p_slot-1] if p_slot else None
            }
            self.wfile.write(json.dumps(resp).encode('utf-8'))
            return

        if path == '/api/move':
            # Phone sends movement update { player: 1, pos: 55.4 }
            pid = req.get('player')
            pos = req.get('pos')
            if pid and 1 <= pid <= 4 and pos is not None:
                with state_lock:
                    p = game_state['players'][pid]
                    p['active'] = True
                    p['pos'] = max(4.0, min(96.0, float(pos)))
                    p['last_seen'] = time.time()
                    game_state['version'] += 1

            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(b'{"status":"ok"}')
            return

        if path == '/api/leave':
            pid = req.get('player')
            if pid and 1 <= pid <= 4:
                with state_lock:
                    game_state['players'][pid]['active'] = False
                    game_state['version'] += 1
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(b'{"status":"ok"}')
            return

        if path == '/api/reset':
            with state_lock:
                for pid in range(1, 5):
                    game_state['players'][pid]['eliminated'] = False
                    game_state['players'][pid]['score'] = 0
                game_state['version'] += 1
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(b'{"status":"ok"}')
            return

        self.send_response(404)
        self.end_headers()

class ThreadedHTTPServer(socketserver.ThreadingMixIn, http.server.HTTPServer):
    daemon_threads = True

def run():
    os.chdir(DIRECTORY)
    server_address = ('0.0.0.0', PORT)
    httpd = ThreadedHTTPServer(server_address, MangoServerHandler)

    print("=" * 65)
    print("🥭 മാങ്ങ പറി (Mango Pari) - Multiplayer Game Server")
    print("=" * 65)
    print(f"🖥️  Laptop Game Screen:   http://localhost:{PORT}")
    print(f"📱 Phone Controller URL: http://{LOCAL_IP}:{PORT}/controller.html")
    print("-" * 65)
    print("Connect your phones to the same Wi-Fi, then scan the QR code")
    print("displayed on the laptop screen to play!")
    print("Press Ctrl+C to stop the server.")
    print("=" * 65)

    # Automatically open the game in the laptop browser
    def open_browser():
        time.sleep(1.0)
        webbrowser.open(f'http://localhost:{PORT}')

    threading.Thread(target=open_browser, daemon=True).start()

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down server...")
        httpd.server_close()

if __name__ == '__main__':
    run()
