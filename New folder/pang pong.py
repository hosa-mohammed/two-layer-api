import turtle
wind = turtle.Screen()
wind.title("ping pong")
wind.bgcolor('pink')
wind.setup(width=800, height=600)
wind.tracer(0)

stik1 = turtle.Turtle()
stik1.speed(0)
stik1.shape("square")
stik1.color("red")
stik1.shapesize(stretch_wid=5, stretch_len=0.5)
stik1.penup()
stik1.goto(-350,0)

stik2 = turtle.Turtle()
stik2.speed(0)
stik2.shape("square")
stik2.color("green")
stik2.shapesize(stretch_wid=5, stretch_len=0.5)
stik2.penup()
stik2.goto(350,0)

ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("blue")
ball.penup()
ball.goto(0,0)
ball.dx = 0.08
ball.dy =  - 0.08

score = turtle.Turtle()
score.speed(0)
score.color('white')
score.penup()
score.hideturtle()
score.goto(0,260)
score.write("player red:0 --- player green:0", align="center", font=("courier",24,"normal"))
score1 = 0
score2 = 0
def stik1_up():
    y=stik1.ycor()
    y  += 20
    stik1.sety(y)

def stik2_up():
    y=stik2.ycor()
    y  += 20
    stik2.sety(y)

def stik1_down():
    y=stik1.ycor()
    y  -= 20
    stik1.sety(y)

def stik2_down():
    y=stik2.ycor()
    y  -= 20
    stik2.sety(y)

wind.listen()
wind.onkeypress(stik2_down, 2)
wind.onkeypress(stik1_down, "s")
wind.onkeypress(stik2_up, 8)
wind.onkeypress(stik1_up, "w")


while True:
    wind.update()

    ball.setx(ball.xcor()+ ball.dx)
    ball.sety(ball.ycor()+ ball.dy)

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    
    if ball.ycor() <-290:
        ball.sety(-290)
        ball.dy *=-1

    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *=-1
        score1 +=1
        score.clear()
        score.write("player red:{} --- player green:{}".format(score1, score2), align="center", font=("courier",24,"normal"))

    if ball.xcor()  <- 390:
        ball.goto(0,0)
        ball.dx *=-1
        score2 +=1
        score.clear()
        score.write("player red:{} --- player green:{}".format(score1, score2), align="center", font=("courier",24,"normal"))

    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor()< stik2.ycor() +50 and ball.ycor() > stik2.ycor() - 50 ):
        ball.setx(340)
        ball.dx *= -1 

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor()< stik1.ycor() +50 and ball.ycor() > stik1.ycor() - 50 ):
        ball.setx(-340)
        ball.dx *= -1  


