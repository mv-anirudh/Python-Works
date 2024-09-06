class Person:
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    def display(self):
        print(f"name:{self.name}\nage:{self.age}\ngender:{self.gender}")
        
    def __str__(self):          
        return self.name
    
    
class Emplyoee(Person):
    
    def __init__(self, name, age, gender,eid,department,salary):
        super().__init__(name, age, gender)
        self.eid=eid
        self.department=department
        self.salary=salary
        
    def display(self):
       super().display()
       print(f"eid:{self.eid}\ndepartment:{self.department}\nsalary:{self.salary}")
        
        
emp1=Emplyoee("jhon",34,"male",213,"it",75000)
emp1.display()        
        






     