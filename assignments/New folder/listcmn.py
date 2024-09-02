list1=[2,3,4,5,6]
list2=[4,5,7,8,]
def list_cmn(l1,l2):
    for n1 in list1:
        if n1 in list2:
            return True
    return False
        
result = list_cmn(list1, list2)
print(result)