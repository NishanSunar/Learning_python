name = "nishan"
print(len(name))  #len() returns the value of length of the string

print(name.endswith("an")) #this return whether the string end with an or not

print(name.startswith("n")) #this return whether the string start with n or not

print(name.capitalize()) #this capitalize the first character of the string

word = "hello world"
index = word.find("world") #this finds the word and return the index where the word start
print(index)

replace_string = word.replace("hello","Bye") #this replace "hello" to "Bye"
print(replace_string)