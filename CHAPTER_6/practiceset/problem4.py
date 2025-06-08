#Write a program to find whether a given username contains less than 10 characters or not>

user = input("Enter the username:")
length = len(user)
if(length >= 10 ):
    print("It contains more than 10 characters.")
else:
    print("It contains less than 10 characters.")