from re import finditer

text="abc 7Klefg@#"

# pattern="\D"  #-D-->excludes digits and gives all other char----d-->gives all digits
#pattern="\\W"   #  --w-->gives alphanum---W--->exculde alphanum
pattern="\\"


matcher=finditer(pattern,text)

for m in matcher:
    print(m.start(),"=>",m.group())