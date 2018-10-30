class World:
    def __init__(self):
        self._color = None   # protected variable
        self.__content = None   # private variable

    def fill(self, content, color):
        self.__content = content
        self._color = color


if __name__ == '__main__':
    wObj = World()
    wObj.fill("dummy", "blue")
    print(wObj._color)
    #print(wObj.__content)
    #Name Mangling
    print(wObj._World__content)