import turtle
import ball

class BallSimulation:
    def __init__(self, num_balls):
        turtle.speed(0)
        turtle.tracer(0)
        turtle.hideturtle()
        self.canvas_width = turtle.screensize()[0]
        self.canvas_height = turtle.screensize()[1]
        self.ball_radius = 0.05 * self.canvas_width
        turtle.colormode(255)
        self.balls = self.initialize_balls(num_balls)

    def initialize_balls(self, num_balls):
        balls = []
        for _ in range(num_balls):
            ball_obj = ball.Ball(self.canvas_width, self.canvas_height, self.ball_radius)
            balls.append(ball_obj)
        return balls

    def run_simulation(self):
        while True:
            turtle.clear()
            for ball_obj in self.balls:
                ball_obj.draw()
                ball_obj.move(self.canvas_width, self.canvas_height)
            turtle.update()


num_balls = int(input("Number of balls to simulate: "))
simulation = BallSimulation(num_balls)
simulation.run_simulation()

# Hold the window; close it by clicking the window close 'x' mark
turtle.done()
