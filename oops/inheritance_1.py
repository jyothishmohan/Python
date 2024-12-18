class fruits:
    def eat(self):
        print("we can eat fruits")
class orange(fruits):
    pass
class apple(fruits):
    def eat(self):
        print("Apple is sweet")

org1=orange()
app1=apple()
org1.eat()
app1.eat()
