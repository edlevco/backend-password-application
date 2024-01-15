from turtle import Turtle

positions = [-260, -260]


class Design(Turtle):

    def __init__(self):
        super().__init__()
        self.speed("fastest")
        self.penup()
        for i in range(0, 50):
            self.goto(positions[0], positions[1])
            self.pendown()
            self.goto(positions[0]+500, positions[1])
            self.goto(positions[0]+500, positions[1]+10)
            positions[1] += 10
            self.goto(positions[0], positions[1])

        self.penup
        positions[1] = -260
        positions[0] = -260
        for i in range(0, 50):
            self.goto(positions[0], positions[1])
            self.pendown()
            self.goto(positions[0], positions[1]+520)
            self.goto(positions[0]+10, positions[1]+520)
            positions[0] += 10
            self.goto(positions[0], positions[1])
            
