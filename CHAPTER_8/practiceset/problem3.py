#write a recursive function to calculate the sum of first n natural number

def sum(n):
    if(n==1):
        return 1
    return sum(n-1) + n

num = int(input("Enter the number: "))
print(f"the sum of first {num} natural number is {sum(num)}")
    