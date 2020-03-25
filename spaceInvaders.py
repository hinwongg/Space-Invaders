import turtle
import os
import math
import random

#Screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Hins Space Invaders")
wn.bgpic("space_invaders_background.gif")

#Register the shapes
turtle.register_shape("invader.gif")
turtle.register_shape("player.gif")
turtle.register_shape("bird.gif")

#Border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300,-300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()

#Set the score to 0
score = 0

#Draw the score
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-290, 280)
scorestring = "Score: %s" %score
score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
score_pen.hideturtle()

#Creater the player turtle
player = turtle.Turtle()
player.color("blue")
player.shape("player.gif")
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)

#playerspeed = 15
playerspeed = 15 #hin testing

#Choose a number of enemies
number_of_enemies = 5

#Create an empty list of enemies
enemies = []

#Add enemies to the list
for i in range(number_of_enemies):
    #Create the enemy
    enemies.append(turtle.Turtle())
    
for enemy in enemies:
    #Draw the normal enemies
    enemy.color("red")
    enemy.shape("invader.gif") 
    enemy.penup()
    enemy.speed(0) #ok
    x = random.randint(-200, 200) 
    y = random.randint(100, 250)
    enemy.setposition(x,y)

###Special Enemies Section###
number_special_enemies = 2

special_enemies = []

for i in range(number_special_enemies):
    special_enemies.append(turtle.Turtle())

for enemy in special_enemies:
    enemy.color("purple")
    enemy.shape("bird.gif")
    enemy.penup()
    enemy.speed(0)
    x = random.randint(-200, 200)
    y = random.randint(100, 250)
    enemy.setposition(x,y)
###Special Enemies Section###
    
#enemyspeed = 2
enemyspeed = 2 #Hin just for testing. Does not follow the normal code

special_enemyspeed = 4

#Create the player's bullet
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5,0.5)
bullet.hideturtle()

#Create extra bullets
bulletOne = turtle.Turtle()
bulletOne.color("yellow")
bulletOne.shape("triangle")
bulletOne.penup()
bulletOne.speed(0)
bulletOne.setheading(90)
bulletOne.shapesize(0.5,0.5)
bulletOne.hideturtle()

bulletTwo = turtle.Turtle()
bulletTwo.color("yellow")
bulletTwo.shape("triangle")
bulletTwo.penup()
bulletTwo.speed(0)
bulletTwo.setheading(90)
bulletTwo.shapesize(0.5,0.5)
bulletTwo.hideturtle()



bulletspeed = 20

#Define bullet state
#ready - ready to fire
#fire - bullet is firing
bulletstate = "ready"
bulletstateOne = "ready"
bulletstateTwo = "ready"

#extraBullet "yes" means the player hit bonus enemy
extraBullet = "no"

#Move the player left
def move_left():
    x = player.xcor()
    x = x - playerspeed
    if x < -280:
        x = -280
    player.setx(x)

def move_right():
    x = player.xcor()
    x = x + playerspeed
    if x > 280:
        x = 280
    player.setx(x)

def fire_bullet():
    #Declare bulletstate as a global if it needs change
    global bulletstate
    global bulletstateOne
    global bulletstateTwo
    if bulletstate == "ready" and bulletstateOne == "ready" and bulletstateTwo == "ready":
        os.system("afplay laser.wav&")
        bulletstate = "fire"
        #Move the bullet to just above the player
        x = player.xcor()
        y = player.ycor() + 10
        bullet.setposition(x,y)
        bullet.showturtle()

        ###Extra bullet###
        if extraBullet == "yes":

            bulletstateOne = "fire"
            x = player.xcor() - 15
            y = player.ycor() + 10
            bulletOne.setposition(x,y)
            bulletOne.showturtle()
            
            bulletstateTwo = "fire"
            x = player.xcor() + 15
            y = player.ycor() + 10
            bulletTwo.setposition(x,y)
            bulletTwo.showturtle()

def isCollision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor() - t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    if distance < 15:
        return True
    else:
        return False
    
#Create keyboard bindings
turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.onkey(fire_bullet, "space")

#Count for each special enemy at the top
count = 0

