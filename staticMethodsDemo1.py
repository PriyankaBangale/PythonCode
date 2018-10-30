class Cruise:
    discount = 0.5

    #Static Method can only use static attribute or variable
    @staticmethod
    def adjust_discount(num):
        Cruise.discount = num
        
class Sunsetsail(Cruise):
    pass

if __name__ == '__main__':
    print(Cruise.discount)
    print(Sunsetsail.discount)

    Cruise.adjust_discount(.10)
    Sunsetsail.adjust_discount(.25)

    print("Cruise ",Cruise.discount)
    print("Sunsetsail ",Sunsetsail.discount)
