import random
COLUMNS = 3
ROWS = 3

guesses = {
    "A":3,
    "B":4,
    "C":5,
    "D":6,
}

values = {
    "A":20,
    "B":15,
    "C":10,
    "D":7,
}

def generate_matrix():
    matrix = []
    symbols = []
    for i in guesses.keys():
        symbols.append(i)
    for i in range(COLUMNS):
        columsarr = []
        for i in range(ROWS):
            while True:
                symbol = random.choice(symbols) 

                if columsarr.count(symbol) < guesses[symbol]:
                    columsarr.append(symbol)
                    break

                
        matrix.append(columsarr)
    
    return (matrix)

# generate_matrix()

def print_matrix(matrix):
    for i in range(len(matrix)):
        
        for j in range(len(matrix[i])):
            if j < len(matrix[i]) - 1:
                print(matrix[i][j], end=" | ")
            else:
                print(matrix[i][j])
        print()

def get_lines(balance):
    print(balance)
    while True:
        lines  = input("Enter the lines to bet on (1-3)")   
        if lines.isdigit():
            lines = int(lines)
            if not 1<=lines<=3:
                print("Lines should be between 1 and 3")
                continue
            
        else:
            print("Enter a valid digit") 
            continue 
        # print("passing")
        amount = input("Enter the amount to bet on each line: $")
        if (int(amount) * lines) <= balance:
            balance -= int(amount) * lines
            break
        else:
            print("The amount is greater than your balance", balance)
    return lines, balance, amount     

def bet(matrix, lines, balance, amount):
    
    winnings = []
    
    for i in range(len(matrix)):
        symbol = matrix[i][0]

        if i >= lines:
            break
        
        for j in range(len(matrix[i])):
            if matrix[i][j] != symbol:
                
                break
        else:
            winnings.append(i + 1)
            balance += values[symbol]*int(amount)
    if len(winnings) >0:
        print("You won on line", *winnings, " and your balance is ", balance)
    else:
        print("You lose!  and you have a balance of ", balance)
    return winnings, balance


def main():
    while True:
        balance = input('Enter your deposit: $')
        if balance.isdigit():
            balance = int(balance)
            break
        else:
            print("Enter a valid amount")
    while True:
        user = input("Press Enter to play, q to quit")
        if user.lower == 'q':
            break
        if balance <= 0:
            print("You do not have any money in your account");
            quit()
        lines, balance, amount = get_lines(balance)
        matrix = generate_matrix()
        winnings, balance = bet(matrix, lines, balance, amount)
        print_matrix(matrix)

    
    print(f"Your winnings are on line ", *winnings, " and your balance is ${balance}")

main()
    