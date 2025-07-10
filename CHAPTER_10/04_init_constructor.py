class Employee:       #class
    
    language = "py"
    salary = 1500000
    
    def __init__(self):     #dunder method which is automatically called
        print("I am creating an object")


nishan = Employee()         
nishan.name = "Nishan"    
nishan.language= "javascript"   #instance attribute have more preference than class attribute
print(nishan.name,nishan.language,nishan.salary)


