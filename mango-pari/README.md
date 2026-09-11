# 🥭 മാങ്ങ പറി (Mango Pari)

An exciting, humorous Malayalam arcade web game where you dodge falling ripe mangoes and catch **Pari** (Prithviraj meme) into your bucket! Featuring a single-player survival mode and an interactive **4-Player Local Multiplayer Mode** where friends control their buckets from their smartphones via a QR code over Wi-Fi.

---

## 🎮 Game Modes

### 1. 🧔 Single Player Mode (ഏകാന്ത പോരാട്ടം)
- **Goal:** Dodge the falling ripe yellow mangoes!
- **The Twist:** **Pari** periodically drops down the screen. You **MUST catch Pari**! If Pari hits the ground uncaught, it is **Game Over**!
- Catching Pari awards **+100 points** and triggers an iconic, boosted voice line: *"പറി!"*.
- Touching any mango results in instant elimination.
- Endless gameplay with smooth, gradual difficulty scaling over time.

### 2. 📱 Multiplayer Mode (4 Players - കൂട്ടായ്മ)
- **Local Wi-Fi Party Game:** Run the main game screen on your laptop or TV screen.
- **Phone Controllers:** Up to 4 players scan a QR code from the game lobby on their smartphones to open `controller.html`.
- **4 Distinct Colored Buckets:**
  - 🔵 **Player 1:** Blue
  - 🔴 **Player 2:** Red
  - 🟢 **Player 3:** Green
  - 🟡 **Player 4:** Gold
- **High-Rate Pari Spawning & Multi-Drops:** Multiple Paris spawn across different corridors so all 4 players can compete and score easily!
- Real-time touch controls, Left/Right buttons, and gyroscope tilt supported on mobile devices.
- Uncaught Paris in Multiplayer do not abruptly end the match—players keep playing until all buckets are knocked out by mangoes, and the winner is announced with a full score breakdown!

### 3. 🤔 "I Don't Know" (എനിക്കറിയില്ല)
- A humorous Malayali meme dialog explaining the game's origins with Prithviraj dialogue audio and direct play buttons.

---

## 🕹️ Controls

- **Laptop Keyboard (Single Player):** `A` / `D` or `Left Arrow` / `Right Arrow`
- **Mouse / Touchpad:** Click and drag bucket left/right on screen
- **Mobile Phone Controller:** Touch trackpad drag, Left/Right tap buttons, or tilt gyro
- **Laptop Keyboard (Multiplayer):** Player 1: `A`/`D`, Player 2: `Left`/`Right`, Player 3: `J`/`L`, Player 4: `4`/`6`

---

## 🚀 How to Run Locally

### Prerequisites
- Python 3.x installed (no external libraries needed, uses standard Python library).
- Any modern web browser (Chrome, Edge, Firefox, Safari).

### Quick Start (Windows)
Simply double-click:
```bat
start_game.bat
```
Or run from PowerShell / Command Prompt:
```bash
python server.py
```
*(On Windows with Python launcher: `py -3 server.py`)*

The server will automatically:
1. Detect your Wi-Fi network IP (bypassing VPNs/WARP).
2. Launch your browser directly to `http://localhost:8080`.
3. Host the real-time Server-Sent Events (SSE) stream on port `8080` for connected smartphones.

---

## 📁 Project Structure

```
mango-pari/
├── assets/
│   ├── bg.jpg              # Atmospheric mango orchard background
│   ├── pari.png            # Pari (Prithviraj) portrait asset
│   ├── rules.png           # Visual game rules graphic
│   ├── bucket_mascot.png   # Cartoon bucket mascot
│   ├── pari_audio.mp3      # "പറി!" voice clip
│   └── qrcode.min.js       # Standalone offline QR code generator
├── index.html              # Main game interface, audio synthesis, and loop
├── controller.html         # Mobile responsive touch controller
├── server.py               # Zero-dependency Python HTTP + SSE server
├── start_game.bat          # 1-click Windows launcher script
├── README.md               # Documentation & instructions
└── .gitignore              # Git ignore rules
```

---

## 📦 How to Upload to GitHub

1. Open your project folder in VS Code or Terminal:
   ```bash
   cd mango-pari
   ```
2. Initialize Git:
   ```bash
   git init
   git add .
   git commit -m "Initial commit: Mango Pari game with Single & Multiplayer modes"
   ```
3. Link your remote GitHub repository and push:
   ```bash
   git remote add origin https://github.com/YOUR_USERNAME/mango-pari.git
   git branch -M main
   git push -u origin main
   ```

---

## 📜 License
MIT License. Created for fun and entertainment!
