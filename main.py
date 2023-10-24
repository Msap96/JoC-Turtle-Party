#Turtle Project Party
#By Marc Sapienza
#10/24/23

import turtle

turtle.color('red')

def back(len):
  turtle.penup()
  turtle.backward(len)
  turtle.pendown()
  
def move(len):
    back(-1 * len)

def polygon(num, size):
  for i in range(num):
    turtle.forward(size)
    turtle.right(360 / num)

def spiral(len, angle):
  for i in range(len, 5, -5):
    turtle.forward(i)
    turtle.right(angle)

spiral(70,60)
back(100)
turtle.color("blue")
spiral(60,75)
back(75)
turtle.color(“green”)
spiral(50,90)
