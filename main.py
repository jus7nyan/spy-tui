import objects
import spytui
import os

window = spytui.Window()
window.set_grid(3)
window.setName("My Window")

button = objects.Button()
label = objects.Label()
label1 = objects.Label()

def on_press(window):
    labelf = objects.Label()
    labelf.set(text="lalalal", pos="center", can_choise=True)
    window.addObject(labelf)
    
button.set(text="hi\nbye\nhmmm",view="double", is_choise=True, pos="center", func=on_press)
label.set(text="bye",view="double", is_choise=False, pos="right", can_choise = True)
label1.set(text="hi",view="double", is_choise=False, pos="left", can_choise = True)

window.addObject(button)
window.addObject(label)
window.addObject(label1)

while True:
    window.Manipulate()
