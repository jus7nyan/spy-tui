import os
import keyboard as kb

class Window:
    def __init__(self):
        rows, columns = os.popen('stty size', 'r').read().split()
        self.Rows, self.Columns = int(rows),int(columns)
        self.Name = "Window"
        self.grid = []
        self.Objects = []
        self.hotkeys = []
    
    def update_size(self):
        rows, columns = os.popen('stty size', 'r').read().split()
        self.Rows, self.Columns = int(rows),int(columns)
        return rows, columns

    def set_grid(self,n):
        for i in range(n):
            self.grid.append([])

    def addObject(self, *args):
        for i in args:
            self.grid[i.gridpos].append(i)
            self.Objects.append(i)
    
    def dellObject(self, *args):
        for i in args:
            self.grid[i.gridpos]
            self.Objects.remove(i)
    
    def render(self):
        rows,columns = int(self.update_size()[0]), int(self.update_size()[1])
        screen = ""
        
        objects = self.Objects
        
        for i in objects:
            result = i.result()
            pos = i.position
            if pos == "center":
                for j in result:
                    if i.View == "simple":
                        screen += " "*(columns // 2 - (len(i.Text)//2+2)) + j + "\n"
                    else:
                        screen += " "*(columns // 2 - (len(result[0])//2+2)) + j + "\n"

            elif pos == "left":
                for j in result:
                    screen += j + "\n"
            elif pos == "right":
                for j in result:
                    screen += " "*(columns - len(result[0]))+j+"\n"
            else:
                return "Position ERROR"
        return rows, columns, screen
    
    def gridrender(self):
        rows,columns = int(self.update_size()[0]), int(self.update_size()[1])
        screen = ""
        
        objects = self.grid
        
        for i in range(len(objects)):
            for j in range(len(objects[i])):
                pass
                
    
    def scprint(self):
        rows, columns, screen = self.render()
        screen = " "*(columns//2-len(self.Name))+self.Name+"\n"+"═"*columns+screen

        os.system("clear")
        print(screen)
    
    def Change_selection(self,arg):
        obj = self.Objects
        if arg == "next":
            for i in range(len(obj)):
                if obj[i].is_choise == True:
                    try:
                        if obj[i+1].can_choise == True:
                            obj[i+1].is_choise = True
                        else:
                            continue
                    except:
                        if obj[(len(obj)-1)-i].can_choise == True:
                            obj[(len(obj)-1)-i].is_choise = True
                        else:
                            continue
                    break
            obj[i].is_choise = False
        elif arg == "perv":
            for i in range(len(obj)):
                if obj[i].is_choise == True:
                    try:
                        if obj[i-1].can_choise == True:
                           obj[i-1].is_choise = True
                        else:
                            continue
                    except:
                        if obj[i-len(obj)].can_choise == True:
                            obj[i-len(obj)].is_choise = True
                        else:
                            continue
                    break
            obj[i].is_choise = False

    
    def switch_press(self):
        ob = self.Objects
        for i in obj:
            pass
    
    def Manipulate(self):
        self.scprint()
        event = kb.read_event()
        obj = self.Objects

        if event.event_type == kb.KEY_DOWN:
            if event.name == "up":
                self.Change_selection("perv")
                self.scprint()
            
            elif event.name == "down":
                self.Change_selection("next")
                self.scprint()
                
            elif event.name == "space":
                for i in obj:
                    if i.is_choise == True and i.can_press == True:
                        func = i.Func
                        func(self)
                self.scprint()

            else:
                self.scprint()
        return self


    def setName(self,Name):
        self.Name = Name
