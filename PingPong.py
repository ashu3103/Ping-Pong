import turtle
ash = turtle.Screen()
ash.bgcolor("black")
ash.title("PingPong by @Ashu")
ash.setup(width=800, height=600)
ash.tracer(1)
#Block-1
block1 = turtle.Turtle()
block1.speed(0)
block1.shape("square")
block1.color("white")
block1.shapesize(stretch_wid=5, stretch_len=1)
block1.penup()
block1.goto(-350, 0)
#Block-2
block2 = turtle.Turtle()
block2.speed(0)
block2.shape("square")
block2.color("white")
block2.shapesize(stretch_wid=5, stretch_len=1)
block2.penup()
block2.goto(350, 0)
#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 5
ball.dy = 5
#Pen
pen = turtle.Turtle()
pen.color("white")
pen.speed(0)
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A:0 Player B:0", align="center", font=("Courier",24))
#Score
score_a = 0
score_b = 0
def block1_up():
	y = block1.ycor()
	y = y+20
	block1.sety(y)
def block1_down():
	y = block1.ycor()
	y = y-20
	block1.sety(y)
def block2_up():
	y = block2.ycor()
	y = y+20
	block2.sety(y)
def block2_down():
	y = block2.ycor()
	y = y-20
	block2.sety(y)
ash.listen()
ash.onkeypress(block1_up,"w")
ash.onkeypress(block1_down,"s")
ash.onkeypress(block2_up,"Up")
ash.onkeypress(block2_down,"Down")
while True:
	ash.update()
	ball.setx(ball.xcor() + ball.dx)
	ball.sety(ball.ycor() + ball.dy)
	if ball.ycor()>290:
		ball.sety(290)
		ball.dy *= -1
	if ball.ycor()<-290:
		ball.sety(-290)
		ball.dy *= -1
	if ball.xcor()>390:
		ball.goto(0,0)
		ball.dx *= -1
		score_a = score_a + 1
		pen.clear()
		pen.write("Player A:{} Player B:{}".format(score_a,score_b), align="center", font=("Courier",24))
	if ball.xcor()<-390:
		ball.goto(0,0)
		ball.dx *= -1
		score_b = score_b + 1
		pen.clear()
		pen.write("Player A:{} Player B:{}".format(score_a,score_b), align="center", font=("Courier",24))
	if (ball.xcor()>340 and ball.xcor()<350) and (ball.ycor()<(block2.ycor()+50) and ball.ycor()>(block2.ycor()-50)):
		ball.dx *= -1
	if (ball.xcor()<-340 and ball.xcor()>-350) and (ball.ycor()<(block1.ycor()+50) and ball.ycor()>(block1.ycor()-50)):
		ball.dx *= -1