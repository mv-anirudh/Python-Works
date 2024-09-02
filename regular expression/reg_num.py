from re import fullmatch

f = open("C:\\Users\\Ashok\\OneDrive\\Desktop\\PythonJuneWorks\\regular expression\\reg_num.txt", "r")
w=open("C:\\Users\\Ashok\\OneDrive\\Desktop\\PythonJuneWorks\\regular expression\\valreg_num.txt","w")


pattern="(KL)(\\s)?[0-9]?[1-9](\\s)?[A-Z]{1,2}(\\s)?[0-9]{4}"


for line in f:
    line= line.rstrip("\n")
    matcher=fullmatch(pattern,line)
    if matcher!=None:
      
        w.write(line +"\n")
    
        

    


      

