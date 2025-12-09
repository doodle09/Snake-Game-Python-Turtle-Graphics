from turtle import Turtle
ALIGNMENT="center"
FONT= ("Arial",24,"normal")
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score=0
        file_path="C:/python/turtle.wala.py/snake.game.py/data.txt"
        with open(file_path) as data:
            self.high_score=int(data.read())
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score : {self.score} high score: {self.high_score}",align=ALIGNMENT,font=FONT)

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(f"Game Over : {self.score}",align=ALIGNMENT,font=FONT)

    def reset(self):
        if self.score>self.high_score:
            self.high_score=self.score
            file_path="C:/python/turtle.wala.py/snake.game.py/data.txt"
            with open(file_path,"w") as data:
                data.write(f"{self.high_score}")

        self.score=0
        self.update_scoreboard()    

            
       
    def increase_score(self):
        self.score+=1
        self.update_scoreboard()



