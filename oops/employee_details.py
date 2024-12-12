class employee:
    basic=0
    TA=0
    DA=0
    def salary(self):
        print("Salary : ",self.basic+self.TA+self.DA)

emp1=employee()
emp1.basic=20000
emp1.TA=500
emp1.DA=100

emp2=employee()
emp2.basic=60000
emp2.TA=5000
emp2.DA=600


emp1.salary()
emp2.salary()
