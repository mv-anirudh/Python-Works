def add_number(n1,n2):
    return n1+n2


def add_number(n1,n2,n3):
    return n1+n2+n3

print(add_number(100,200,300))
 
 
 ## python do not support method overloading bt deafult
 ## function decalration is obscured by a ddeclaration of the same name 
 
 
 
def add_numbers(*args):
     print(sum(args))
     
     
add_numbers(10,20,30)