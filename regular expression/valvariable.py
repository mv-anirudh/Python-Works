from re import fullmatch

variable_name=input("entera variable name :  ")

pattern="[k-m][0369][a-zA-Z0-9@]*"

matcher=fullmatch(pattern,variable_name)
print("invalid" if matcher==None  else "valid")