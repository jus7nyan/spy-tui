from colorama import init, Fore, Back, Style
init()

class View:
    def __init__(self):
        self.single = ["┌","─","┐",
                       "│",
                       "└",    "┘"]
        self.double = ["╔","═","╗",
                       "║",
                       "╚",    "╝"]
        self.choise = Fore.BLACK + Back.WHITE
        self.end = Style.RESET_ALL
    
    def get(self, object):
        view = object.View
        text = object.Text
        choise = object.is_choise
        text = text.split("\n")
        maxlen = len(max(text))
        rows = len(text)
        
        if view == "simple":
            result = []
            if choise == True:

                for i in range(rows):
                    result.append(self.choise + text[i] +" "*(maxlen-len(text[i]))+ self.end)
            else:
                for i in range(rows):
                    result.append(text[i] +" "*(maxlen-len(text[i])))
            return result
        
        elif view == "single":
            if choise == True:
                
                result0 = [self.single[0]+self.single[1]*maxlen+self.single[2]]
                resultt = []
                result1 = [self.single[4]+self.single[1]*maxlen+self.single[5]]
                
                for i in range(rows):
                    resultt.append(self.single[3]+self.choise+text[i]+" "*(maxlen-len(text[i]))+self.end+self.single[3])
                
                result = result0+resultt+result1
                
                return result
            else:

                
                result0 = [self.single[0]+self.single[1]*maxlen+self.single[2]]
                resultt = []
                result1 = [self.single[4]+self.single[1]*maxlen+self.single[5]]
                
                for i in range(rows):
                    resultt.append(self.single[3]+text[i]+" "*(maxlen-len(text[i]))+self.single[3])
                
                result = result0+resultt+result1
        
        elif view == "double":
            if choise == True:
                
                result0 = [self.double[0]+self.double[1]*maxlen+self.double[2]]
                resultt = []
                result1 = [self.double[4]+self.double[1]*maxlen+self.double[5]]
                
                for i in range(rows):
                    resultt.append(self.double[3]+self.choise+text[i]+" "*(maxlen-len(text[i]))+self.end+self.double[3])
                
                result = result0+resultt+result1
                
                return result
            else:
                
                result0 = [self.double[0]+self.double[1]*maxlen+self.double[2]]
                resultt = []
                result1 = [self.double[4]+self.double[1]*maxlen+self.double[5]]
                
                for i in range(rows):
                    resultt.append(self.double[3]+text[i]+" "*(maxlen-len(text[i]))+self.double[3])
                
                result = result0+resultt+result1
                
        return result

                                    # Label class
class Label:
    def __init__(self):
        self.Text = ""                              # text of the label
        self.View = "simple"                        # what like label look
        self.is_choise = False                      
        self.can_choise = False
        self.can_press = False
        self.position = [0, "center"]
        self.len = len(self.Text)
        self.gridpos = 0
    
    def set(self, text = -1,
            view = -1,
            is_choise = -1,
            can_choise = -1,
            func = -1,
            pos = -1,
            gridpos = -1):
        
        
        if text != -1:
            self.Text = text
        if view != -1:
            self.View = view
        if is_choise != -1:
            self.is_choise = is_choise
        if can_choise != -1:
            self.can_choise = can_choise
        if pos != -1:
            self.position = pos
        if gridpos != -1:
            self.gridpos = gridpos
    
    def result(self):
        return View().get(self)




                                            # Button class
class Button:
    def __init__(self):
        self.Text = ""                          # Text on button
        self.View = "simple"                    # what like button look
        self.is_choise = False                  # whether the button is selected
        self.is_pressed = False                 # whether the button is pressed
        self.can_choise = True                  # is it possible to choise the button
        self.can_press = True                   # is it possible to press the button
        self.Func = self.base_func              # function of the button
        self.position = "center"                # lowercase button position
        self.len = len(self.Text)               # button text length
        self.gridpos = 0                        # button position in a column
    
    def base_func():
        return 0
    
    def set(self, text = -1,                    # set the parameters of button
            view = -1,
            is_choise = -1,
            can_choise = -1,
            func = -1,
            pos = -1,
            gridpos = -1):
        
        if text != -1:
            self.Text = text
        if view != -1:
            self.View = view
        if is_choise != -1:
            self.is_choise = is_choise
        if can_choise != -1:
            self.can_choise = can_choise
        if pos != -1:
            self.position = pos
        if func != -1:
            self.Func = func
        if gridpos != -1:
            self.gridpos = gridpos
        
    def result(self):                           # end view of the button
        return View().get(self)
