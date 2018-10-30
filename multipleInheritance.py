class parentClass1:
    def func(self):
        print("This is my func function in the parent class1")

class parentClass2:
    def func(self):
        print("This is my func function in the parent class2")

class childClass(parentClass1, parentClass2):
    '''childClass  is inheriting its properties from multiple parent class'''
    def func(self):
        #super(childClass, self).func()
        parentClass2.func(self)

if __name__ == '__main__':
    childObj = childClass()
    childObj.func()