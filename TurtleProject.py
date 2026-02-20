"""
import turtle
drawing_board=turtle.getscreen() #bir ekran olusturuyoruz
drawing_board.bgcolor("white") #olusturduğumuz ekranın  arka planını atıyourz. bunu kodla yapabiliriz internette hex cod yazınca cıkar
drawing_board.title("Turtle Game") #ekrandaki yazmasını istediğimiz yazı
turtle_instance =turtle.Turtle() # imleci olustururuz
turtle_instance.forward(100) #360 derecelik açılara göre ayarlanıyor
turtle_instance.left(90)
turtle_instance.forward(100) # kac bırım ılerı gıdecegını soylerız
turtle_instance.left(90) #sol tarafa kac derecelık acıyla dondugunu soylerız
turtle_instance.forward(100)
turtle_instance.left(90)
turtle_instance.forward(100)
turtle.done() # kapatırız
"""
import turtle

""""
import turtle
drawing_board=turtle.getscreen() #bir ekran olusturuyoruz
drawing_board.bgcolor("white") #olusturduğumuz ekranın  arka planını atıyourz. bunu kodla yapabiliriz internette hex cod yazınca cıkar
drawing_board.title("Turtle Game") #ekrandaki yazmasını istediğimiz yazı
turtle_instance =turtle.Turtle() # imleci olustururuz
turtle_instance.forward(100)
turtle_instance.left(144)
turtle_instance.forward(100)
turtle_instance.right(100)
turtle_instance.forward(100)
turtle_instance.left(144)
turtle_instance.forward(100)
turtle_instance.right(90)
turtle_instance.forward(100)
turtle_instance.left(144)
turtle_instance.forward(100)
turtle_instance.right(90)
turtle_instance.forward(100)
turtle_instance.left(144)
turtle_instance.forward(100)
turtle_instance.right(90)
turtle_instance.forward(100)
turtle_instance.left(144)
turtle_instance.forward(100)
turtle_instance.right(90)
turtle_instance.forward(100)
turtle_instance.left(144)
turtle_instance.forward(100)
turtle_instance.right(90)
turtle_instance.forward(100)
turtle_instance.left(144)
turtle_instance.forward(100)
turtle.done() # kapatırız
"""
"""
turtle_instance=turtle.Turtle()
numside=5
angle=360/numside*2
sideleng=100
for i in range(numside):
    turtle_instance.right(angle)
    turtle_instance.forward(sideleng)
turtle.done()
"""

"""
drawing_board=turtle.getscreen()
drawing_board.bgcolor("white")
turtle_instance=turtle.Turtle()
turtle_instance.color("red")
def drawing(size):
    for i in range(4):
        turtle_instance.forward(size)
        turtle_instance.left(90)
        size-=5

drawing(150)
drawing(145)
drawing(140)
drawing(135)
drawing(130)
drawing(125)
drawing(120)
drawing(115)
drawing(110)
drawing(105)
drawing(100)
drawing(95)
drawing(90)
drawing(85)
drawing(80)
drawing(75)
drawing(70)
drawing(65)
drawing(60)
drawing(55)
drawing(50)
drawing(45)
drawing(40)
drawing(35)
drawing(30)

turtle.done()
"""

#daire böyle çizilir. ve açılarını değiştirebiliriz
drawing_board=turtle.getscreen()
drawing_board.bgcolor("white")
turtle_instance=turtle.Turtle()
turtle_instance.color("red")
turtle.speed(1)

turtle_colors=["red","yellow","purple","blue","green","orange"]

for i in range(6):
    turtle_instance.color(turtle_colors[i])
    turtle_instance.circle(10*i)
    turtle_instance.circle(-10*i)
    turtle_instance.left(50)

#turtle.done()
turtle.mainloop()