
class View:
    
    def __init__(self):
        
        self.simple = ["","\n"]
        
        self.single =  ["┌","", "┐\n",
                        "│","", "│\n",
                        "└","", "┘\n"]
        
        self.double =  ["╔","" ,"╗\n",
                        "║","", "║\n",
                        "╚","" ,"╝\n"]
    
    def get(self,name, text):
        if name == "single":
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
        self.Text = ""
        self.Pos = "center"
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
        elif info == "all":
            info = [self.Text, self.Pos, self.View, self.result()]
        return info
        
    
    def settext(self, text):
        try:
            self.Text = text
            return 0
        except:
            return 1
    
    def setPos(self, pos):
        try:
            self.Pos = pos
        except:
            return 1

    def setView(self, name):
        try:
            self.View = name
            return 0
        except:
            return 1
    
    def result(self):
        return (View().get(self.View, self.Text))


class Button:

    def __init__(self):
        self.Text = ""
        self.is_pressed = False
        self.Pos = "center"
        self.View = View().get("double", self.Text)
