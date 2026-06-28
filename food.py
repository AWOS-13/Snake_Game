from turtle import Turtle
import random
class Food(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("red")
        self.penup()
        self.shapesize(0.6,0.6)
        self.appear()
    
    def appear(self):
        random_x=random.randint(-350,350)
        random_y=random.randint(-250,250)
        self.goto(random_x,random_y)
        
    