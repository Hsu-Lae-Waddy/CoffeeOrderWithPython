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

    

total =0
orders=[]

while True:
    print("/n ... Coffee menu ...")
    print("1. Latte")
    print("2. Espresso")
    print("3. Cappuccino")
    
    choice=input("Choose cofee(1/2/3) or q to quit: ")

    if choice == "q":
        break
    elif choice == "1":
        Coffee_name="Latte"
    elif choice == "2":
        Coffee_name="Espresso"
    elif choice =="3":
        Coffee_name="Cappuccino"
    else:
        print("Invalid choice")
        continue

    size = input("Choose size (small,medium,large): ")
    
    order=Coffee(Coffee_name,size)
    orders.append(order)
    total=total+order.price
    print("order added!")

    print("/n --- Your Orders --- ")
    for i in orders:
        i.descript()

    print(f"Total Price: {total}")
    print("Thank you")
        