import os
os.system('cls'if os.name == 'nt' else 'clear')
import turtle
#استدعينا المكتبه وبعد كدا كتبنا الخلفيه اللي هيا اسمهاwind
wind = turtle.Screen()
wind.title("ping bong")
wind.bgcolor("black")
wind.setup(height=600,width=800)
wind.tracer(0)

#!عملنا المضرب الاول
madrab1=turtle.Turtle()
madrab1.speed(0)
madrab1.shape("square")
madrab1.color("white")
madrab1.shapesize(stretch_wid=5, stretch_len=1)
madrab1.penup()
madrab1.goto(-350,0)
#!عملنا المضرب الثاني
madrab2=turtle.Turtle()
madrab2.speed(0)
madrab2.shape("square")
madrab2.color("red")
madrab2.shapesize(stretch_wid=5, stretch_len=1)
madrab2.penup()
madrab2.goto(350,0)
#!عملنا الكره
ball=turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("yellow")
ball.penup()
ball.goto(0,0)
#!علشان الكوره تتحرك
#!2.5 سرعه الكره
ball.dx  = .1
ball.dy = .1

#!علشان اعمل نتيجه للمباره
score1 = 0
score2 = 0
score = turtle.Turtle()
score.speed(0)
score.color("blue")
#!علشان ميظهرش خطوط علي الشاشه
score.penup()
score.hideturtle()
score.goto(0,260)
score.write("player1 : 0 player2 : 0",align = "center", font = ("courier",24,"normal"))


 #!  علشان اخلي المضرب يطلع فوق المضرب الاول
def madrab1_up():
    y=madrab1.ycor()
    y +=20
    madrab1.sety(y)
#!علشان اخلي المضرب ينزل تحت المضرب الاول
def madrab1_dwen():
    y=madrab1.ycor()
    y -=20
    madrab1.sety(y)

def madrab2_up():
    y=madrab2.ycor()
    y +=20
    madrab2.sety(y)

def madrab2_dwen():
    y=madrab2.ycor()
    y -=20
    madrab2.sety(y)


#!ربط الكيبورد بالحركه
wind.listen()
#!علشان اربط الكيبورد ب حرف w
wind.onkeypress(madrab1_up,"w")
#!علشان اربط الكيبورد بحرف s
wind.onkeypress(madrab1_dwen,"s")
#!علشان اربط المضرب التاني بالكيبورد
wind.onkeypress(madrab2_up,"Up")

wind.onkeypress(madrab2_dwen,"Down")

while True:
    wind.update()
#! اكواد علشان الانعكاس وكدا
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

#!اكواد الانعكاس  علشان لو الكوره طلعت فوق تتعكس وتنزل تحت
    
    if ball.ycor() >290  :
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() <-290  :
        ball.sety(-290)
        ball.dy *= -1

    #!لو هخلي الكوره خرجت ترجع تاني في النص
    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        #!الكود اللي تحت علشان لو الكره خرجت تتحسب للعيب الاول  
        score1+= 1
        score.clear()
        score.write("player1 : {} player2 : {}".format (score1 , score2),align = "center", font = ("courier",24,"normal"))

    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1 
        #!علشان لو الكره خرجت تتحسب للعيب الثاني
        score2 += 1 
        score.clear()
        score.write("player1 : {} player2 : {}".format (score1 , score2),align = "center", font = ("courier",24,"normal"))
#! علشان اخلي الكوره لو جات في المضرب تتعكس
       
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < madrab2.ycor() + 40 and ball.ycor() > madrab2.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < madrab1.ycor() + 40 and ball.ycor() > madrab1.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
        
    