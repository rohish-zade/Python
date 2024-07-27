capitals_dict = {
'Alabama': 'Montgomery',
'Alaska': 'Juneau',
'Arizona': 'Phoenix',
'Arkansas': 'Little Rock',
'California': 'Sacramento',
'Colorado': 'Denver',
'Connecticut': 'Hartford',
'Delaware': 'Dover',
'Florida': 'Tallahassee',
'Georgia': 'Atlanta',
}

state = input("Pick a state from the dictionary: ")
state = state.capitalize()  # Convert the input to capitalize for case insensitivity
print(state)

while True:
    guess = ""
    if state in capitals_dict:
        print(state)
        capital = capitals_dict[state]
        guess = input("Enter the capital of {}: ".format(state))
        guess = guess.capitalize()  # Convert the guess to capitalize for case insensitivity

        while True:
            if guess == capital:
                print("Correct!")
                break
            elif guess.lower() == "exit":
                print("goodbye section",guess.lower())
                print("The correct answer was: {}".format(capital))
                print("Goodbye!")
                print("goodbye secction:", guess)
                break
            else:
                print("Incorrect. Try again or type 'exit' to quit.")
                guess = input("Enter the capital of {}: ".format(state)).capitalize()
    elif guess.lower() == 'exit':
        print("in exit section",guess)
        break
    else:
        print("Invalid state. Please pick a state from the dictionary.")
        state = input("Pick a state from the dictionary: ")
        state = state.capitalize()
        
