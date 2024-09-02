from re import fullmatch

text="1"

pattern="(0?[1-9]|(1|2)\\d|3[0-1])"

matcher=fullmatch(pattern,text)

print("invalid" if matcher==None  else "valid")