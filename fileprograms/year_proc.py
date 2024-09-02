f=open("C:\\Users\\Ashok\\OneDrive\\Desktop\\PythonJuneWorks\\fileprograms\\years.txt")
f_cen=open("C:\\Users\\Ashok\\OneDrive\\Desktop\\PythonJuneWorks\\fileprograms\\cen_year.txt","w")
f_non_cen=open("C:\\Users\\Ashok\\OneDrive\\Desktop\\PythonJuneWorks\\fileprograms\\non_cen_year.txt","w")

for i in f:
    y=int(i.rstrip("\n"))
    
    if y%100==0:
        f_cen.write(str(y)+"\n")
    else:
        f_non_cen.write(str(y)+"\n")