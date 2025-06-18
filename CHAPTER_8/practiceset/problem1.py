#Write a program using function to find greatest among three numbers

def greatest(a,b,c):
    if(a>=b and a>=c):
        return a
    elif(b>=a and b>=c):
        return b
    elif(c>=a and c>=b):
        return c
    
a = int(input("Enter 1st numbers:"))
b = int(input("Enter 2nd numbers:"))
c = int(input("Enter 3rd numbers:"))
print(f"The greatest is {greatest(a,b,c)}")