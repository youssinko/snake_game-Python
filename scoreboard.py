from turtle import Turtle
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.current_score = 0
        self.color('white')
        self.penup()
        self.goto(0, 270)
        self.write(f" Your Score: {self.current_score}", align='center', font=('Arial', 24, 'normal'))
        self.hideturtle()
    def increase_score(self):
        self.clear()
        self.current_score += 1
        self.write(f" Your Score: {self.current_score}", align='center', font=('Arial', 24, 'normal'))
    def game_over_msg(self):
        self.clear()
        self.goto(0, 0)
        self.color("red")
        self.write(f" Game Over", align='center', font=('Arial', 30, 'normal'))

