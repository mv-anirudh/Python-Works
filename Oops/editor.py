

class Editor:
    def __init__(self,name,vendor):
     self.name=name
     self.vendor=vendor
    
    
    
    def open(self):
      print(f"{self.name} open") 
     
     
    def execute(self):
        print(f"{self.name}execute")

class Vscode(Editor):
    def __init__(self, name, vendor):
       super().__init__(name, vendor)
       
       
class Pycharm(Editor):
    def __init__(self, name, vendor):
       super().__init__(name, vendor)
       

Vscode_instance=Vscode("vscode","microsoft")
Pycharm_instance=Pycharm("pychram","Jetbrains")
    
Vscode_instance.open()
Vscode_instance.execute()
Pycharm_instance.open()
Pycharm_instance.execute()

