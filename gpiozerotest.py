from gpiozero import Button
from signal import pause

button1 = Button(17)
button2 = Button(27)

def say_one():
	print("one")
	
def say_two():
	print("two")

button1.when_pressed = say_one
button2.when_pressed = say_two

pause()	
