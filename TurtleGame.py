import turtle
import random as rand
import math
import time

wn = turtle.Screen()
wn.bgcolor("white")

#setting borders
border = turtle.Turtle()
border.penup()
border.setposition(-350,-350)
border.pendown()
border.hideturtle()
border.pensize(3)
border.speed(800)
for side in range(4):
    border.forward(700)
    border.left(90)
border.hideturtle()

#setting lines
line1 = turtle.Turtle()
line1.penup()
line1.speed(800)
line1.setposition(-350,-300)
line1.pendown()
line1.hideturtle()
line1.pensize(3)
line1.forward(700)
line1.left(90)
line1.forward(600)
line1.left(90)
line1.forward(700)




#setting players
player1 = turtle.Turtle()
player1.left(90)
player1.penup()
player1.setposition(0,-330)
player1.color("blue")
player1.shape("turtle")

player2 = turtle.Turtle()
player2.right(90)
player2.penup()
player2.setposition(0,330)
player2.color("red")
player2.shape("turtle")
dusmanlar = []

p_speed = 20
x = 0
ctr = 0

rightC = False
leftC = False
rightC2 = False
leftC2 = False

#defining functions
def rightP():
    global rightC
    rightC = True
    
def rightR():
    global rightC
    rightC = False
    
def leftP():
    global leftC
    leftC = True

def leftR():
    global leftC
    leftC = False
    
def p1Fire():
    pass

#defining functions
def rightP2():
    global rightC2
    rightC2 = True
    
def rightR2():
    global rightC2
    rightC2 = False
    
def leftP2():
    global leftC2
    leftC2 = True

def leftR2():
    global leftC2
    leftC2 = False
    
p2bullet = turtle.Turtle()
p2bullet.hideturtle()
p2bullet.speed(0)
p2bullet.shape("circle")
p2bullet.color("black")
p2bullet.left(90)
p2bullet.penup()
def p2Fire():
    global p2bullet
    if(p2bullet.ycor() > -330):
        return
    p2bullet.setx(player2.xcor())
    p2bullet.sety(player2.ycor())
    p2bullet.showturtle()
    
p1bullet = turtle.Turtle()
p1bullet.hideturtle()
p1bullet.speed(0)
p1bullet.shape("circle")
p1bullet.color("black")
p1bullet.left(90)
p1bullet.penup()
def p1Fire():
    global p1bullet
    if(p1bullet.ycor() < 330):
        return
    p1bullet.setx(player1.xcor())
    p1bullet.sety(player1.ycor())
    p1bullet.showturtle()
    

    
    
def tekrar():
    print(leftC)  
    if (leftC):
        player1.setx(player1.xcor() - p_speed)
    if (rightC):
        player1.setx(player1.xcor() + p_speed)
    if (leftC2):
        player2.setx(player2.xcor() - p_speed)
    if (rightC2):
        player2.setx(player2.xcor() + p_speed)
        
    if(p1bullet.ycor() < 330):
        p1bullet.sety(p1bullet.ycor() + 40)
    else:
        if(p1bullet.xcor()-player2.xcor() < 20 and p1bullet.xcor()-player2.xcor() > -20 and p1bullet.isvisible()):
            #p2 mermi yedi
            border.clear()
            line1.clear()
            player1.ht()
            player2.ht()
            p1bullet.ht()
            p2bullet.ht()
            turtle.color("blue")
            turtle.write("GAME OVER BLUE TURTLE WON",align= "center", font=("Arial", 26, "normal"))
            time.sleep(3)
            turtle.bye()
        else:
            p1bullet.ht()
            
    if(p2bullet.ycor() > -330):
        p2bullet.sety(p2bullet.ycor() - 40)
    else:
        if(p2bullet.xcor()-player1.xcor() < 20 and p2bullet.xcor()-player1.xcor() > -20 and p2bullet.isvisible()):
            #p1 mermi yedi
            border.clear()
            line1.clear()
            player1.ht()
            player2.ht()
            p1bullet.ht()
            p2bullet.ht()
            turtle.color("red")
            turtle.write("GAME OVER RED TURTLE WON",align= "center", font=("Arial", 26, "normal"))
            time.sleep(3)
            turtle.bye()
        else:
            p2bullet.ht()

    
    
    
    
    turtle.ontimer(tekrar,1)
    
tekrar()

    
wn.listen()
wn.onkeypress(rightP, "Right")
wn.onkeypress(leftP, "Left")
wn.onkeyrelease(rightR, "Right")
wn.onkeyrelease(leftR, "Left")
wn.onkeypress(rightP2, "d")
wn.onkeypress(leftP2, "a")
wn.onkeyrelease(rightR2, "d")
wn.onkeyrelease(leftR2, "a")
wn.onkeypress(p1Fire, "Up")
wn.onkeypress(p2Fire, "w")