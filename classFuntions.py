class demo:
    def __init__(self):
        self.age = 10

if __name__ == '__main__':
    obj1 = demo()
    print(hasattr(obj1, 'age'))
    #print(getattr(obj1, 'age'))
    #setattr(obj1,'age',11)
    #print(getattr(obj1, 'age'))
    delattr(obj1,'age')
    print(hasattr(obj1, 'age'))
    #print(getattr(obj1, 'age'))