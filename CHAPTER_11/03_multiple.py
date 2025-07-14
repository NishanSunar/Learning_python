class employee:
    name = "Nishan"
    company = "Microsoft"
    def show(self):
        print(f"The name of the employee is {self.name} and the company is {self.company}")
class Greet(employee):    #this holds the attributes and methods of employee
    @staticmethod
    def greet():
        print("Namaste")
               
class programmer(Greet):     #this holds the attributes and methods of both class employee and greet
    company = "Dell"



b = programmer()
b.show()
b.greet()