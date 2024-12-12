class Employee:
    company_name = "Jaguar Landrover"
    location = "Pullur"

    def __init__(self, id, name, salary):
        self.id = id
        self.name = name
        self.salary = salary
    def details(self):
        print(self.id,self.name,self.salary)

emp1 = Employee(101, "Suraj", 500000)
emp2 = Employee(102, "Mujeeb", 1000000)

emp1.details()
emp2.details()


