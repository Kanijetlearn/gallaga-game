import pgzrun
import random
# Set Height and Width
WIDTH = 400
HEIGHT = 600

RED = (255,0,0)
GREEN =(0,255,0)
BLUE = (0,0,255)
BLACK =(0,0,0)
WHITE = (255,255,255)


ship = Actor("galaga")
ship.x = WIDTH//2
ship.y = HEIGHT-100
ship.dead= False


bullets = []

enemies = []

for x in range(8):
    for y in range(4):
        enemies.append(Actor("bug"))
        enemies[-1].x =100 + 40*x
        enemies[-1].y = 0 + 20 *y

score =0
direction = 1

def drawScore():
    screen.draw.text(str(score),(50,30))



def on_key_down(key):
    if ship.dead == False:
        if key == keys.SPACE:
            bullets.append(Actor("bullet"))
            bullets[-1].x= ship.x
            bullets[-1].y = ship.y-40


def update():
    global score
    global direction
    if ship.dead == False:
        if keyboard.left:
            ship.x-=2
        elif keyboard.right:
            ship.x+=2               
        
    for bullet in bullets:
        if bullet.y<-20:
            bullets.remove(bullet)
        else:
            bullet.y -=10
    moveDown = False
    if len(enemies)>0 and (enemies[-1].x > WIDTH - 20 or enemies[0].x < 20):
        moveDown = True
        direction = direction*-1
    for enemy in enemies:
        enemy.x += 2*direction
        if moveDown == True:
            enemy.y += 30
        for bullet in bullets:
            if enemy.colliderect(bullet):
                score += 150
                bullets.remove(bullet)
                enemies.remove(enemy)
        if enemy.colliderect(ship):
            ship.dead = True




def draw():
    screen.clear()
    screen.fill(BLUE)
    
    for bullet in bullets:
        bullet.draw()
    for enemy in enemies:
        enemy.draw()
    if ship.dead==False:
        ship.draw()
    drawScore()

pgzrun.go()
