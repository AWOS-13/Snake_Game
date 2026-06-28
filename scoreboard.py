from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.highscore =self.get_highscore()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0,290)
        self.update_score()
        
    def update_score(self):
        self.write(f"Score : {self.score}       High score : {self.highscore}",align="center",font=("arial",24,"normal"))

    def increase_score(self):
        self.score+=2
        self.clear()

        self.update_score()


    def get_highscore(self):
        with open("C:/Users/awwso/Desktop/Projects/python/GUI/Snake Game/highscore.txt") as file:
            return int(file.read())
            

    def save_highscore(self):
        with open("C:/Users/awwso/Desktop/Projects/python/GUI/Snake Game/highscore.txt","w") as file:
            file.write(str(self.highscore))



    def game_over(self):
        self.clear()
        self.screen.bgcolor("red")
        self.goto(0,0)        
        if self.score> self.highscore :
            self.highscore= self.score
            self.save_highscore()

        self.write(f"---------Game Over -------- \n\nFinal Score: {self.score}\n\nHigh Score: {self.highscore}",align="center",font={"Arial",28,"normal"})









# class Scoreboard(Turtle):
#     def __init__(self):
#         super().__init__()
#         self.score =0
#         self.color("white")
#         self.penup()
#         self.goto(0,350)
#         self.hideturtle()
#         self.update_scoreboard()
        
#     def update_scoreboard(self):
#         self.write(f"Score: {self.score}",align="center",font={"Arial",24,"normal"})
    
#     def increase_score(self):
#         self.score+=2
#         self.clear()
#         self.update_scoreboard()
        
#     def game_over(self):
#         self.screen.bgcolor("darkred")
#         self.goto(0,0)
#         self.write(f"Game over \nFinal Score: {self.score}",align="center",font={"Arial",28,"normal"})
        