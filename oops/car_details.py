class car:
    company=0
    price=0
    color=0

    def car_details(self):
        print("company : ",self.company)
        print("price : ",self.price)
        print("color : ",self.color)
        print()
        print()
car1=car()
car2=car()
car3=car()

car1.company='KIA'
car1.price=300000
car1.color="Black"

car2.company='Toyota'
car2.price=600000
car2.color="Blue"

car3.company='Mercedes'
car3.price=750000
car3.color="Red"

print("Car 1 details")
print()
car1.car_details()
print("Car 2 details")
print()
car2.car_details()
print("Car 2 details")
print()
car3.car_details()
