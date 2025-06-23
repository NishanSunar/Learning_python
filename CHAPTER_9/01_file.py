#reading data from file
f = open("CHAPTER_9/01_file.txt")
data = f.read()
print(data)
f.close() 



#writing data to the file

data = "\nhello baby my name is nishant"

f = open("CHAPTER_9/01_file.txt","a")
f.write(data)
f.close()
