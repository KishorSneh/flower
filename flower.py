import turtle
t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("#8D0B41")
t.pencolor("#D39D55")
t.speed(0)
for i in range(200):
    t.circle(190-i,90)
    t.lt(90)
    t.circle(190-i,90)
    t.lt(18)