from abc import ABC,abstractmethod

class Editor(ABC):
    
    @abstractmethod
    def Open(self):
        pass
    @abstractmethod
    def execute(self):
        pass
    @abstractmethod
    def debug(self):
        pass
    

    
    
    
    
class vscode(Editor):
    
    def Open(self):
        print("editor is opening")
        
    def execute(self):
        print("editor is executing")
        
    def debug(self):
        print("editor debuging")
        
    
        
        
        
        
        
vc=vscode()
vc.Open()