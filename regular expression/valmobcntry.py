from re import fullmatch

number="91 9544541391"

pattern="(91)\\s?[6-9]\\d{9}"

matcher=fullmatch(pattern,number)

print("invalid" if matcher==None  else "valid")