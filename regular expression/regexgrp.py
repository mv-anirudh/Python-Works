from re import finditer

text="abc123 @K#7LMdef"
# pattern="[abf]"   #checks weather a b
#pattern="[a-k]" #chk for alpha frm a to k
#pattern="[a-z]"  #chk for all lowcase a to z
#pattern="[A-Z]"   #chk for all uppcase frm AtoZ
#pattern="[A-Za-z]"  #chk for all alph
#pattern="[0-9]"or \d   #chk for all num
#pattern="[A-Za-z0-9]"
#pattern="[^A-Za-z0-9]"#chk for all the char expect alpha num
#pattern="[\s]"# chk for space

pattern="[^A-Za-z0-9\s]" # type: ignore

matcher=finditer(pattern,text)

for m in matcher:
    print(m.start(),"=>",m.group())