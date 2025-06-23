with open("CHAPTER_9/file.txt") as f:
    content = f.read()
    
with open("CHAPTER_9/this_copy.txt","w") as f:
    f.write(content)