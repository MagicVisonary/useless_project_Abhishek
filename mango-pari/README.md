<img width="1280" height="640" alt="git (1)" src="https://github.com/user-attachments/assets/8920b256-2ba8-4988-b824-5351134eb4bd" />

# മാങ്ങ പറി (Mango Pari) 🎯

[![Live Game Demo](https://img.shields.io/badge/🎮_Play_Live-Game_Demo_(One--Click)-FFD700?style=for-the-badge&logo=google-chrome&logoColor=black)](https://magicvisonary.github.io/useless_project_Abhishek/)
[![TinkerHub](https://img.shields.io/badge/TinkerHub-Useless_Projects_3.0-00C853?style=for-the-badge&link=https%3A%2F%2Ftinkerhub.org%2Fevents%2F1M8ORET9A1%2Fuseless-projects-3.0)](https://tinkerhub.org/events/1M8ORET9A1/useless-projects-3.0)

## Basic Details
### Team Name: MANGO TANGO

### Team Members
- Team Lead: Abhishek K S - NSS College of Engineering, Palakkad

### Hosted Project Link
🚀 **[Play Live on GitHub Pages (One-Click Link)](https://magicvisonary.github.io/useless_project_Abhishek/)**

### Project Description
A chaotic, humorous Malayalam arcade web game where players must dodge falling ripe yellow mangoes and risk everything to catch **Pari** (Prithviraj meme) into their bucket! Featuring a Single-Player survival mode and an interactive **4-Player Local Multiplayer Mode** where friends control their buckets from their smartphones via a QR code over local Wi-Fi.

Now enhanced with a **"Last Player Standing" Battle Royale elimination system**: when a player's bucket hits a mango, their phone vibrates and locks out with the infamous **"മാങ്ങാത്തൊലി! (Mangatholi)"** title, while the surviving players battle it out until the champion stands victorious!

### The Problem (that doesn't exist)
Instead of traditional *manga parikkal* (mango plucking), human civilization has been lacking an intense, high-stakes system focused solely on *pari parikkal*!

### The Solution (that nobody asked for)
"മാങ്ങ പറി" gives you this once-in-a-lifetime opportunity: a high-energy multiplayer game where missing Pari means defeat, touching a mango gives you the title of *Mangatholi*, and catching Pari unleashes a thunderous *"പറി!"* voice blast!

---

## Technical Details
### Technologies/Components Used
For Software:
- **Languages:** JavaScript (ES6+), HTML5, CSS3, Python 3
- **Frameworks / APIs:**
  - **Web Audio API:** Real-time synthesizer, dynamic range compression & 3.8x gain booster for punchy dialogue and BGM sidechain ducking.
  - **Server-Sent Events (SSE) + TCP_NODELAY:** Ultra low-latency (<15ms) event-driven streaming from smartphones to the laptop screen with sub-millisecond Condition wakeups.
  - **Request Coalescing Netcode:** Guarantees exactly 1 active HTTP request per phone, eliminating 100% of mobile browser socket queue congestion.
  - **60/120 FPS Linear Interpolation (LERP):** Smooth client-side bucket gliding eliminating all network jitter and packet stutter.
  - **Pointer & Touch Events API:** Responsive mobile touch trackpad, swipe controls, Left/Right tap buttons, and optional gyroscope tilt.
- **Libraries:**
  - `qrcode.min.js` (Standalone, zero-dependency offline QR code generator)
- **Tools:**
  - Visual Studio Code
  - Python 3 standard library (`http.server`, `socket`, `threading`, `urllib.parse`)
  - Git & GitHub

For Hardware:
- **Laptop / PC:** Acts as the host server and main display screen (runs the game canvas, safe corridor physics, and audio).
- **Smartphones (1 to 4):** Connected over local Wi-Fi, functioning as wireless gamepad controllers via QR code with live haptic feedback.

---

### Implementation
For Software:
# Installation
1. Clone this repository:
```bash
git clone https://github.com/Abhishek-ks-04/useless_project_Abhishek.git
cd useless_project_Abhishek
```
2. No external dependencies or `npm install` needed! Everything runs using pure web technologies and Python standard library.

# Run
Simply double-click:
```bat
start_game.bat
```
Or run via terminal:
```bash
python server.py
```
*(On Windows with Python launcher: `py -3 server.py`)*

Then open `http://localhost:8080` on your laptop browser!

---

### Project Documentation
For Software:

# Screenshots

### 1. Main Menu Screen
![Main Menu Screen](images/Screenshot%202026-09-12%20015736.png)
*Main Menu: Featuring Single Player, 4-Bucket Multiplayer Lobby, and the "I Don't Know" meme mode.*

### 2. In-Game Gameplay Screen
![Gameplay Screen](images/Screenshot%202026-09-12%20015935.png)
*Live Gameplay: Player 1 bucket dodging falling ripe yellow mangoes while catching Pari with audio blast.*

### 3. Game Rules
![Rules Graphic](assets/rules.png)
*Official rules: Catch Pari (+100 points) or game over; touching mangoes leads to instant elimination.*

# Diagrams
```text
+------------------+         Local Wi-Fi          +---------------------+
|  Player Phone 1  | ---------------------------> |                     |
| (controller.html)|        HTTP POST /move       |                     |
+------------------+                              |                     |
                                                  |    Laptop Screen    |
+------------------+                              |    (index.html)     |
|  Player Phone 2  | ---------------------------> |                     |
| (controller.html)|                              | Real-time Canvas    |
+------------------+                              | 4 Dynamic Buckets   |
                                                  | Web Audio BGM & SFX |
+------------------+                              |                     |
|  Player Phone 3  | ---------------------------> |                     |
| (controller.html)|        SSE Live Stream       |                     |
+------------------+    <------------------------ |    Python Server    |
                             (/api/stream)        |     (server.py)     |
+------------------+                              |                     |
|  Player Phone 4  | ---------------------------> |                     |
| (controller.html)|                              +---------------------+
+------------------+
```
*Architecture workflow: Phones act as wireless gamepads streaming inputs to the laptop game over local Wi-Fi via SSE.*

### Project Demo
# Video

<video src="images/Recording%202026-09-12%20020811.mp4" controls="controls" width="100%"></video>

🎥 **[Click here to watch / download the Gameplay Demo Recording (MP4)](images/Recording%202026-09-12%20020811.mp4)**

*Demonstrates live gameplay: dodging falling mangoes, catching Pari with audio blast, and 4-player smartphone multiplayer action.*

# Live One-Click Game Demo
🎮 **[Click Here to Launch & Play Mango Pari Live on GitHub Pages](https://magicvisonary.github.io/useless_project_Abhishek/)**

- **Instant Browser Play:** Single Player mode, "I Don't Know" meme guide, and 2-Player keyboard multiplayer work 100% directly in your browser without downloading anything!
- **Local Wi-Fi Smartphone Gamepads:** Clone the repo and run `start_game.bat` or `python server.py` to connect up to 4 smartphone gamepads with real-time haptic feedback over local Wi-Fi.

---
Made with ❤️ at TinkerHub Useless Projects 

![Static Badge](https://img.shields.io/badge/TinkerHub-24?color=%23000000&link=https%3A%2F%2Fwww.tinkerhub.org%2F)
![Static Badge](https://img.shields.io/badge/UselessProjects--26-26?link=https%3A%2F%2Ftinkerhub.org%2Fevents%2F1M8ORET9A1%2Fuseless-projects-3.0)
