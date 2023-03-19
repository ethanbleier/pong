# Simple python pong
# By Ethan

import turtle

wn = turtle.Screen()
wn.title("Pong by Ethan Bleier")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Score
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("blue")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("red")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed()
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 5
ball.dy = 5

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("0 | 0", align="center", font=("Cambria", 30, "bold"))

# Functions
def paddle_a_up():
    if (paddle_a.ycor() < 250):
        y = paddle_a.ycor()
        y += 50
        paddle_a.sety(y)
    else:
        y=paddle_a.ycor()
        y+=0
        paddle_a.sety(y) 

        
def paddle_a_down():
    if (paddle_a.ycor() > -250):
        y = paddle_a.ycor()
        y -= 50
        paddle_a.sety(y)
    else:
        y=paddle_a.ycor()
        y+=0
        paddle_a.sety(y) 

def paddle_b_up():
    if (paddle_b.ycor() < 250):
        y = paddle_b.ycor()
        y += 50
        paddle_b.sety(y) 
    else:
        y = paddle_b.ycor()
        y+=0
        paddle_b.sety(y)
    
def paddle_b_down():
    if (paddle_b.ycor() > -250):
        y = paddle_b.ycor()
        y -= 50
        paddle_b.sety(y)
    else:
        y = paddle_b.ycor()
        y+=0
        paddle_b.sety(y) 


# Keybinds
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "[")
wn.onkeypress(paddle_b_down, "'")
wn.onkeypress(wn.bye, "Escape")

# Game loop
while True:
    wn.update()
    
    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Top and bottom
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    elif ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    # Left and right
    if ball.xcor() > 350:
        score_a += 1
        pen.clear()
        pen.write("{} | {}".format(score_a, score_b), align="center", font=("Cambria", 30, "bold"))
        ball.goto(0, 0)
        ball.dx *= -1

    elif ball.xcor() < -350:
        score_b += 1
        pen.clear()
        pen.write("{} | {}".format(score_a, score_b), align="center", font=("Cambria", 30, "bold"))
        ball.goto(0, 0)
        ball.dx *= -1

    # Paddle and ball collisions
    if ball.xcor() < -340 and paddle_a.ycor() + 50 > ball.ycor() > paddle_a.ycor() - 50:
        ball.dx *= -1

    elif ball.xcor() > 340 and paddle_b.ycor() + 50 > ball.ycor() > paddle_b.ycor() - 50:
        ball.dx *= -1
