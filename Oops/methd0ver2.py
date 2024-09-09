class Operations:
    def add(self,*args):
        total =sum([arg for arg in args if isinstance (arg,(int,float))])       
            
        return total
    
math=Operations()

print(math.add(10,22,34,55.5,"hello"))
