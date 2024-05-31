from turtle import Turtle
FONT = ("Comic Sans MS", 18, "normal")


class Scoreboard(Turtle):
   
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-235, 240)
        self.upadte_score()
    
    def upadte_score(self):
        self.clear()
        self.write(f"Level: {self.level}", align="center", font=FONT)

    
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Comic Sans MS", 38, "normal"))
        self.goto(0, -40)
        self.write(f"Your final score: {self.level}", align="center", font=("Magneto", 18, "normal"))


    def increase_lvl(self):
        self.level += 1      
        self.upadte_score()

