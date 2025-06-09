#wap to check whether a number is prime or not

num = int(input("Enter the number"))
count = 0
for i in range(1,num):
    if(num%i==0):
        count += 1
        
if(count >= 2):
        print(f"{num} is not prime ")
else:
        print(f"{num} is prime")