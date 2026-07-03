from random import randint




class Train:


    def __init__(self, trainNo):
        self.trainNo = trainNo
    def book(self , fro , to):
        print(f"ticket is book in train NO: {self.trainNo} from {fro} to {to}")

    def getstatus(self):
        print(f" train NO: {self.trainNo} from {fro} to {to}vis running succesfully and is on time  ")

    def getfare(self, fro , to ):
        print(f"ticket booked  in train NO: {self.trainNo} from {fro} to {to} is {randint(222 , 5555)}")






t = Train(12399)
t.book("rampur ", "delhi")
t.getfare("Rampoor" , "ludhiana")


