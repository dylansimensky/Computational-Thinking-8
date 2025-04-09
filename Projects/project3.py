# creates turtle
import turtle

# turns screen black
turtle.Screen().bgcolor("black")

# increases turtle speed
t = turtle.Turtle()
t.speed(50)

t.goto(0,0)
t.color("pink")

for i in range(40) :
    t.forward(101)
    t.left(125)


turtle.exitonclick()