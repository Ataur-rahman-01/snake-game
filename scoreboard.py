from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        with open("data.txt", mode="r") as snake_score:
            self.high_score = int(snake_score.read())
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align='center', font=('Arial', 20, 'normal'))

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align='center', font=('Arial', 25, 'normal'))
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as snake_score:
                snake_score.write(f"{self.high_score}")
        self.score = 0
        self.update_score()

    def increase(self):
        self.score += 1
        self.update_score()
