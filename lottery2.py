import random
from pathlib import Path

print("This program simulates a Lottery\n")
print("Type \"help\" for information")

# initialzise stats
if(Path("./save.txt").is_file()):
    save_file = open("./save.txt", "r")
    money = int(save_file.readline())
    money_won = int(save_file.readline())
    money_lost = int(save_file.readline())
    won_2 = int(save_file.readline())
    won_3 = int(save_file.readline())
    won_4 = int(save_file.readline())
    won_5 = int(save_file.readline())
    won_6 = int(save_file.readline())
    lost = int(save_file.readline())
    paid = int(save_file.readline())


else:    
    money = 1000
    money_won = 0
    money_lost = 0
    won_2 = 0
    won_3 = 0
    won_4 = 0
    won_5 = 0
    won_6 = 0
    lost = 0
    paid = 0

def won_total():
    return won_2 + won_3 + won_4 + won_5 + won_6

# save stats, called when program gets quitted correctly and when money is not enough
# to play again
def save():
    file = open("./save.txt", "w")
    file.write(str(money) + "\n")
    file.write(str(money_won) + "\n")
    file.write(str(money_lost) + "\n")
    file.write(str(won_2) + "\n")
    file.write(str(won_3) + "\n")
    file.write(str(won_4) + "\n")
    file.write(str(won_5) + "\n")
    file.write(str(won_6) + "\n")
    file.write(str(lost) + "\n")
    file.write(str(paid) + "\n")
    file.close()

# start of game
while True:
    print()
    command = input("> ")
    print()

    if command == "help":
        print("help - display useful information")
        print("stat - show statistics")
        print("play - try your luck")
        print("quit - quit program (saves statistics)\n")
        print("if you want to play a new game delete the save file")

    elif command == "stats":
        print("Money : " +str(money) + "\n")
        print("Money won  : " + str(money_won))
        print("Money lost : " + str(money_lost) + "\n")
        print("Games won  : " + str(won_total()))
        print("Games lost : " + str(lost) + "\n")
        print("2 right: " + str(won_2))
        print("3 right: " + str(won_3))
        print("4 right: " + str(won_4))
        print("5 right: " + str(won_5))
        print("6 right: " + str(won_6))

    elif command == "play":
        if money >= 2:
            money -= 2
        else:
            print("You dont have enough money!")
            save()
            break

        draw = sorted(random.sample(range(1,50), 6))
        tries = []
        for i in range(6):
            tries.append(int(input("Number " + str(i + 1) + ": ")))

        right_numbers = 0
        if tries[0] in draw: right_numbers += 1 
        if tries[1] in draw: right_numbers += 1
        if tries[2] in draw: right_numbers += 1
        if tries[3] in draw: right_numbers += 1
        if tries[4] in draw: right_numbers += 1
        if tries[5] in draw: right_numbers += 1

        print("The draw was: " + str(draw))
        print("Right numbers: " + str(right_numbers))

        money_won_currently = 0
        if right_numbers <= 1:
            print("You won nothing.")
            lost += 1
            money_lost += 2

        elif right_numbers == 2:
            money_won_currently = 5
            print("You won 5 dollars!")
            won_2 += 1

        elif right_numbers == 3:
            money_won_currently = 220
            print("You won 220 dollars!")
            won_3 += 1

        elif right_numbers == 4:
            money_won_currently = 5000
            print("You won 5.000 dollars!")
            won_4 += 1

        elif right_numbers == 5:
            money_won_currently = 190000
            print("You won 190.000 dollars!")
            won_5 += 1

        elif right_numbers == 6:
            money_won_currently = 20000000
            print("You won 20.000.000 dollars!")
            won_6 += 1

        money_won += money_won_currently
        money += money_won_currently

    elif command == "quit":
        save()
        break

    else:
        print("unknown command")