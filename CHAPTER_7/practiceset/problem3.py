#print multiplication table of given number using while loop

num = int(input("Enter the number:"))

i = 1
while(i<11):
    print(f"{num} x {i} = {num*i}")
    i += 1