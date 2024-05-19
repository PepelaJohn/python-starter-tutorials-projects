import random

correct = False

number = random.randint(0,100)
guesses = 0
while not correct:
    answer = input("Guess a number between 0 and 100: ")
    if not answer.isdigit():
        print("Not a digit")
        continue
    if int(answer) == number:
        correct = True
    
    elif int(answer) < number:
        print("Less Than")
    else :
        print('Larger')
    guesses += 1

print("You took ", guesses, " guesses to get the right answer")