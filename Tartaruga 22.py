import turtle
a = turtle.Screen()
tartaruga = turtle.Turtle()
fundo = turtle.Screen()

fundo.colormode(255)
fundo.bgcolor((0, 0, 255))

tartaruga.speed(0)

colours = [(85, 211, 136), (197, 196, 126), (235, 233, 166), (25, 135, 222), (211, 64, 159), (159, 165, 106), (178, 160, 125), (36, 192, 70), (231, 184, 204), (63, 203, 219)]

for i in range(2000):
  tartaruga.color(colours[i % len(colours)])
  tartaruga.forward(i)
  tartaruga.right(98)
a.exitonclick()