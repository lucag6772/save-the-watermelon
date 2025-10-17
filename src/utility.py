#Some optional variables to both save time and serve as a failsafe incase you dont provide the variables
def print_divider(text = "", dospacing = False):
    divider_line = "-----------------"
    #"-----------------" + "-----------------" = "----------------------------------"
    if text is None or text == "":
        divider_line += divider_line
    else:
        divider_line += "[" + text + "]" + divider_line
    if dospacing:
        print(" ")
        print(" ")
    print(divider_line)

# message = variable to give a prefix to what the game is asking us
def prompt_input(message = ""):
    guess = input(message).lower()
    return guess