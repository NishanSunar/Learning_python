with open("CHAPTER_9/log.txt","r") as f:
    lines = f.readlines()
    
lineno = 1
for line in lines:
    if("python" in line):
        print(f"Yes python is present in the line {lineno} ")
        break
    lineno += 1
        
else:
        print("No python is not present ")
    