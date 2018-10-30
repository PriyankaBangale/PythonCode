class Listmgr:
    def __init__(self, initial_list):
        self.initial_list = initial_list

    def __add__(self, value):
        retlist = []
        for element in self.initial_list:
            retlist.append(element+value)
        return retlist

if __name__ == '__main__':
    nums = Listmgr([100, 50, 250])
    ans1 = nums + 5
    #ans2 = nums + 10 + 5
    print(ans)