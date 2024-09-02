placement={"Django":35,"bigdata":45,"java":65,"pbi":25,"c++":32}
def get_value(key):
    return placement.get(key)
srt=sorted(placement,key=get_value,reverse=True)
print(srt)