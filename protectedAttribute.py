class World:
    def __init__(self):
        self.color = None
        self._content = None # protected variable

    def fill(self, content, color):
        self._content = content
        self.color = color

    def empty(self):
        self._content = None

if __name__ == '__main__':
    wObj = World()
    wObj.fill("dummy","blue")
    print(wObj.color)
    print(wObj._content)
    wObj._content = "dummy1"
    print(wObj._content)
