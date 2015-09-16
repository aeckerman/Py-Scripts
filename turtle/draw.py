import turtle

win = turtle.Screen()
win.bgcolor("#fff")

char = turtle.Turtle()
char.color("#3498db")
char.shape("turtle")

for i in range(1,5):
	char.forward(100)
	char.right(90)

print ("Drawn!")

