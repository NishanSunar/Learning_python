#write a program to calculate the factorial of a given number using for loop.

num = int(input("Enter the number for Factorial: "))
fact = 1
if(num == 0):
    print(f"The factorial of {num} is 1")
else:
    for i in range(1,num+1):
        fact = fact * i 
        
print(f"The factorial of {num} is {fact}")