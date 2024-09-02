f=open("C:\\Users\\Ashok\\OneDrive\\Desktop\\PythonJuneWorks\\fileprograms\\stud.txt","r")
students=[]
for stud in f:
    students.append(stud.rstrip("\n"))
    
    print(students)