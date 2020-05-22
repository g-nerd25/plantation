#importing
import turtle
import math
import random
import time
import pynput
from pynput import keyboard

#turtle background
wn=turtle.Screen()
wn.title("Plantation The Game")
wn.bgcolor("gold")

#making the shop and house scene blocker
blocker=turtle.Turtle()
blocker.speed(0)
blocker.shape("square")
blocker.shapesize(50, 50)
blocker.color("orange")
blocker.hideturtle()

#making chest half-blocker
blocker2=turtle.Turtle()
blocker2.speed(0)
blocker2.penup()
blocker2.shape("square")
blocker2.shapesize(20, 20)
blocker2.color("gray")
blocker2.hideturtle()

#item stats
waterBucket = 0
dirtShovel = 0
rockPick = 0

#creating player
player=turtle.Turtle()
player.speed(0)
player.penup()
player.shape("square")
player.color("red")

#player's speed
playerspeed = 15

#player movement definition
def forward():
	player.setheading(90)
	y = player.ycor()
	y += playerspeed
	if y > 280:
		y = 280
	player.sety(y)
def backward():
	player.setheading(270)
	y = player.ycor()
	y -= playerspeed
	if y < -280:
		y =-280
	player.sety(y)
def right():
	player.setheading(0)
	x = player.xcor()
	x += playerspeed
	if x > 280:
		x = 280
	player.setx(x)
def left():
	player.setheading(180)
	x = player.xcor()
	x -= playerspeed
	if x < -280:
		x = -280
	player.setx(x)

#detections of keyboard events
turtle.listen()
turtle.onkey(forward, "Up")
turtle.onkey(backward, "Down")
turtle.onkey(right, "Right")
turtle.onkey(left, "Left")

#making the store for buying seeds
store =turtle.Turtle()
store.speed(0)
store.shape("square")
store.shapesize(5, 5)
store.penup()
store.color("purple")
store.setpos(-200, -200)

#making pen for texts
pen=turtle.Turtle()
pen.penup()
pen.pensize(5)
pen.hideturtle()
pen.speed(0)

inv=turtle.Turtle()
inv.penup()
inv.speed(0)
inv.ht()
inv.setpos(-450, 300)
inv.write("Inventory: ", font=("Arial", 15, "bold"))
inv.setpos(-450, 270)
inv.write("- Water Bucket(w)", font=("Arial", 12, "normal"))
inv.setpos(-450, 240)
inv.write("- Shovel(s)", font=("Arial", 12, "normal"))
inv.setpos(-450, 210)
inv.write("- Pickaxe(p)", font=("Arial", 12, "normal"))
inv.setpos(-450, 180)
inv.write("- Axe(a)", font=("Arial", 12, "normal"))

#making borders
border=turtle.Turtle()
border.speed(0)
border.penup()
border.setposition(-300, 300)
border.pensize(10)
border.pendown()
for edges in range(4):
	border.forward(600)
	border.right(90)
border.hideturtle()

#making dirt patches
dirt = turtle.Turtle()
dirt.speed(0)
dirt.color("brown")
dirt.shape("square")
dirt.shapesize(10, 2)
dirt.penup()
dirt.setheading(0)
dirt.setposition(-200, 150)

dirt2 = turtle.Turtle()
dirt2.speed(0)
dirt2.color("brown")
dirt2.shape("square")
dirt2.shapesize(10, 2)
dirt2.penup()
dirt2.setheading(0)
dirt2.setposition(-150, 150)

dirt3 = turtle.Turtle()
dirt3.speed(0)
dirt3.color("brown")
dirt3.shape("square")
dirt3.shapesize(10, 2)
dirt3.penup()
dirt3.setheading(0)
dirt3.setposition(-100, 150)

#making water can
can=turtle.Turtle()
can.shape("circle")
can.speed(0)
can.penup()
can.setposition(-240, 240)
can.color("gray")
can.shapesize(0.8, 0.8)
can.ht()

#making shovel
shovel=turtle.Turtle()
shovel.speed(0)
shovel.shape("square")
shovel.shapesize(0.8, 0.8)
shovel.penup()
shovel.color("gray")
shovel.ht()

#making pickaxe
pick=turtle.Turtle()
pick.speed(0)
pick.shape("triangle")
pick.shapesize(0.8, 0.8)
pick.penup()
pick.color("gray")
pick.ht()

#making the pickaxeshovel=turtle.Turtle()
axe=turtle.Turtle()
axe.speed(0)
axe.shape("circle")
axe.shapesize(0.8, 0.8)
axe.penup()
axe.color("gray")
axe.ht()

#making house
#making the outside view
house=turtle.Turtle()
house.shape("square")
house.speed(0)
house.penup()
house.color("blue")
house.shapesize(7, 10)
house.setposition(100, 179)

