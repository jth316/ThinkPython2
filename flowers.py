import math
import turtle

bob = turtle.Turtle()

def polyline(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)

#need to create an arc for the petals
def arc(t, r, angle):
    arc_length = 2 * math.pi * r * abs(angle) / 360
    n = int(arc_length / 4) + 3
    step_length = arc_length / n
    step_angle = float(angle) / n
    t.lt(step_angle/2)
    polyline(t, n, step_length, step_angle)
    t.rt(step_angle/2)

#creating a petal
def petal(t, r, angle):
    for i in range(2):
        arc(t, r, angle)
        t.lt(180-angle)

#creating a flower
def flower(t, n, r, angle):
    for i in range(n):
        petal(t, r, angle)
        t.rt(360.0/n)
    turtle.mainloop()

#flower(bob, 7, 60, 60)
#flower(bob, 10, 50, 80)
flower(bob, 20, 200, 20)