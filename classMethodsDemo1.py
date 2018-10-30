class Cruise:
    #Class Variable or Attribute
    discount = 0.5
    @classmethod
    def adjust_discount(cls, num):
        cls.discount = num

    def discount1(self,num):
        self.discount = num


class Sunsetsail(Cruise):
    pass

if __name__ == '__main__':
    print(Cruise.discount)
    print(Sunsetsail.discount)
    obj1 = Cruise()
    obj1.discount1(100)
    print(Cruise.discount)

    #Cruise.adjust_discount(.10)
    #Sunsetsail.adjust_discount(.25)

    #print("Cruise ",Cruise.discount)
    #print("Sunsetsail ",Sunsetsail.discount)