#making the inner door of the house
door=turtle.Turtle()
door.speed(0)
door.shape("square")
door.penup()
door.shapesize(0.5, 2)
door.setpos(0, -295)
door.color("brown")
door.setpos(100, 110)

#making a chest for storing items
chestP=turtle.Turtle()
chestP.speed(0)
chestP.penup()
chestP.shape("square")
chestP.color("gold")
chestP.shapesize(1, 1.5)
chestP.setpos(-200, 200)
chestP.hideturtle()

#making random generated rocks
numOfrocks = random.randint(3, 5)
rockPlaces = []
for rocks in range(numOfrocks):
	rockPlaces.append(turtle.Turtle())

for rock in rockPlaces:
	rock.speed(0)
	rock.penup()
	rock.shape("square")
	rock.color("gray")
	rock.setposition(random.randint(-150, 250), random.randint(-250, -100))

#making random trees
numOftrees = random.randint(3, 5)
treePlaces = []
for trees in range(numOftrees):
	treePlaces.append(turtle.Turtle())

for tree in treePlaces:
	tree.speed(0)
	tree.shape("circle")
	tree.penup()
	tree.color("darkgreen")
	tree.setposition(random.randint(-150, 250), random.randint(-250, -100))

#making seeds
#seed list = apples, eggplant, strawberry, spinach, burger

running = True

while running:
	player.showturtle()

	goTostore = math.sqrt(math.pow(player.xcor()- store.xcor(),2)+ math.pow(player.ycor()- store.ycor(),2))
	if goTostore < 60:
		STORE = True
		blocker.showturtle()
		pen.setpos(-400, 200)
		pen.write("WELCOME TO WONDER STORE!", font=("Arial", 30, "bold"))
		pen.setpos(-400, 100)
		pen.write("Available seeds: ", font=("Arial", 20, "normal"))
		pen.setpos(-400, 60)
		pen.write("- Apple Seed ~ price = $25", font=("Arial", 12, "normal"))
		pen.setpos(-400, 30)
		pen.write("- EggPlant seed ~ price = $12", font=("Arial", 12, "normal"))
		pen.setpos(-400, 0)
		pen.write("- strawberry seed ~ price = $20", font=("Arial", 12, "normal"))
		pen.setpos(-400, -30)
		pen.write("- spinach seed ~ price = $15", font=("Arial", 12, "normal"))
		pen.setpos(-400, -60)
		pen.write("- burger seed ~ price = $30", font=("Arial", 12, "normal"))
		pen.setpos(0, 100)
		pen.write("Upgrade Tools: ", font=("Arial", 20, "normal"))
		pen.setpos(0, 70)
		pen.write("- Water Bucket ~ price = $50`", font=("Arial", 12, "normal"))
		pen.setpos(0, 40)
		pen.write("- Shovel ~ price = $100", font=("Arial", 12, "normal"))
		pen.setpos(0, 10)
		pen.write("- PickAxe ~ price = $150", font=("Arial", 12, "normal"))
		pen.setpos(0, -20)
		pen.write("- Axe ~ price = $150", font=("Arial", 12, "normal"))
		pen.setpos(-100, -200)
		pen.write("PRESS Q TO QUIT", font=("Arial", 17, "bold"))
		player.hideturtle()

		while STORE:
			pen.hideturtle()

			turtle.listen()



	goTohome = math.sqrt(math.pow(player.xcor()- door.xcor(),2)+ math.pow(player.ycor()- door.ycor(),2))
	if goTohome < 20:
		HOUSE = True
		blocker.showturtle()
		player.setpos(0, -275)

		pen.setpos(-280, 280)
		pen.pensize(5)
		for houseEdge in range(4):
			pen.pendown()
			pen.forward(600)
			pen.right(90)

		pen.pensize(1)
		pen.penup()

		door.setpos(0, -295)
		door.showturtle()
		chestP.setpos(-200, 200)
		chestP.showturtle()

		while HOUSE:
			player.showturtle()

			Outside = math.sqrt(math.pow(player.xcor()- door.xcor(),2)+ math.pow(player.ycor()- door.ycor(),2))
			if Outside < 20:
				blocker.hideturtle()
				door.setpos(100, 110)
				chestP.hideturtle()
				player.setpos(100, 80)
				pen.clear()
				HOUSE = False

			InvChest = math.sqrt(math.pow(player.xcor()- chestP.ycor(),2)+ math.pow(player.ycor()- chestP.ycor(),2))
			if InvChest < 20:
				blocker2.showturtle()
				pen.setpos(0, 150)
				pen.write("Chest: ", font=("Arial", 15, "normal"))

				ChestOP = True
				while ChestOP:
					player.hideturtle()





#end of code :)
