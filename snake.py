# Sanke Class:
# Method :Creat snake()
# Method :Move snake()


from turtle import Turtle




class Snake:
    def __init__(self):
        self.turtles=[]
        self.positions = [(-40,0),(-20,0),(0,0)]
        self.Creat_Snake()
        self.head = self.turtles[-1]
        
        
    def Creat_Snake(self):
        for i in range(len(self.positions)):
            new_turtle = Turtle("square")
            new_turtle.color("white")
            new_turtle.penup()
            new_turtle.goto(self.positions[i])
            self.turtles.append(new_turtle)
        
    def Move_Snake(self):
        for i in range(len(self.turtles)-1):
            self.turtles[i].goto(self.turtles[i+1].pos())
        self.head.forward(20)
        
    def up(self):
        self.head.setheading(90)
    def down(self):
        self.head.setheading(270)
    def right(self):
        self.head.setheading(0)
    def left(self):
        self.head.setheading(180)

    def extend(slef):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(slef.turtles[0].pos())
        slef.turtles.insert(0,new_segment)
        
    def change_place_y(self):
        y= self.head.ycor()
        x= self.head.xcor()
        y*=-1
        self.head.goto(x,y)
        
    def change_place_x(self):   
        y= self.head.ycor()
        x= self.head.xcor()
        x*=-1
        self.head.goto(x,y) 
    