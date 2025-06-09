#write a program to print multiplication table of given number

num = int(input("Enter a number:"))

print("Multiplication table of ",num)

for i in range(1,11):
    print(f"{num} x {i} = {num*i}")