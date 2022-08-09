from turtle import *
from math import sin,cos,pi

v=5
l=500/2

a1=[0,l]
a2=[(-1)*l*cos(pi/6),l/2]
a3=[(-1)*l*cos(pi/6),(-1)*(l/2)]
a4=[0,-1*l]
a5=[l*cos(pi/6),-1*(l/2)]
a6=[l*cos(pi/6),l/2]

pts=[a1,a2,a3,a4,a5,a6]

getscreen()

t1=Turtle()
t1.width(2)
t1.color('red')
t1.up()
t1.setpos(a1)
t1.down()
t1.speed(v)

t2=Turtle()
t2.color('green')
t2.width(2)
t2.up()
t2.setpos(a2)
t2.down()
t2.speed(v)

t3=Turtle()
t3.color('pink')
t3.width(2)
t3.up()
t3.setpos(a3)
t3.down()
t3.speed(v)

t4=Turtle()
t4.color('blue')
t4.width(2)
t4.up()
t4.setpos(a4)
t4.down()
t4.speed(v)

t5=Turtle()
t5.color('black')
t5.width(2)
t5.up()
t5.setpos(a5)
t5.down()
t5.speed(v)

t6=Turtle()
t6.color('purple')
t6.width(2)
t6.up()
t6.setpos(a6)
t6.down()
t6.speed(v)

while True:
    if (abs(t1.pos()))<5:
        break
    print(abs(t1.pos()))
    t1.setheading(t1.towards(t2))
    t1.forward(v)

    t2.setheading(t2.towards(t3))
    t2.forward(v)

    t3.setheading(t3.towards(t4))
    t3.forward(v)

    t4.setheading(t4.towards(t5))
    t4.forward(v)

    t5.setheading(t5.towards(t6))
    t5.forward(v)

    t6.setheading(t6.towards(t1))
    t6.forward(v)
