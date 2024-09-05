class Dishes:
    
    def __init__(self,name,price,caloreis):
        self.name=name
        self.price=price
        self.calories=caloreis
    
    def __str__(self):
        return self.name    
    
    
    
class Resturant:
     def __init__(self,name,place):
         self.name=name
         self.place=place
         self.dishes=[]
         
     def __str__(self):
         return self.name
     
     def add_dishes(self,dish):
         self.dishes.append(dish)
         
     def list_dishes(self):
         for d in self.dishes:
             print(d)
             
briyani=Dishes("biriyani",130,500)
mandhi=Dishes("mandhi",720,750)

resturant1=Resturant("paradise","kakkand")
resturant2=Resturant("hotbox","kochi")

resturant1.add_dishes(briyani)
resturant1.add_dishes(mandhi)

resturant1.list_dishes()
        
    
    
    