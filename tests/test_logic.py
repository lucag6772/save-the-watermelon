from src.game import GameState
from src.gamelogic import DIFFICULTIES, get_possible_words_from_difficulty


#Test 1: Make sure difficulty can be valid or invalid
def Test_Difficulty_Valid(difficulty: str):
    if difficulty.upper() in DIFFICULTIES:
        return True
    else:
        return False

def RunDifficultyTest():
    wasSuccess = False
    if(Test_Difficulty_Valid("EASY") and Test_Difficulty_Valid("MEDIUM") and Test_Difficulty_Valid("eAsY") and not Test_Difficulty_Valid("BLUE")):
        wasSuccess = True
    return wasSuccess
def RunGameStateTest():
    testState = GameState("EASY")
    testState.select_next_word()
    if testState.get_word() in get_possible_words_from_difficulty("EASY"):
        return True
    else:
        return False
def RunGameStateFailTest():
    testState = GameState("MEDIUM")
    testState.select_next_word()
    if testState.get_word() in get_possible_words_from_difficulty("EASY"):
        return True
    else:
        return False
def RunGameStateOnEasyWithFailCount():
    testState = GameState("EASY")
    testState.select_next_word()
    if testState.get_attempt_score() == "Remaining Slices: 15":
        return True
    else:
        return False

def run_tests():
    print("Difficulty Test returned " + str(RunDifficultyTest()))
    print("We made a game state with the easy difficulty. Is the chosen word from the right list?: " + str(
        RunGameStateTest()))
    print("We made a game state with the medium difficulty. Is the chosen word from the EASY list?: " + str(
        RunGameStateFailTest()))
    print("We made a game state with the easy difficulty. Did we have 15 remaining slices at the start: " + str(
        RunGameStateFailTest()))