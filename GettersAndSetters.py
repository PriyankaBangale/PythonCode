class exampleClass:
    def setName(self,name):
        self.name = name

    def getName(self):
        return self.name

if __name__ == '__main__':
    classObj = exampleClass()
    classObj.setName("PythonClass")
    print(classObj.getName())