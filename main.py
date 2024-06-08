import random
import turtle
import time
import pyautogui
from gif_process import frame_list

genislik, yukseklik = pyautogui.size()



screen=turtle.Screen()
screen_color="light blue"
screen.bgcolor(screen_color)
screen.title("catching a turtle")
screen.setworldcoordinates(-genislik/2 , -yukseklik/2 , genislik/2 , yukseklik/2)
screen.setup(genislik/1.5 , yukseklik/1.3)


instance = turtle.Turtle() ; instance.shapesize(0.01) ; instance.speed(0) ; instance.penup()
instance.color("black")
screen.addshape("turtle.gif")
instance.shape("turtle.gif")
gif_number=0


for i in frame_list:
    screen.addshape(f"frames/{i}")

def gif():
    global gif_number,frame_list
    instance.shape(f"frames/{frame_list[gif_number]}")
    gif_number=(gif_number+1)%len(frame_list)
    screen.ontimer(gif,45)

score_instance = turtle.Turtle() ;score_instance.penup() ;score_instance.hideturtle() ;score_instance.speed(0)
score_instance.color("red")


time_instance = turtle.Turtle()  ;time_instance.penup() ;time_instance.hideturtle() ;time_instance.speed(0)
time_instance.color("orange")


score_instance.goto(-120,350)
time_instance.goto(-110,300)
score_number=int(0)


def time_start():
    global time_number
    time_number=int(30)

time_start()



def score():
    score_instance.clear()
    score_instance.write(f"SCORE: {score_number}", font=("Times New Roman", 25, "normal"))

def time_count():
    global instance,time_number,restart_instance
    if time_number>0:
        time_instance.clear()
        time_instance.write(f"TIME: {time_number}", font=("Times New Roman", 20, "normal"))
        time_number=time_number-1
        change()
        screen.ontimer(time_count,1000)

    else:

        instance.hideturtle() ; instance.goto(0,0)
        time_instance.clear();time_instance.write(f"Game Over", font=("Times New Roman", 22, "normal"))

        restart_instance=turtle.Turtle()
        restart_instance.color("red")
        restart_instance.penup() ;restart_instance.hideturtle() ;restart_instance.speed(0)
        restart_instance.goto(-150,0)
        restart_instance.write(f"RESTART", font=("Times New Roman", 35, "normal")) ;restart_instance.goto(-175,-10)
        restart_instance.pendown()
        restart_instance.pensize(5)
        restart_instance.forward(470) ;restart_instance.left(90)
        restart_instance.forward(100) ;restart_instance.left(90)
        restart_instance.forward(470) ;restart_instance.left(90)
        restart_instance.shapesize(2);restart_instance.showturtle() ;restart_instance.forward(70)


click_lock=False
def unlock_lock():
    global click_lock
    click_lock=False

def loop():
    x = random.randint(int(-genislik / 1.5 * 0.90), int(genislik / 1.5 * 0.90))
    y = random.randint(int(-yukseklik / 1.3 * 0.60), int(yukseklik / 1.3 * 0.30))
    instance.goto(x, y)
change_lock=False
def change_uplock():
    global change_lock
    change_lock=False
def change():
    global change_lock
    if not change_lock:
        loop()
        change_lock=True
        screen.ontimer(change_uplock,500)

def restart_game():
    global score_number
    restart_instance.hideturtle()
    restart_instance.penup()
    restart_instance.clear()
    instance.showturtle()
    score_number = 0
    score()
    time_instance.clear()
    time_start()
    time_count()

def click(x, y):
    global score_number, click_lock
    if time_number>0:
        def pos():
            position = instance.pos()
            left_offset = 35  # Kaplumbağanın sol tarafındaki mesafe
            right_offset = 37  # Kaplumbağanın sağ tarafındaki mesafe
            top_offset = 20  # Kaplumbağanın üst tarafındaki mesafe
            bottom_offset = 16  # Kaplumbağanın alt tarafındaki mesafe

            left = position[0] - left_offset
            right = position[0] + right_offset
            top = position[1] + top_offset
            bottom = position[1] - bottom_offset

            within_x_bounds = left <= x <= right
            within_y_bounds = bottom <= y <= top

            """print(f"Kaplumbağa pozisyonu: {position}, Tıklama: {(x, y)}, "
                  f"\nX sınırları: ({left}, {right}), Y sınırları: ({bottom}, {top}), "
                  f"İçeride mi: {within_x_bounds and within_y_bounds}")"""

            return within_x_bounds and within_y_bounds


        if not click_lock:
            if pos():
                score_number+=1
                score()
                click_lock=True
                change()
                screen.ontimer(unlock_lock, 100)
    if time_number<=0:
        if x>-189 and x<303 and y<95 and y>-15:
            restart_game()


screen.listen()
screen.ontimer(score,200)
screen.ontimer(time_count,200)
screen.onscreenclick(click)
screen.ontimer(gif,100)

turtle.mainloop()