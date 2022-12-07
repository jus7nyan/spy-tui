import os

class Window:
    def __init__(self):
        stroki, columns = os.popen('stty size', 'r').read().split()
        self.Size = (int(stroki),int(columns))
        self.Grid = (3,3)
        self.Objects = []
    
    def render(self):
        screen = ""
        for i in self.Objects:
            for j in i.result():
                screen += str(j)+""
        return screen
    
    def print(self, screen):
        print(screen)
    
    def addObject(self, object):
        try:
            self.Objects.append(object)
            return 0
        except:
            return 1

    def dellObject(self):
        pass

