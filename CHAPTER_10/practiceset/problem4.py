import random
class Train:
    
    def __init__(self, trainNo):
        self.trainNo = trainNo
        
    def book(self, fro, to):
        print(f"Ticket is booked in train no : {self.trainNo} from {fro} to {to}")
    def getstatus(self):
        print(f"Train no : {self.trainNo} is running on time")
    def getFare(self, fro , to):
        print(f"Ticket fare in train no: {self.trainNo} from {fro} to {to} is {random.randint(222,5555)}")
        
t = Train(15320)
t.book("kolkata","Delhi")
t.getstatus()
t.getFare("kolkata","Delhi")
    