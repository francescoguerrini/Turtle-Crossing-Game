from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
level = 1

class Player (Turtle):
    def __init__(self):
        super().__init__()
        self.color = ("black")
        self.shape("turtle")
        self.setheading(90)
        self.penup()
        self.go_to_start()

    def move(self):
        self.forward(MOVE_DISTANCE)

    def level_up(self):
        if self.ycor() > FINISH_LINE_Y:
            self.clear()
            level += 1


    def go_to_start(self):
        self.goto(STARTING_POSITION)

    def finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False

