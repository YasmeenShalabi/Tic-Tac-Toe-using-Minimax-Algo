# Tic-Tac-Toe AI Using Minimax
 
A Python Tic-Tac-Toe game where the player competes against an AI powered by the **Minimax algorithm**.
 
## How It Works
 
The player uses **X** and the AI uses **O**.
 
The AI uses Minimax to simulate possible future moves and determine the best move. It:
 
- Maximizes the AI's chance of winning.
- Minimizes the player's chance of winning.
- Uses recursion to explore possible game outcomes.
- Uses backtracking to simulate and undo moves.
- Evaluates outcomes as:
- `+1` → AI wins
- `0` → Draw
- `-1` → Player wins

## How Minimax Works

Minimax works by looking at every possible move from the current board, then recursively imagining what would happen after each move. For example: you try one move, assume I respond in the best way to avoid losing, then you compare the outcomes and pick the move that gives you the best guaranteed result
 
## Features
 
- Player vs. AI gameplay
- Winner and draw detection
- Recursive Minimax algorithm
- AI move evaluation
- Simple command-line interface
 
## Running the Game
run: python tic_tac_toe.py

Enter a number from 1–9 when prompted to choose your position.

## Technologies

Python
Minimax Algorithm
Recursion
Backtracking
