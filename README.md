# 🐍 Snake Game (Python Turtle)

A classic Snake game built with Python's `turtle` graphics module. Eat the food, grow longer, and try to beat the high score without running into yourself!

## 🎮 Demo

The snake wraps around the screen edges instead of dying when it hits a wall — only colliding with its own body ends the game.

## 📂 Project Structure

```
.
├── main.py          # Game window setup and main game loop
├── snake.py         # Snake class — movement, growth, direction control
├── food.py          # Food class — random spawn logic
├── scoreboard.py     # Score class — score display and high score persistence
└── highscore.txt     # Stores the current high score
```

## ✅ Requirements

- Python 3.x
- `turtle` module (included in the standard Python library)

## ▶️ How to Run

```bash
python main.py
```

## 🕹️ Controls

| Key | Action |
|-----|--------|
| ↑   | Move Up |
| ↓   | Move Down |
| →   | Move Right |
| ←   | Move Left |

## 🏆 Scoring

- Each piece of food eaten adds **2 points**.
- The high score is saved automatically to `highscore.txt` if you beat it.

## ⚠️ Known Issue / TODO

`scoreboard.py` currently reads/writes `highscore.txt` using a **hardcoded absolute path**:

```python
with open("C:/Users/awwso/Desktop/Projects/python/GUI/Snake Game/highscore.txt") as file:
```

This will break on any machine other than the original one. Before pushing to GitHub, consider replacing it with a relative path, for example:

```python
import os
HIGHSCORE_FILE = os.path.join(os.path.dirname(__file__), "highscore.txt")

with open(HIGHSCORE_FILE) as file:
    ...
```

## 📝 License

Feel free to use and modify this project for learning purposes.
