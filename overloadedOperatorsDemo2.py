class overloading:
    def __init__(self, var1, var2):
        self.var1 = var1
        self.var2 = var2
        print("Value of var1 and var2 is %d and %d" %(self.var1,self.var2))

    def __str__(self):
        return "returning a string from it"

    def __len__(self):
        return self.var2+self.var1

    def __add__(self,var):
        self.var3 = self.var1 + var
        return "Sum of var1 and var2 is %r" %(self.var3)


if __name__ == '__main__':
    obj = overloading(10,20)
    print(obj)
    print(len(obj))
    print(obj+20)



    
