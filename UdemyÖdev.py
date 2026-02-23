import turtle
import random

screen = turtle.Screen()
screen.setup(width=768, height=648)
screen.bgcolor("black")

target = turtle.Turtle()
target.shape("turtle")
target.color("white")
target.turtlesize(2)
target.penup()

sayac = 0
puan = 0

def isinal():
    global sayac
    if sayac < 10:
        target.hideturtle()
        x = random.randint(-384, 384)
        y = random.randint(-324, 324)
        target.goto(x, y)
        target.showturtle()
        sayac += 1
        screen.ontimer(isinal, 1000)
    else:
        print(f"Oyun bitti! Toplam puan: {puan}")
        target.hideturtle()

def koordinat_goster(x, y):
    global puan
    if target.distance(x, y) < 20:  # Tıklama hedefe yakınsa
        puan += 1
        print(f"Tebrikler! Puan: {puan}")
    else:
        print(f"Iska! Puan: {puan}")

screen.onscreenclick(koordinat_goster)
isinal()
screen.mainloop()