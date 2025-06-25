#Rename the file

with open("CHAPTER_9/old.txt") as f:
    content = f.read()
    
with open("CHAPTER_9/renamed_by_python.txt","w") as f:
    f.write(content)