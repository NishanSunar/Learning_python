'''
1 for snake
-1 for water
0 for gun
'''

import random
computer = random.choice([-1,0,1])
player = input("Enter your choice:")
youDict = {"S": 1, "W": -1, "G": 0}
reverseDict = {1:"Snake", -1 : "Water", 0 : "Gun"}
you = youDict[player]
print(f"You choose: {reverseDict[you]} \nComputer choose : {reverseDict[computer]}")

if(computer == -1 and you == 1):
    print("You win!")
elif(computer == -1 and you == 0):
    print("You lose!")
elif(computer == -1 and you == -1):
    print("You draw!")
elif(computer == 1 and you == -1):
    print("You lose!")
elif(computer == 1 and you == 1):
    print("You draw!")
elif(computer == 1 and you == 0):
    print("You win!")
elif(computer == 0 and you == 0):
    print("You draw!")
elif(computer == 0 and you == 1):
    print("You lose!")
elif(computer == 0 and you == -1):
    print("You win!")
else:
    print("Something went wrong!")
    