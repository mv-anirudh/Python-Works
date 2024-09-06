class Grandparent:
    def m1(self):
        print("grandparent class m1 method")
        

class Parent(Grandparent):
    def m2(self):
        print("parent class m2 method")
        
        
class Child(Parent):
    def m3(self):
        print("child class m3 method")
    


child=Child()
child.m3()
child.m2()
child.m1()