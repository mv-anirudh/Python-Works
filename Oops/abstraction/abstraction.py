from abc import ABC,abstractmethod
 
class Car():
    
    @abstractmethod
    def start(self):
        pass
    
    @abstractmethod
    def accelerates(self):
        pass
    
    @abstractmethod
    def stop(self):
        pass
    
    
class swfit:
    
    def start(self):
        print("car is starting")
        
    def acclerates(self):
        print("car accelerates")
        
    def stop(self):
        print("car stops")
    
sw=swfit()
sw.start()
sw.acclerates()
sw.stop()