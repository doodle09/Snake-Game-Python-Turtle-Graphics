from turtle import  Screen
from snake_move import Snake
from food import Food
from scoreboard import Scoreboard
import time

# screen set up
screen=Screen()
# snake body will not show peice by peice but entire body at once after tracer, and will only show the result after using update.
screen.tracer(0)
screen.setup(width= 600, height= 600)
screen.bgcolor("black")
screen.title("my snake game ")

snake= Snake()
food=Food()
scoreboard=Scoreboard()

screen.listen()
screen.onkey(snake.up,"w")
screen.onkey(snake.down,"s")
screen.onkey(snake.left,"a")
screen.onkey(snake.right,"d")

game_is_on= True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    #detect collision with food
    if snake.head.distance(food)<15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    #detect collision with wall
    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.ycor()<-280:
        scoreboard.reset()
        snake.reset()


    #detect collision with tail
    for segment in snake.segments:
        if segment==snake.head:
            pass
        elif snake.head.distance(segment)<10:
            scoreboard.reset()
            snake.reset()
        

screen.exitonclick()