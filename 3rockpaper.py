import random

options = ["r", 'p', 's']
user_wins = 0
comp_wins = 0
while True:
    user = input("Type, R, P or S, Q to quit: ")
    if user == 'q':
        if user_wins > 0 or comp_wins>0:
            print('You have ', user_wins, "wins and the computer wins are ", comp_wins)
        quit()
    if user.lower() not in options:
        print("Invalid input")
        continue
    random_number = random.randrange(0,3)
    computer = options[random_number]
    if user == "r" and computer=='s':
        print("You win")
        user_wins += 1
       
    elif user == 'p' and computer=='r':
        print("You win")
        user_wins += 1
    elif user == 's' and computer=='p':
        print("You win")
        user_wins += 1
    else:
        print("You lost")
        comp_wins += 1
       