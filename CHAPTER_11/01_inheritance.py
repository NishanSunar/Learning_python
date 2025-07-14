class employee:
    name = "Nishan"
    company = "Microsoft"
    def show(self):
        print(f"The name of the employee is {self.name} and the company is {self.company}")
        
class programmer(employee):
    company = "Dell"

a = employee()
b = programmer()
a.show()
b.show()