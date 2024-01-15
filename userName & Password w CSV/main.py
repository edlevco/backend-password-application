import turtle
from button import Button
from design import Design


turtle.colormode(255)


screen = turtle.Screen()
screen.setup( width=500, height=500)
screen.bgcolor((59,255,111))
design = Design()

sign_up = Button(-120, -10, "sign up")
sign_in = Button(20, -10, "sign in")


signing_in = True
# while signing_in:
#     pass
    


screen.exitonclick()

