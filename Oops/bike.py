class Bike:
    
    
    def __init__(self,name,brand,price):
        self.name=name
        self.brand=brand
        self.price=price
    
    def __str__(self):
        return self.name
    
    
    

class Showroom:
     
     
     def __init__(self,name,place):
        self.name=name
        self.place=place
        self.bikes=[]
        
     def add_vechile(self,bike):
         self.bikes.append(bike)
         
     def list_vechiles(self):
         for b in self.bikes:
             print(b)
        
        

    
activa_instance=Bike("activa","honda",10000)
hunter_instance=Bike("hunter","re",30000)
jupiter_instance=Bike("jupiter","re",15000)

