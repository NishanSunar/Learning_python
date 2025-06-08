#write a program to find if the given name is present in the list or not

names = ["Nishan", "Suman", "Suyog", "Sandesh", "Samyog", "Swaroop", "Shandesh"]

given_name = input("Enter the name:")

if(given_name in names):
    print("Your name is in the list.")
else:
    print("Your name is not in the list.")