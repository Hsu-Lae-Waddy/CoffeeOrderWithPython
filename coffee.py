class Coffee:
    def __init__(self,name,size):
        self.name=name
        self.size=size
        self.price=self.calculate()

    def calculate(self):
       if self.size == "small":
           return 5000
       elif self.size =="medium":
           return 7000
       else :
           return 9000 
    def changeSize(self,newSize):
        self.size=newSize
        self.price=self.calculate()
        print(f"{self.name} is changed to {self.size}")
    def descript(self):
        print(f"Coffee: {self.name}, Size: {self.size} , Cost: {self.price}")

    

order1=Coffee("Latte","medium")
order2=Coffee("Espresso","small")

order1.descript()
order2.descript()

order3= Coffee("Cappuccino", "small")
order3.changeSize("large")
order3.descript()



        