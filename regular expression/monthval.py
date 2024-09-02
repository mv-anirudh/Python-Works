#chk valid month 

from re import fullmatch
text="14"

pattern="(0?[1-9]|1[0-2])"###if 0 --only 1-9---if 1 only 1-2--- () cause or---

matcher=fullmatch(pattern,text)
print("invalid" if matcher==None  else "valid")