#Function with passing argument

def goodday(name, end):     #parameter
    print("Good day, " + name)
    print(end)
    return "done"  #return value to the variable calling the function
    
    
a = goodday("nishan", "thankyou")   #passing argument "nishan"
print(a)