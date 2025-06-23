words = ["Donkey","ram"]

with open("CHAPTER_9/file.txt","r") as f:
    content = f.read()
    
for word in words:
    contentNew = content.replace(word,'#' * len(word))

with open("CHAPTER_9/file.txt","w") as f:
    f.write(contentNew)