#Main game loop
while True:

    for enemy in enemies:
        #Move the enemy
        x = enemy.xcor()
        x  = x + enemyspeed
        enemy.setx(x)

        #Move the enemy back and down
        if enemy.xcor() > 280:
            #Move all enemies down
            for e in enemies:
                y = e.ycor()
                y = y - 40
                e.sety(y)
            #Change enemy direction
            enemyspeed = enemyspeed * (-1)
            
        if enemy.xcor() < -280:
            #Move all enemies down
            for e in enemies:
                y = e.ycor()
                y = y - 40
                e.sety(y)
            #Change enemy direction
            enemyspeed = enemyspeed * (-1)

        #Check for collision between the bullet and the enemy
        if isCollision(bullet, enemy):
            os.system("afplay explosion.wav&")
            #Reset the bullet
            bullet.hideturtle()
            bulletstate = "ready"
            bullet.setposition(0,-400)
            #Reset the enemy
            x = random.randint(-200,200)
            y = random.randint(100,250)
            enemy.setposition(x, y)
            #Update the score
            score = score + 10
            scorestring = "Score: %s" %score
            score_pen.clear()
            score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
        #BulletOne
        if isCollision(bulletOne, enemy):
            os.system("afplay explosion.wav&")
            #Reset the bullet
            bulletOne.hideturtle()
            bulletstateOne = "ready"
            bulletOne.setposition(0,-400)
            #Reset the enemy
            x = random.randint(-200,200)
            y = random.randint(100,250)
            enemy.setposition(x, y)
            #Update the score
            score = score + 10
            scorestring = "Score: %s" %score
            score_pen.clear()
            score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
        #BulletTwo
        if isCollision(bulletTwo, enemy):
            os.system("afplay explosion.wav&")
            #Reset the bullet
            bulletTwo.hideturtle()
            bulletstateTwo = "ready"
            bulletTwo.setposition(0,-400)
            #Reset the enemy
            x = random.randint(-200,200)
            y = random.randint(100,250)
            enemy.setposition(x, y)
            #Update the score
            score = score + 10
            scorestring = "Score: %s" %score
            score_pen.clear()
            score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))

        if isCollision(player, enemy):
            os.system("afplay explosion.wav&")
            player.hideturtle()
            enemy.hideturtle()
            print("Game Over")
            break
        
####SPECIAL ENEMIES SECTION####
    for enemy in special_enemies:
        #Move the enemy
        x = enemy.xcor()
        x  = x + special_enemyspeed
        enemy.setx(x)

        #Move the enemy back and down
        if enemy.xcor() > 280:
            #Move all enemies down
            for e in special_enemies:
                y = e.ycor()
                y = y - 40
                e.sety(y)
            #Change enemy direction
            special_enemyspeed = special_enemyspeed * (-1)
            
        if enemy.xcor() < -280:
            #Move all enemies down
            for e in special_enemies:
                y = e.ycor()
                y = y - 40
                e.sety(y)
            #Change enemy direction
            special_enemyspeed = special_enemyspeed * (-1)

        #Check for collision between the bullet and the special enemy
        if isCollision(bullet, enemy):
            os.system("afplay explosion.wav&")
            #Reset the bullet
            bullet.hideturtle()
            bulletstate = "ready"
            bullet.setposition(0,-400)
            #Update the bullet so it has SUPERPOWERS
            extraBullet = "yes"
            #Put enemy at top of screen
            count = count + 20
            x = (-180) + count
            enemy.setposition(x, 290)
            #enemy.stamp()
            #enemy.hideturtle()
            enemy.clear()
                
####SPECIAL ENEMIES SECTION####

    #Move the bullet
    if bulletstate == "fire":
        y = bullet.ycor()
        y = y + bulletspeed
        bullet.sety(y)

    if bulletstateOne == "fire":  
        y = bulletOne.ycor()
        y = y + bulletspeed
        bulletOne.sety(y)

    if bulletstateTwo == "fire":
        y = bulletTwo.ycor()
        y = y + bulletspeed
        bulletTwo.sety(y)

    #Check to see if the bullet has gone to the top
    if bullet.ycor() > 275:
        bullet.hideturtle()
        bulletstate = "ready"
        
    if bulletOne.ycor() > 275:
        bulletOne.hideturtle()
        bulletstateOne = "ready"
        
    if bulletTwo.ycor() > 275:
        bulletTwo.hideturtle()
        bulletstateTwo = "ready"
       

   
        
        

delay = raw_input("Press enter to finish.")
