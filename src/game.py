import logic
from src.logic import run_main_menu, run_difficulty_select

GAME_STATE = {
    "DIFFICULTY": "NONE"
}

def main_game_loop():
    #Defining the continue_game variable and we're running the main menu once
    continue_game = run_main_menu()
    #This will run the main_menu until we say Yes
    while continue_game == False:
        continue_game = run_main_menu()

    selected_difficulty, difficulty_valid = run_difficulty_select()
    while difficulty_valid == False:
        difficulty_valid = run_difficulty_select()
    GAME_STATE["DIFFICULTY"] = selected_difficulty



main_game_loop()