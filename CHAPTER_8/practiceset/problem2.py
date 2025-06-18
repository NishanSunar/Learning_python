#Write a program using function to convert celsius to fahrenheit

def cel_to_farh(celcius):
    farh = (celcius * 9/5) + 32
    return farh
    
    
temp = float(input("Enter the temperture in Celcius:"))
print(f"The equivalent temperature in farhenheit is {cel_to_farh(temp)}")