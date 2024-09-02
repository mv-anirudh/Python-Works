#valid pancard number {1-3}alha 4{PCAFHT}ANY ONE {5} alpha {4digit } {one alpha }
#-------------------------------------------------------------------------------------------------------------------------------------

from re import fullmatch

pan_num="ABCTY1234D"

pattern="[A-Z]{3}[PCAFHT][A-Z]\\d{4}[A-Z]"

matcher=fullmatch(pattern,pan_num)
print("valid"if matcher!=None else "not valid")