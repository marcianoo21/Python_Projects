from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    
    def __init__(self):
        super().__init__()
        self.color("black")
        self.setheading(90)
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POSITION)


    def go_up(self):
        new_y =  self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)


    def crossed_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False
            
    def start_position(self):
        self.goto(STARTING_POSITION)

