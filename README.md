# Modular Snake Game 🐍

A professional implementation of the classic Snake game using **Python** and **Pygame**. This project follows an intermediate-level modular architecture, separating logic, objects, and configurations for better scalability and maintenance.

## 🚀 Features
- **Modular Design:** Divided into constants, objects, and game engine.
- **Persistence:** High score is saved locally in a `record.txt` file.
- **Clean Code:** Implemented using Object-Oriented Programming (OOP).
- **Responsive Controls:** Improved input logic to prevent illegal 180-degree turns.

## 🛠️ Project Structure
```text
snake-game/
├── src/
│   ├── __init__.py      # Package initialization
│   ├── constantes.py    # Game settings (colors, dimensions, speed)
│   ├── objetos.py       # Snake and Food classes
│   └── motor.py         # Score persistence and file handling
├── main.py              # Main entry point
├── requirements.txt     # Project dependencies
└── record.txt           # Local high score storage
´´´

## 📦 Installation & Setup

1. Clone the repository:
```bash
git clone https://github.com/dylannsotoo/snake-game.git
```

2. Navigate to the project directory:
```bash
cd snake-game
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## 🎮 How to Play

Run the game using Python:
```bash
python main.py
```

Controls:
- **Arrow Keys**: Move the snake
- **ESC**: Exit the game

## 🚀 Future Improvements

The project is currently in its core version, but the following features are planned for future releases to enhance the user experience and data management:

- **SQL Database Integration:** Migration from `.txt` to an **SQLite** database to handle more complex data and multiple user records.
- **User Identification:** A start menu to ask for the **Player's Name** before the match begins.
- **Global Leaderboard:** Implementation of a top 10 ranking system showing the best players' names and scores.
- **Dynamic Difficulty:** Gradual speed increase as the snake grows longer.
- **Power-ups:** Special items that grant temporary abilities (e.g., speed reduction or double points).