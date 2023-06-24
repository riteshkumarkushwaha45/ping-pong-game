from turtle import *
ALIGNMENT="center"
FONT=("Courier",50,"normal")

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0,230)
        self.score_l=0
        self.score_r=0
        self.updatescr()
        

    def updatescr(self):
        self.write(f"{self.score_l} : {self.score_r}",align=ALIGNMENT,font=FONT)

    def inc_score_l(self):
        self.clear()
        self.score_l+=1
        self.updatescr()

    def inc_score_r(self):
        self.clear()
        self.score_r+=1
        self.updatescr()
    

