#example-- sometimes we want to play pubg if the day is sunday

a = int(input("enter your age:"))

#if elif else ladder
if a >= 18 :
    print("You are above the age of consent.")

elif (a < 0):
    print("You are entering invalid age.")
else :
    print("You are underage.")
    
print("End of program")