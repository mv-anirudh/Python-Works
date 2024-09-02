## check numbervalid or not 
#------rule for vech num----------------------------------------------------------------------------------------------------------------------------
#first should be KL
# digit//2//
#letter//2//
#digit//4//
#-------------------------------------------------------------------------------------------------------------------------------------------------------------

from re import fullmatch
vech_num=input("enter your vechile number: ")

pattern="(KL)(-)?[0-9](-)?[A-Z]{1,2}(-)?[0-9]{4}"

matcher=fullmatch(pattern,vech_num)

print("invalid" if matcher==None  else "valid")

