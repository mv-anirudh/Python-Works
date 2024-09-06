class Grandparent:
    def m1(self):
        print("garndparent class m1 method")
        
class Parent:
    def m2(self):
        print("parent calss m2 method")
        
class Child(Grandparent,Parent):##multiple inheritance
    def m3(self):
        print("child classs m3 method")
        
child=Child()
child.m3()
child.m2()
child.m1()