import turtle

drawing_board = turtle.Screen()
drawing_board.bgcolor("white")
drawing_board.title("Yeni Oyun")

turtle_instance=turtle.Turtle()
turtle_instance.speed(1)
turtle_instance.color("red")
def forward():
    turtle_instance.forward(100)
    """"turtle_instance.setheading(turtle_instance.heading()+20)ikiside aynı manaya gelir"""
def left():
    turtle_instance.left(10)
    """turtle_instance.setheading(turtle_instance.heading() - 20) ikiside aynı manaya gelir """
def right():
    turtle_instance.right(10 )
def back():
    turtle_instance.left(180)
def clear():
    turtle_instance.clear()
def return_home():
    turtle_instance.home()
def pen_up():
    turtle_instance.penup()
def pen_down():
    turtle_instance.pendown()
drawing_board.listen()
drawing_board.onkey(fun=forward, key="w")
drawing_board.onkey(fun=left, key="a")
drawing_board.onkey(fun=right, key="d")
drawing_board.onkey(fun=back, key="s")
drawing_board.onkey(fun=clear, key="i")
drawing_board.onkey(fun=return_home, key="h")
drawing_board.onkey(fun=pen_up, key="2")
drawing_board.onkey(fun=pen_down, key="1")
turtle.mainloop() #adas