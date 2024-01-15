from turtle import Turtle

class Button(Turtle):

    def __init__(self, xCor, yCor, text):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(xCor, yCor)
        # self.pendown()
        self.begin_fill()
        self.setheading(0)
        self.forward(100)
        self.setheading(90)
        self.forward(50)
        self.setheading(180)
        self.forward(100)
        self.setheading(270)
        self.forward(50)
        self.end_fill()
        self.goto(xCor+55, yCor+10)
        self.color("white")
        self.write(text, align="center", font=("Arial", 24, "bold"))
        
        
