from re import finditer

text="ab12xyz678#$pqr123cdef"

# pattern="[a-z]{3}"
#pattern="[c-ht-z]"
pattern="([a-z]{3}|[0-9]{3})"#or fuction so op of 3 a-z and 3 0-9 
matcher=finditer(pattern,text)

for m in matcher:
    print(m.start(),"==>",m.group())
    