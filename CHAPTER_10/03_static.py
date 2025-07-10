class Employee:       #class
    
    language = "py"
    salary = 1500000
    
    def getInfo(self):
        print(f"The language is {self.language}")
    @staticmethod    #usig staticmethod doesn't need any parameer in function
    def Greet():
        print("Namaste")


nishan = Employee()          #object
nishan.name = "Nishan"     #instance attribute
nishan.language= "javascript"   #instance attribute have more preference than class attribute
print(nishan.name,nishan.language,nishan.salary)
nishan.getInfo()  #this becomes  --> Employee.getInfo(nishan)
#HERE  name is object attribute and language and salary are class attribute


nishan.Greet()
