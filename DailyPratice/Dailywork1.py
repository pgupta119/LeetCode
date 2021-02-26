# Method with class

class newClass():
    x=0
    y=0
    def New(self,x,y):
        self.x=x
        self.y=y


def Main():
    n=newClass()
    n.New(7,7)
    print("New Value of X", n.x)
    print("New value of Y", n.y)

if __name__=='__main__':
    Main()


# Class Using Heritance 

class pet():
    def __init__(self, name, age):
        self.name=name
        self.age=age


class  cat(pet):
    def __init__(self,name,age):
        super().__init__(name,age)


def main():
    p=pet("Pet",1)
    c=cat("cat",2)
    print(c.name)
    print(p.name)
    print(c.age)
    print(p.cat("A",1))

if __name__=='__main__':
    main()