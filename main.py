import turtle
import time
import random
import pygame



turtlescreen = turtle.Screen()
turtlescreen.title("Catch The AstroTurtle! @lockheedist")
turtlescreen.bgpic("turtlespace.gif")
#turtlescreen.setup(width=.75, height=0.5, startx=None, starty=None)
# turtlescreen.bgcolor("light yellow")





#Sound Systems
pygame.init()
pygame.mixer.init()
sound = pygame.mixer.Sound('turtlemusic.mp3')
pygame.mixer.Sound.play(sound)
pygame.mixer.Sound.set_volume(sound, 0.1)

m = 0
def stop_music():
    global m
    if m==0:
        pygame.mixer.pause()
        m = 1
    elif m==1:
        pygame.mixer.unpause()
        m = 0


#Scoreboard and Turtle positioning again
score=0
pen= turtle.Turtle()
pen.hideturtle()
pen.color("light blue")
pen.penup()
pen.goto(0, 250)
pen.write(f"Score: {score}", align="center", font=('Courier New', 32, "bold"))

def scoreincrease(*args):
    global score
    score +=1
    turtlegorandom()
    #Score dash update with little animation.
    pen.clear()
    pen.color("white")
    pen.write(f"Score: {score}", align="center", font=('Courier New', 36, "bold"))
    time.sleep(0.4)
    pen.clear()
    pen.color("red")
    pen.write(f"Score: {score}", align="center", font=('Courier New', 32, "bold"))
    time.sleep(0.3)
    pen.clear()
    pen.color("light blue")
    pen.write(f"Score: {score}", align="center", font=('Courier New', 32, "bold"))



#randomturtle
instance = turtle.Turtle()
instance.shape("turtle")
instance.shapesize(2,2)
instance.speed(0)
turtle.tracer()#n=2, delay=0
instance.penup()


def turtlegorandom(*args):
    instance.goto(random.randint(-300, 300), random.randint(-300, 300))







turtlescreen.listen()

turtlescreen.onkey(fun=stop_music,key='m')
instance.onclick(fun=scoreincrease)





turtle.mainloop()