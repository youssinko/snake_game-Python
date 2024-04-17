from turtle import Turtle
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
STEPS = 20
class Snake:

    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)
    def add_segment(self,position):
        segment = Turtle("square")
        segment.color("white")
        segment.penup()
        segment.setposition(position)
        self.snake.append(segment)
    def growing(self):
        self.add_segment(self.snake[-1].position())

    def move(self):
        """getting the length of the snake array ,start from backwards, change coordinates where the
        last item will replace the item before it"""
        for x in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[x - 1].xcor()
            new_y = self.snake[x - 1].ycor()
            self.snake[x].goto(new_x, new_y)
        self.snake[0].forward(STEPS)

    def move2(self):
        self.snake[0].setheading(90)

    def move3(self):
        self.snake[0].setheading(270)

    def move4(self):
        self.snake[0].setheading(180)

    def move5(self):
        self.snake[0].setheading(0)
    def reset(self):
        for seg in self.snake:
            seg.goto(1000,1000)
        self.snake.clear()
        self.create_snake()
        self.head = self.snake[0]
