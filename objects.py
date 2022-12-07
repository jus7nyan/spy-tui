from colorama import init
init()
from colorama import Fore, Back, Style



class View:
    
    def __init__(self):
        
        self.simple = ["","\n"]
        
        self.single =  ["┌","", "┐\n",
                        "│","", "│\n",
                        "└","", "┘\n"]
        
        self.double =  ["╔","" ,"╗\n",
                        "║","", "║\n",
                        "╚","" ,"╝\n"]
        self.choise = Fore.BLACK + Back.WHITE
        self.end = Style.RESET_ALL
    
    def get(self,name, text, is_choise):
        if name == "single" and is_choise:
            view = self.single
            view[4] = self.choise + text +self.end
            for i in range(len(text)):
                view.insert(1,"─")
            for i in range(len(text)):
                view.insert(len(text)+7, "─")
            return view

        elif name == "double" and is_choise:
            view = self.double
            view[4] = self.choise + text + self.end
            for i in range(len(text)):
                view.insert(1,"═")
            for i in range(len(text)):
                view.insert(len(text)+7, "═")
            return view
        
        elif name == "simple" and is_choise:
            view = self.simple
            view[0] = self.choise + text +self.end
            return view
        
        elif name == "single":
            view = self.single
            view[4] = text
            for i in range(len(text)):
                view.insert(1,"─")
            for i in range(len(text)):
                view.insert(len(text)+7, "─")
            return view

        elif name == "double":
            view = self.double
            view[4] = text
            for i in range(len(text)):
                view.insert(1,"═")
            for i in range(len(text)):
                view.insert(len(text)+7, "═")
            return view
        
        elif name == "simple":
            view = self.simple
            view[0] = text
            return view


class Label:

    def __init__(self):
        self.is_choise = False
        self.Text = ""
        self.Pos = "center"
        self.Neighbors = 0
        self.View = "simple"
        
    
    def get_info(self, info):
        if info == "text":
            info = self.Text
        elif info == "pos":
            info = self.Pos
        elif info == "view":
            view = self.View
        elif info == "result":
            info = self.result()
        elif info == "is_choise":
            info = self.is_choise
        elif info == "all":
            info = [self.Text, self.Pos, self.View, self.is_choise, self.result()]
        return info
    
    def set(self, text="", pos="center", neighbors=0, view="simple", is_choise = False):
        try:
            self.Text = text
            self.Pos = pos
            self.View = view
            self.is_choise = is_choise
            self.Neighbors = neighbors
        except:
            return 1
    
    def result(self):
        return (View().get(self.View, self.Text, self.is_choise))


class Button:

    def __init__(self):
        self.is_choise = False
        self.Text = ""
        self.Pos = "center"
        self.Neighbors = 0
        self.View = "simple"
        self.is_pressed = False
        self.Func = "on_pressed"
    
    def get_info(self, info):
        if info == "text":
            info = self.Text
        elif info == "pos":
            info = self.Pos
        elif info == "view":
            view = self.View
        elif info == "result":
            info = self.result()
        elif info == "is_choise":
            info = self.is_choise
        elif info == "is_pressed":
            info = self.is_Pressed
        elif info == "all":
            info = [self.Text, self.Pos, self.View, self.is_choise, self.is_pressed, self.Neighbors, self.result()]
        return info
    
    def set(self, text="", pos="center", neighbors=0, view="simple", is_choise = False, is_pressed=False, func = "on_pressed"):
        try:
            self.Text = text
            self.Pos = pos
            self.View = view
            self.is_choise = is_choise
            self.Neighbors = neighbors
            self.is_pressed = is_pressed
            self.Func = func
        except:
            return 1
    
    def result(self):
        return (View().get(self.View, self.Text, self.is_choise, self,is_pressed))