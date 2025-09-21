h="Hello, \nFucking World"
print(h)
#Inheritance
 #Hirarchical Inheritance
class A:
    def display1(self):
        print("I am in class A")
class B(A):
    def display2(self):
        print("I am in class B")
class C(A):
    def display3(self):
        print("I am in class C")

class D:
    def display4(self):
        print("I am in class D")

ob1=B()
ob1.display1()

#Multilevel Inheritance
class A:
    def display1(self):
        print("I am in class A")
class B(A):
    def display2(self):
        print("I am in class B")
class C(B):
    def display3(self):
        print("I am in class C")

class D:
    def display4(self):
        print("I am in class D")

ob2=C()
ob2.display1()

#Multiple Inheritance
class A:
    def display1(self):
        print("I am in class A")
class B:
    def display2(self):
        print("I am in class B")
class C(A,B):
    def display3(self):
        print("I am in class C")

ob2=C()
ob2.display1() 
'''Nijeer class ke age pradhanno dibe then , first inheritence then next then next'''
