from turtle import Turtle
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.current_score = 0
        self.highest_score = 0
        self.color('white')
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update()

    def update(self):
        self.clear()
        self.write(f" Your Score: {self.current_score} Highest :{self.highest_score}", align='center', font=('FONT'))

    def increase_score(self):
        self.current_score += 1
        self.update()
    # def game_over_msg(self):
    #     self.clear()
    #     self.goto(0, 0)
    #     self.color("red")
    #     self.write(f" Game Over", align='center', font=('Arial', 30, 'normal'))
    def highest(self):
        if self.current_score > self.highest_score:
            self.highest_score = self.current_score
            self.current_score = 0
            self.update()


