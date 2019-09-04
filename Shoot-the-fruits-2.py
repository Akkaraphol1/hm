# Program name : Shoot-the-fruits-2.py
import pgzrun
import random
# define size window
WIDTH = 1280
HEIGHT = 720

#create oblect
apple = Actor('apple')
orange = Actor('orange')
pineapple = Actor('pineapple')
#function draw
def draw():
    global x1,y1,z1
    screen.fill("black")
    apple.draw()
    apple.topleft = x1,y1
    orange.draw()
    orange.topright = x1,z1
    pineapple.draw()
    pineapple.topleft = z1,y1
    
def update():
    global x1,y1,z1
    x1 += 120
    if x1 > WIDTH:
        x1 = 0
    y1 += 100
    if y1 > HEIGHT:
        y1 = 0
    z1 += 120
    if z1 > HEIGHT:
        z1 = 0

z1 = int(HEIGHT*10)        
x1 = int(WIDTH*2)
y1 = int(HEIGHT*2)

def on_mouse_down(pos):
    if apple.collidepoint(pos):
        print("good Chot!")
        place_apple()
    elif orange.collidepoint(pos):
        print("good Chot!")
        place_orange()
    elif pineapple.collidepoint(pos):
        print("good Chot!")
        place_pineapple()   
    else :
        print("You missed")

def place_apple():
    apple.x = random.randint(600,600)
    apple.y = random.randint(600,600)
def place_orange():
    orange.x = random.randint(600,600)
    orange.y = random.randint(600,600)
def place_pineapple():
    pineapple.x = random.randint(600,600)
    pineapple.y = random.randint(600,600)
    
place_apple()
place_orange()
place_pineapple()
pgzrun.go()
