import random
n = random.randint(1,100)
a = -1
guesses = 0
while(a != n):
    guesses += 1
    a = int(input("Guess a number: "))
    if (a > n):
        print("Lower Number Please")
    else:
        print("Higher Number Please")
        
print(f"You Guessed the right number correctly in {guesses} attempts")
    
