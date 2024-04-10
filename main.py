from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from scoreboard import Score
screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.move2, "Up")
screen.onkey(snake.move3, "Down")
screen.onkey(snake.move4, "Left")
screen.onkey(snake.move5, "Right")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        score.increase_score()
        snake.growing()

    elif snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.game_over_msg()
        game_on = False
    elif snake.head.distance(snake.snake[-1]) < 15:
        score.game_over_msg()
        game_on = False
    for x in snake.snake:
        if x == snake.head:
            pass
        elif snake.head.distance(x) < 10:

            score.game_over_msg()
            game_on = False




# def food():
#     food = Turtle()
#     food.shape("circle")
#     food.color('red')
#     food.penup()
#     food.setposition(random.randint(-300, 300), random.randint(-300, 300))
#     saved_food.append(food)
#     return saved_food
# food()

#
# if abs(saved_food[0].xcor()) == abs(snake[0].xcor()) and abs(food.ycor()) == abs(snake[0].ycor()):
#     print("you won!")
#     position(snake[-1].xcor()-20, snake[-1].ycor()-20)







screen.exitonclick()

