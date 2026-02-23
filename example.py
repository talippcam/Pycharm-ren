import turtle


t = turtle.Turtle()
Ekran_Oyun=turtle.Screen()
Ekran_Oyun.bgcolor("green")
Ekran_Oyun.title("Yılan Oyunu")
t.shape("classic")
t.speed(0)
t.pen(fillcolor="black", pencolor="red", pensize=5)
joe=t.clone()
joe.shape("turtle")
def left():
    t.left(90)
    t.color("red")
def right():
    t.right(90)
def forward():
    t.fd(10)
def back():
    t.left(180)
def geriDön():
    print(t.pos())
def takeCoord():
    print(t.pos())
def Clear_Screen():
    t.clear()
def Tp():
    t.teleport(70.00,210.00)
def TurnHome():
    t.home()
def DaireÇiz():
    t.circle(50)
def stampyapıcı():
    t.stamp()
    t.forward(100)
def stampsilici():
    t.clearstamp()
def GeriAlıcı():
    t.undo()
def DöndürxCoord():
    print(round(t.xcor(),5))
def DöndüryCoord():
    print(round(t.ycor(),5))
def uzaklıkHesapla():
    print(round(t.distance(0,0),5))
def KalemKaldır():
    t.penup()
def Kalemindir():
    t.pendown()
def SaklaKaplımbağa():
    t.hideturtle()
def GösterKaplumbağa():
    t.showturtle()
def KaplumbağaKontrol():
    print(t.isvisible())
Ekran_Oyun.listen()
Ekran_Oyun.onkey(left,"a")
Ekran_Oyun.onkey(right,"d")
Ekran_Oyun.onkey(forward,"w")
Ekran_Oyun.onkey(back,"s")
Ekran_Oyun.onkey(geriDön,"h")
Ekran_Oyun.onkey(takeCoord,"t")
Ekran_Oyun.onkey(Clear_Screen,"c")
Ekran_Oyun.onkey(Tp,"i")
Ekran_Oyun.onkey(TurnHome,"y")
Ekran_Oyun.onkey(DaireÇiz,"p")
Ekran_Oyun.onkey(stampsilici,"x")
Ekran_Oyun.onkey(stampyapıcı,"z")
Ekran_Oyun.onkey(GeriAlıcı,"m")
Ekran_Oyun.onkey(DöndürxCoord,"f")
Ekran_Oyun.onkey(DöndüryCoord,"g")
Ekran_Oyun.onkey(uzaklıkHesapla,"q")
Ekran_Oyun.onkey(KalemKaldır,1)
Ekran_Oyun.onkey(Kalemindir,2)
Ekran_Oyun.onkey(SaklaKaplımbağa,3)
Ekran_Oyun.onkey(GösterKaplumbağa,4)
Ekran_Oyun.onkey(KaplumbağaKontrol,"5")
turtle.done()
