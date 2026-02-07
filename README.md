# 🚗 YOHANNN – Endless Car Survival Game

YOHANNN is a simple **endless vertical car survival game** built using **Python and Pygame**.  
The objective is to survive as long as possible while dodging enemy cars coming from different lanes.

---

## 🎮 Gameplay Features

- Smooth vertical scrolling background
- Lane-based enemy car spawning
- Randomized enemy cars
- Keyboard-controlled player movement
- Collision detection using `pygame.Rect`
- Game Over screen with survival time
- Instant restart without restarting the program

---

## 🕹️ Controls

| Key | Action |
|----|-------|
| **W** | Move up (increase speed) |
| **S** | Move down |
| **A** | Move left |
| **D** | Move right |
| **Any Key** | Restart after Game Over |

---

## 🧠 Game Logic Summary

- Player movement is restricted to road boundaries
- Enemies spawn in predefined lanes
- Background scrolls continuously to simulate motion
- Collision detection ends the game
- Survival time is calculated using system ticks

---

## 🛠️ Technologies Used

- **Python 3**
- **Pygame**

---

## 📂 Project Structure

YOHANNN/
│
├── assets/
│ ├── background/
│ │ └── background-1_2.png
│ ├── player/
│ │ └── Pcar.png
│ └── enemy/
│ ├── E1.png
│ ├── E2.png
│ ├── E3.png
│ ├── E4.png
│ ├── E5.png
│ └── E6.png
│
├── main.py
├── README.md
├── CREDITS.md
└── LICENSE

---

## ▶️ How to Run

1. Install Python (3.8 or above)
2. Install pygame:
   ```bash
   pip install pygame
Run the game:

python main.py