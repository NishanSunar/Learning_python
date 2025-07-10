class programmer:
    company = "Microsoft"
    def __init__(self, name , salary, pin):
        self.name = name 
        self.salary = salary
        self.pin = pin
    
    
p = programmer("Nishan",1200000,9080) 
print(p.name, p.salary, p.company, p.pin) 