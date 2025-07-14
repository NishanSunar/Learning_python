class employee:
    name = "Nishan"
    company = "Microsoft"
    
    def __init__(self):
        print("constructor of employee")
    def show(self):
        print(f"The name of the employee is {self.name} and the company is {self.company}")
class Greet(employee):    #this holds the attributes and methods of employee
    def __init__(self):
        super().__init__()   #this calls the method of its parent class
        print("constructor of greet")
    @staticmethod
    def greet():
        
        print("Namaste")
               
class programmer(Greet):     #this holds the attributes and methods of both class employee and greet
    company = "Dell"
    
    def __init__(self):
        super().__init__()
        print("constructor of programmer")



b = programmer()
b.show()
b.greet()