import math
import turtle

bob = turtle.Turtle()

def polyline(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)

#shapes made of triangles
def triangle(t, angle, length1, length2):
    for i in range (1):
        t.fd(length1)
        t.lt(angle)
        t.fd(length2)
        t.lt(angle)
        t.fd(length1)
    

def polygon(t, n, angle, length1, length2):
    t.lt(45)
    for i in range(n):
        triangle(t, angle, length1, length2)
        t.lt(180)
    turtle.mainloop()
    

#hexagon code
#polygon(bob, 6, 120, 100, 100)

#triangle(bob, 126, 100, 117)

#pentagon code
#polygon(bob, 5, 126, 100, 117)

#heptagon code
#polygon(bob, 7, 115.715, 100, 87)