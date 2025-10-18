# Save the Watermelon

## Project Description
"Save the Watermelon" is a terminal-based word-guessing game implemented in Python 3.10 using only the standard library. Players take on the role of "elite fruit operators" tasked with saving a watermelon by guessing secret words across three levels. The game features three difficulty levels (Easy, Medium, Hard) with varying attempt limits and word lists, offering a military-themed twist on the classic Hangman game. It is designed for beginner to intermediate Python developers to practice modular programming, file I/O, and game logic, while providing an engaging experience for casual gamers.

## How to Run
1. Ensure Python 3.10 or higher is installed.
2. Clone the repository:
   ```
   git clone <your-repo-url>
   ```
3. Navigate to the project directory:
   ```
   cd save-the-watermelon
   ```
4. Ensure word list files exist in the `data/` directory:
   - `data/words_easy.txt` (e.g., "cat", "dog", "bat")
   - `data/words_medium.txt` (e.g., "apple", "banana", "orange")
   - `data/words_hard.txt` (e.g., "watermelon", "strawberry", "pineapple")
5. Run the game using one of the following commands:
   ```
   python -m src.game
   ```
   or
   ```
   python src/game.py
   ```

## How to Test
Run the unit tests to verify core functionality:
```
python -m unittest tests/test_logic.py
```
Manual test results and a detailed test plan are available in `docs/test-plan.md`.

## Features & Rules
- **Main Menu**: Players confirm readiness with "yes" to proceed or "no" to exit.
- **Difficulty Selection**: Choose from:
  - Easy: 15 attempts, shorter words.
  - Medium: 10 attempts, medium-length words.
  - Hard: 5 attempts, longer words.
- **Gameplay**: 
  - Players guess single letters or the full word to reveal a secret word across three levels.
  - Words are randomly selected from difficulty-specific files (`data/words_<difficulty>.txt`), with no repeats in a session.
  - Correct letter guesses reveal all occurrences in the word; correct full-word guesses win the level instantly.
  - Incorrect guesses deduct one attempt.
  - Invalid inputs (non-alphabetic single letters or duplicate guesses) are rejected with error messages.
- **Win Condition**: Successfully guess the word in each of the three levels.
- **Lose Condition**: Exceed the maximum allowed incorrect guesses in any level.
- **User Experience**: Thematic messages (e.g., "YOU SAVED THE WATERMELON SOLDIER!") and formatted dividers enhance console readability.

## Known Issues/Limitations
- **No Replay Option**: After winning or losing, players must restart the program to play again (replay is a stretch goal not implemented).
- **Module Naming**: The project uses `gamelogic.py` (for menu and word loading) and `utility.py` (for display/input helpers) instead of the suggested `logic.py` and `words.py`. This does not affect functionality, as responsibilities are equivalent.
- **File Dependency**: The game requires `data/words_<difficulty>.txt` files to exist with valid words; missing or empty files will cause errors.

## Credits
- **Developed by**: [Luca Gerardi]