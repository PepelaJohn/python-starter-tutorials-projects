import random


def roll(): 
    return random.randint(0,6)  

while True:
    players = input("Enter the number of players (2-4): ")
    if players.isdigit():
        players = int(players)
        if 2<=players<=4:
            break


max_score = 50

player_scores = [0 for _ in range(players)]

while max(player_scores) < max_score:
    for player in range(players):
        print("Its player no", player + 1, "turn to play")
        player_score = player_scores[player]
        while True:
            print(player_score)
            should_roll = input("Would you like to roll? ")
            if should_roll.lower() != 'y':
                break;
            
            roll_val = roll()
            if roll_val == 1:
                print("You rolled a 1 Done")
                break

            else:
                player_score += roll_val
                
                print("You rolled a : ", roll_val)
        player_scores[player] = player_score  
        
        print("Your total score is :", player_score)

print("Your scores are: ")
for score in player_scores:
    print(score)


