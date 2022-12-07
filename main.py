import spytui
import objects

window = spytui.Window()

label1 = objects.Label()
label1.set(text="Hello", pos="center", neighbors=0, view="single", is_choise=False)

label2 = objects.Label()
label2.set(text="Привет", pos="center", neighbors=0, view="double", is_choise=True)

label3 = objects.Label()
label3.set(text="Охайо", pos="center", neighbors=0, view="simple", is_choise=False)

window.addObject(label1)
window.addObject(label2)
window.addObject(label3)

screen = window.render()
window.print(screen)
