import src.gamelogic as gameLogic
from src.utility import prompt_input, print_divider


def main_game_loop():
    continue_game = gameLogic.run_main_menu()
    #This will run the main_menu until we say Yes
    while continue_game == False:
        continue_game = gameLogic.run_main_menu()

    selected_difficulty, difficulty_valid = gameLogic.run_difficulty_select()
    while difficulty_valid == False:
        difficulty_valid = gameLogic.run_difficulty_select()
    gameState = GameState(selected_difficulty)
    gameState.select_next_word()
    run_game_loop(gameState)

class GameState:

    used_words = []
    max_failed_attempts_by_difficulty = {
        "EASY" : 15,
        "MEDIUM" : 10,
        "HARD": 5
    }

    #Constructor so we can
    def __init__(self, difficulty):
        self.CurrentAttempts = 0
        self.FailedAttempts = 0
        self.MaxFailedAttempts = self.max_failed_attempts_by_difficulty[difficulty]
        self.CurrentWord = ""
        self.GuessedLetters = []
        self.Difficulty = difficulty

    def select_next_word(self):
        have_we_used_this_word = True
        while have_we_used_this_word == True:
            self.CurrentWord = gameLogic.choose_random_word_from_difficulty(self.Difficulty)
            have_we_used_this_word = self.CurrentWord in self.used_words
        self.CurrentAttempts = 0
        self.FailedAttempts = 0
        self.GuessedLetters = []

    #Will return whether or not the result of making this guess resulted in guessing the whole word
    def make_guess(self, guess):
        guess = guess.lower()
        if len(guess) > 1 and guess == self.CurrentWord:
            self.GuessedLetters = self.get_letters_from_word()
            print("Woah! You guessed the ENTIRE word!")
            return True
        else:
            letters_to_guess = self.get_letters_from_word()
            #lettersToGuess = [A,P,L,E]
            # guess = "A"
            if guess in letters_to_guess:
                self.GuessedLetters.append(guess)
                print("Phew! You're safe, for now, watermelon...")
                return self.did_we_guess_word()
            else:
                self.FailedAttempts = self.FailedAttempts + 1
                self.CurrentAttempts = self.CurrentAttempts + 1
                print("NO!!! The watermelon has been sliced since I guessed wrong!!")
                return False

    def is_game_over(self):
        return self.CurrentAttempts >= self.MaxFailedAttempts

    def did_we_guess_word(self):
        letters_to_guess = self.get_letters_from_word()
        have_we_guessed_word = True
        for letter in letters_to_guess:
            if letter not in self.GuessedLetters:
                have_we_guessed_word = False
        if have_we_guessed_word and self.CurrentWord not in self.used_words:
            self.used_words.append(self.CurrentWord)
        return have_we_guessed_word

    def get_letters_from_word(self):
        lettersToGuess = []
        for letter in self.CurrentWord:
            if letter not in lettersToGuess:
                lettersToGuess.append(letter)
        return lettersToGuess

    def get_word_string(self):
        output_string = ""
        for letter in self.CurrentWord:
            if letter not in self.GuessedLetters:
                output_string += "_"
            else:
                output_string += letter
        return output_string

    def get_attempt_score(self):
        score = "Remaining Slices: "
        remaining = self.MaxFailedAttempts - self.CurrentAttempts
        score += str(remaining)
        return score

    def get_word(self):
        return self.CurrentWord


def run_game_loop(gameState: GameState):
    current_level = 0
    print("GAME STARTED. FIRST WORD")
    while current_level < 3:
        print("LEVEL " + str(current_level + 1))
        while not gameState.did_we_guess_word():
            print_divider("LEVEL " + str(current_level + 1), dospacing=True)
            print(gameState.get_attempt_score())
            print(gameState.get_word_string())
            print_divider(dospacing=True)
            guess = prompt_input("Make a guess: ")
            gameState.make_guess(guess)
            if gameState.is_game_over():
                print("You're a disappointment to this country.. Another watermelon lost to history...")
                return
        gameState.select_next_word()
        current_level = current_level + 1
    print("YOU SAVED THE WATERMELON SOLDIER, THANK YOU FOR YOUR SERVICE! o7")