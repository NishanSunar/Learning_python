#Recursion is a function which calls itself repeatively



#factorial of any number

def factorial(n):
    if (n == 1 or n == 0):
        return 1
    return n * factorial(n-1)

n = int(input("Enter the number for factorial : "))
print(f"The factorial of {n} is {factorial(n)}")
