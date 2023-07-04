import turtle

turtle.bgcolor("lightblue")
turtle.pensize(2.5)
turtle.speed(0.5)
color = ["red", "blue", "green", "orange"]
for a in range(18):
    for i in color:
        turtle.color(i)
        turtle.circle(100)
        turtle.left(10)
turtle.mainloop()