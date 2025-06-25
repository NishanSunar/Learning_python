with open("CHAPTER_9/file.txt") as f:
    content1 = f.read()
    
with open("CHAPTER_9/log.txt") as f:
    content2 = f.read()
    
if(content1 == content2) :
    print("Files are identical")
else:
    print("Files are not identical")
    
