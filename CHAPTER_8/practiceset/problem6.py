list = ["Nishan","is","an", "engineer", "boy"]

def remove(list, word):
    n = []
    
    for item in list:
        if not(item == word):
            n.append(item.strip(word))
    return n
       
    
    
print(remove(list,"an"))