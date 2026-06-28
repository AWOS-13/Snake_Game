# Game window
# Loop
import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score


window = Screen ()
window.setup(800,650)
window.bgcolor("black")
window.title("Sanke Game")
window.tracer(0)

snake =Snake()
food = Food()
score = Score()

game = True
while game:
    window.update()
    time.sleep(0.1)
    snake.Move_Snake()
    window.listen()
    window.onkey(snake.up,"Up")
    window.onkey(snake.down,"Down")
    window.onkey(snake.right,"Right")
    window.onkey(snake.left,"Left")
    
    if snake.head.distance(food)<17:
        food.appear()
        snake.extend()
        score.increase_score()
        
    if snake.head.ycor()>=300 or snake.head.ycor()<=-290:
        snake.change_place_y()
    if snake.head.xcor()>= 400 or snake.head.xcor()<= -400:
        snake.change_place_x() 
        
    for i in snake.turtles[:-1]:
        if snake.head.distance(i)<10:
            score.game_over()
            game=False
            
            

# snake = Snake()
# food = Food()
# score = Scoreboard()


# while True:
#     snake.Move_Snake()
#     window.update()
#     time.sleep(0.1)
#     window.listen()
#     window.onkey(snake.up,"Up")
#     window.onkey(snake.down,"Down")
#     window.onkey(snake.right,"Right")
#     window.onkey(snake.left,"Left")
#     if snake.head.distance(food)<15:
#         food.appear()
#         snake.extend()
#         score.increase_score()
    
#     if snake.head.xcor() >370 or snake.head.xcor() <-370 or snake.head.ycor() >370 or snake.head.ycor()<-370:
#         score.game_over()
#         break
        
#     for i in snake.turtles[:-1]:
#         if snake.head.distance(i)<10:
#             score.game_over()
#             break
   


window.exitonclick()