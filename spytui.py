import os

class Window:
    def __init__(self):
        rows, columns = os.popen('stty size', 'r').read().split()
        self.Rows, self.Columns = int(rows),int(columns)
        self.Grid = (3,3)
        self.Objects = []
        
    def update(self):
        rows, columns = os.popen('stty size', 'r').read().split()
        self.Rows, self.Columns = int(rows),int(columns)
    
    def render(self):
        self.update()
        grid = []

        
        screen = ""
        for i in range(self.Grid[0]):
            grid.append([])
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

    def dellObject(self, object):
        try:
            for i in self.Objects:
                if i == object:
                    self.Objects.remove(object)
            return 0
        except:
            return 1
