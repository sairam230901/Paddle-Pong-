import turtle
import winsound

wn = turtle.Screen()
wn.title("Welcome to Pong Game")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)                  # Basically stops the window from updating as we want manually, the game loop to update,
                              # also it speeds up the game a bit

#Score
score_a = 0
score_b = 0
#Paddle a
paddle_a = turtle.Turtle()    # from turtle module we create a Turtle class
paddle_a.speed(0)             # this is the speed of animation(not paddle's speed), this sets to the max speed
paddle_a.shape("square")      # paddle shape
paddle_a.shapesize(stretch_wid=5, stretch_len=1)       # by default it is 20 by 20 pixels, now wid gets stretched by 5.
paddle_a.color("orange")       # paddle colour is set
paddle_a.penup()              # Turtle by default draws line as it moves, in order to avoid it we use this penup command
paddle_a.goto(-350,0)

#Paddle b
paddle_b = turtle.Turtle()    # from turtle module we create a Turtle class
paddle_b.speed(0)             # this is the speed of animation(not paddle's speed), this sets to the max speed
paddle_b.shape("square")      # paddle shape
paddle_b.shapesize(stretch_wid=5, stretch_len=1)       # by default it is 20 by 20 pixels, now wid gets stretched by 5.
paddle_b.color("yellow")       # paddle colour is set
paddle_b.penup()              # Turtle by default draws line as it moves, in order to avoid it we use this penup command
paddle_b.goto(350,0)

#Ball

ball = turtle.Turtle()    # from turtle module we create a Turtle class
ball.speed(0)             # this is the speed of animation(not ball's speed), this sets to the max speed
ball.shape("circle")      # ball shape
    # by default it is 20 by 20 pixels, now wid gets stretched by 5.
ball.color("red")       # ball colour is set
ball.penup()            # Turtle by default draws line as it moves, in order to avoid it we use this penup command
ball.goto(0,0)
ball.dx = 0.25           # what these dx and dy do is that we control the ball motion independently in x and y axes
ball.dy = 0.25           # the no 2 is the amount of pixels that we move in each itr

#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align= "center", font= ("Courier",20, "normal"))
#Funtion for paddle

def paddle_a_up():
    y = paddle_a.ycor()  #finds the current y coordinate of the paddle
    if y!=220:
       y+=20
       paddle_a.sety(y)  #sets the current y cor to the updated value

def paddle_a_down():
    y = paddle_a.ycor()  #finds the current y coordinate of the paddle
    if y!=-220:
       y-=20
       paddle_a.sety(y)  #sets the current y cor to the updated value

def paddle_b_up():
    y = paddle_b.ycor()  #finds the current y coordinate of the paddle
    if y!=220:
       y+=20
       paddle_b.sety(y)  #sets the current y cor to the updated value

def paddle_b_down():
    y = paddle_b.ycor()  #finds the current y coordinate of the paddle
    if y!=-220:
       y-=20
       paddle_b.sety(y)  #sets the current y cor to the updated value

#Keyboard Binding
wn.listen()
wn.onkeypress(paddle_a_up,"w")
wn.onkeypress(paddle_a_down,"s")
wn.onkeypress(paddle_b_up,"Up")
wn.onkeypress(paddle_b_down,"Down")


# Main Game Loop
while True:
    wn.update()

    #For moving the ball

    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)

    #border check for ball
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("387186__alexiero-1__ai-snare-20.wav",winsound.SND_ASYNC)


    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("387186__alexiero-1__ai-snare-20.wav", winsound.SND_ASYNC)

    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx*=-1
        score_a+=1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a,score_b), align="center", font=("Courier", 20, "normal"))

    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx*=-1
        score_b+=1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a,score_b), align="center", font=("Courier", 20, "normal"))


    #Paddle and ball Collision

    if ball.xcor() >330 and ball.xcor() <340 and (ball.ycor() < paddle_b.ycor()+40 and ball.ycor() > paddle_b.ycor()-40):
        ball.setx(330)
        ball.dx *= -1
        winsound.PlaySound("387186__alexiero-1__ai-snare-20.wav", winsound.SND_ASYNC)

    if ball.xcor() <-330 and ball.xcor() >-340 and (ball.ycor() < paddle_a.ycor()+40 and ball.ycor() > paddle_a.ycor()-40):
        ball.setx(-330)
        ball.dx *= -1
        winsound.PlaySound("387186__alexiero-1__ai-snare-20.wav", winsound.SND_ASYNC)