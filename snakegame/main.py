import turtle
from turtle import Screen
import time

from scoreboard import scoreboard
from snake import Snake
from Food import Food
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake Game")
screen.tracer(0)
snake = Snake()
food = Food()
scoreboard = scoreboard()



# segment_1 =turtle.Turtle(shape ="square")
# segment_1.color("white")
# segment_2 = turtle.Turtle(shape ="square")
# segment_2.color("white")
# segment_2.goto(-20,0)
# segment_3 = turtle.Turtle(shape ="square")
# segment_3.color("white")
# segment_3.goto(-40,0)
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
    if snake.head.xcor() >280 or snake.head.xcor() <-280 or snake.head.ycor() >280 or snake.head.ycor() <-280:
        game_is_on = False
        scoreboard.game_over()
    for seg in snake.segment:
        if seg == snake.head:
            pass
        elif snake.head.distance(seg) < 10:
            scoreboard.game_over()
            game_is_on = False




screen.exitonclick()