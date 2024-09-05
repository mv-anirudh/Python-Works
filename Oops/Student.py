class Student:
    
    name: str
    roll_no: int
    course: str
    age: int
    gender: str
    
    def __init__(self, name, roll_no, course, age, gender):
        self.name = name
        self.roll_no = roll_no
        self.course = course
        self.age = age
        self.gender = gender
        
    def display(self):
        print(f"Name: {self.name}\nRoll No: {self.roll_no}\nCourse: {self.course}\nAge: {self.age}\nGender: {self.gender}")

# Create an instance of the Student class and call the display method
student_instance = Student("John", 11, "Python", 21, "Male")
student_instance.display()
