#meder monkeys app code
#author: Simon Lee
#input: random number is generated between 1 and 6 on 2 seperate dice, also
#an option to put "y" or "n" to replay game
#output: if sum of both dice is greater than or equal to 9, you win and drink
from random import randint
import math

def roll():
    complete = False
    while not complete:
        done = False
        while not done:
            list1 = []
            playercount = int(input("How many players do you have: "))
            print("\n")
            namecount = 0
            for i in range(int(playercount)):
                if namecount <= playercount:
                    names = input("Enter your names: ")
                    print("\n")
                    list1.append(names)
                    namecount += 1
                    continue
                    
            t = tuple(list1)
            index = t.index(names)

            playcount = 7 
            count = 0
            print("\n")
            for i in range(int(playcount)):
                for i in t:
                    print(i + " it's your turn\n")
                    roll1 = int(randint(1,6))
                    roll2 = int(randint(1,6))
                    rollsum = (roll1 + roll2)
                    print(f"Dice 1: {roll1}\n")
                    input()
                    print(f"Dice 2: {roll2}\n")
                    if rollsum == 9 or rollsum == 10 or rollsum == 11 or rollsum == 12:
                        print("MEDER MONKEY!!!!!\n")
                        print("       .-\"-.            .-\"-.            .-\"-.           .-\"-. ")
                        print("     _/_-.-_\_        _/.-.-.\_        _/.-.-.\_       _/.-.-.\_")
                        print("    / __} {__ \      /|( o o )|\      ( ( o o ) )     ( ( o o ) )")
                        print("   / //  \"  \\ \     | //  \"  \\ |       |/  \"  \|       |/  \"  \|")
                        print("  / / \\'---'/ \ \  / / \\'---'/ \ \      \\'/^\\'/         \\ .-. /")
                        print("  \ \_/`\"\"\"`\_/ /  \ \_/`\"\"\"`\_/ /      /`\ /`\         /`\"\"\"`\ ")
                        print("   \           /    \           /      /  /|\  \       /       \ ")
                        count +=1
                        pass
                    else:
                        print("You Lose\n")
                        count += 1
                        pass
                    
                    if count < playcount:
                        going = input("Keep Going [(tap)/N]").upper()
                        print("\n")
                        if going == "N":
                            done = True
                            break

            
            replay = input("Do you want to play Meder Monkey's again? [(tap)/N]: ").upper()
            print("\n")
            if replay == "N":
                complete = True
                break
            else:
                continue


        
       
print("============Welcome To Meder Monkeys=========")
print("     _                                       ")
print("//\                                          ")
print("V  \                                         ")
print(" \  \_                                       ")
print("  \,'.`-.                                    ")
print("   |\ `. `.                                  ")
print("   ( \  `. `-.                        _,.-:\ ")
print("    \ \   `.  `-._             __..--' ,-';/ ")
print("     \ `.   `-.   `-..___..---'   _.--' ,'/  ")
print("     `. `.    `-._        __..--'    ,' /    ")
print("        `. `-_     ``--..''       _.-' ,'    ")
print("          `-_ `-.___        __,--'   ,'      ")
print("             `-.__  `----\"\"\"    __.-'        ")
print("               `--..____..--'                \n")

print("============Welcome To Meder Monkeys=========\n")

print("RULES: 1. Roll 2 Dice!\n")
print("       2. If Dice total is 9, 10, 11, or 12... you have landed on Meder Monkey!")
print("          When you land on Meder Monkey, YOU DRINK! \n")
print("       3. Meder Monkeys last for Seven Rounds! So be prepared to drink atleast ")
print("          7 times\n")
roll()
print("Goodbye!")
    


        
    

