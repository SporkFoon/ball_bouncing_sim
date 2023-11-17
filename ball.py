import turtle
import random

class Ball:
    def __init__(self, canvas_width, canvas_height, ball_radius):
        self.xpos = random.randint(-1 * canvas_width + ball_radius, canvas_width - ball_radius)
        self.ypos = random.randint(-1 * canvas_height + ball_radius, canvas_height - ball_radius)
        self.vx = random.randint(1, int(0.01 * canvas_width))
        self.vy = random.randint(1, int(0.01 * canvas_height))
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.radius = ball_radius

    def draw(self):
        turtle.penup()
        turtle.color(self.color)
        turtle.fillcolor(self.color)
        turtle.goto(self.xpos, self.ypos)
        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(self.radius)
        turtle.end_fill()

    def move(self, canvas_width, canvas_height):
        self.xpos += self.vx
        self.ypos += self.vy

        if abs(self.xpos + self.vx) > (canvas_width - self.radius):
            self.vx = -self.vx

        if abs(self.ypos + self.vy) > (canvas_height - self.radius):
            self.vy = -self.vy

def initialize_balls(num_balls, canvas_width, canvas_height, ball_radius):
    balls = []
    for _ in range(num_balls):
        ball = Ball(canvas_width, canvas_height, ball_radius)
        balls.append(ball)
    return balls