class A(object):
    def __init__(self, age):
        print("Age: 18 ")
        self.age=age

class B(A):
    def __init__(self,age):
        A.__init__(self,age)
        print("Age: 21")
        self.age=age
obj=B("Age")
