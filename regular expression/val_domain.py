from re import fullmatch

f=open("C:\\Users\\Ashok\\OneDrive\\Desktop\\PythonJuneWorks\\regular expression\\domain.txt","r")

w=open("C:\\Users\\Ashok\\OneDrive\\Desktop\\PythonJuneWorks\\regular expression\\com.txt","w")

pattern="[\\w\\W]+\\.com"

for line in f:
    doamin=line.rstrip("\n")
    matcher=fullmatch(pattern,doamin)
    if matcher!=None:
        w.write(doamin + "\n")
    