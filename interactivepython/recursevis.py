# import turtle

# myTurtle = turtle.Turtle()
# myWin = turtle.Screen()

# def drawSpiral(myTurtle, lineLen):
#     if lineLen > 0:
#         myTurtle.forward(lineLen)
#         myTurtle.right(90)
#         drawSpiral(myTurtle,lineLen-5)

# drawSpiral(myTurtle,100)
# myWin.exitonclick()

import turtle
from random import randrange

def tree(branchLen,t,thickness):	
    if branchLen > 5:
    	if branchLen > 10:
    		t.pencolor("brown")
    	else:
    		t.pencolor("green")
    	t.width(thickness)
        t.forward(branchLen)
        rand = randrange(15,45)
        rand2 = randrange(10,20)
        t.right(rand)
        tree(branchLen-rand2,t,thickness)
        t.left(rand*2)
        tree(branchLen-rand2,t,thickness)
        t.right(rand)
        t.penup()
        t.backward(branchLen)
        t.pendown()
    

def main():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("green")
    tree(75,t,5)
    myWin.exitonclick()

main()
