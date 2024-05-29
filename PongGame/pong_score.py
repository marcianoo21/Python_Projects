from turtle  import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.r_score = 0
        self.l_score = 0
        self.caption = "Thanks for the game!"
        self.update_score()

    def update_score(self):
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Arial", 40, "normal"))
        self.goto(0, 200)
        self.write(":", align="center", font=("Arial", 40, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Arial", 40, "normal"))

    def l_point(self):
        self.l_score += 1
        self.clear()
        self.update_score()

    def r_point(self):
        self.r_score += 1
        self.clear()
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(self.caption, align="center", font=("Arial", 60, "normal"))

    def winner(self):
        self.goto(0, -100)
        if self.l_score == 9: 
            self.write("Left player wins!", align="center", font=("Arial", 30, "normal"))
        else:
            self.write("Right player wins!", align="center", font=("Arial", 30, "normal"))