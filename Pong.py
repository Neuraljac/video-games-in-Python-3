# -*- coding: utf-8 -*-
"""
This is a basic Pong game tutorial made in christmas colors. 
Written by Neuraljac (adapted from @TokyoEdTech)
"""

# Part 1: Getting Started

import turtle

wn = turtle.Screen()
wn.title("Pong by @TokyoEdTech")
wn.bgcolor("green")
wn.setup(width = 800, height = 600)
wn.tracer(0)

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("yellow")
paddle_a.shapesize(stretch_wid=(5), stretch_len=(1))
paddle_a.penup()
paddle_a.goto(-350, 0)


# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("yellow")
paddle_b.shapesize(stretch_wid=(5), stretch_len=(1))
paddle_b.penup()
paddle_b.goto(350, 0)


# Ball
ornament = turtle.Turtle()
ornament.speed(0)
ornament.shape("circle")
ornament.color("red")
#ornament.shapesize(stretch_wid=(5), stretch_len=(1))
ornament.penup()
ornament.goto(0, 0)

ornament.dx = 2
ornament.dy = 2



# Paddle A upward
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)
    
# Paddle A downward
def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)
    
# Paddle B upward
def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)
    
# Paddle B downward
def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)
    
# Keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down") 



# Main game loop
while True:
    wn.update()
    
    
    # Move the ornament
    ornament.setx(ornament.xcor() + ornament.dx)
    ornament.sety(ornament.ycor() + ornament.dy)
    
    # Border check 
    if ornament.ycor() > 290:
        ornament.sety(290)
        ornament.dy *= -1
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    