marks = {
    "Nishan" : 100,
    "suyog" : 40,
    "sandesh" : 50,
    "suman" : 80
    
}

print(marks.items()) #this prints all the items of the dictionary
print(marks.keys())# this prints all the keys of the dictionary
print(marks.values()) #this prints all the values of the dictionary

marks.update({"Nishan": 99}) #this update the values of the keys
print(marks["Nishan"])

print(marks.get("suyog")) #gets the value of the key mentioned #this returns None value
print(marks["suyog"]) #this gives error