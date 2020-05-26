#Plantation The game
#A farming game by G - NERD
#written in Python 3.6.9

#This game is a basic farming game written with python with the turtle module
#My very first actual ame that I made using python turtle
#I leaned a lot of stuffs from this coding

#Enjoy playing the Game!

#importing stuff we needed
import turtle
import math
import random
import time

#turtle background seeting up
wn=turtle.Screen()
wn.title("Plantation The Game")
wn.bgcolor("gold")

#player's stats
#player's gold
gold = 100000

#player's tools level
axeLevel = 1
pickLevel = 1
shovelLevel = 1

#field stats
field1 = 0
field2 = 0
field3 = 0

#seed's stats
appleSeeds = 0
eggplantSeeds = 0
strawberrySeeds = 0
spinachSeeds = 0
burgerSeeds = 0

#making the turtle for writing warnings
warning=turtle.Turtle()
warning.speed(0)
warning.ht()
warning.color("red")
warning.penup()
warning.setpos(-100, -250)

#making a turtle for exiting scenes in every mainloop
exiter=turtle.Turtle()
exiter.speed(0)
exiter.penup()
exiter.shape("circle")
exiter.color("purple")
exiter.setpos(-175, -100)
exiter.ht()

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

#creating player
player=turtle.Turtle()
player.speed(0)
player.penup()
player.shape("square")
player.color("red")

#player's speed of moving
playerspeed = 15

#player movement definition
#forward movement
def forward():
	player.setheading(90)
	y = player.ycor()
	y += playerspeed
	if y > 280:
		y = 280
	player.sety(y)
#backward movement
def backward():
	player.setheading(270)
	y = player.ycor()
	y -= playerspeed
	if y < -280:
		y =-280
	player.sety(y)
#right movement
def right():
	player.setheading(0)
	x = player.xcor()
	x += playerspeed
	if x > 280:
		x = 280
	player.setx(x)
#left movement
def left():
	player.setheading(180)
	x = player.xcor()
	x -= playerspeed
	if x < -280:
		x = -280
	player.setx(x)


#defining help
def help():
	HelpCenter = True
	player.setpos(0, -200)
	blocker.showturtle()
	pen.setpos(-300, 300)
	pen.write("INSTRUCTIONS: ", font=("Arial", 18, "bold"))
	pen.setpos(-300, 200)
	pen.write("Use arrow keys to move", font=("Arial", 15, "bold"))
	pen.setpos(-300, 150)
	pen.write("Use the a key to use the axe to break things like trees and items", font=("Arial", 15, "bold"))
	pen.setpos(-300, 100)
	pen.write("Use the p key to use the pickaxe to break things like rocks and ores", font=("Arial", 15, "bold"))
	pen.setpos(-300, 50)
	pen.write("Use the s key to use the shovel to make your dirt plantable", font=("Arial", 15, "bold"))
	pen.setpos(-300, 0)
	pen.write("Use the w key to water your plants, but you must youch them first!", font=("Arial", 15, "bold"))
	pen.setpos(-100, -150)
	pen.write("Press 0 to quit help", font=("Arial", 15, "bold"))

#closing help center
def closeHelp():
	HelpCenter = False
	player.setpos(0, 0)
	pen.clear()
	blocker.ht()

#detections of keyboard events
turtle.listen()
turtle.onkey(forward, "Up")
turtle.onkey(backward, "Down")
turtle.onkey(right, "Right")
turtle.onkey(left, "Left")

#sepcial keys
#help center opener and closer
turtle.onkey(help, "h")
turtle.onkey(closeHelp, "0")

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

#making the Inventory list
inv=turtle.Turtle()
inv.penup()
inv.speed(0)
inv.ht()
inv.setpos(-450, 300)
#basic starting tools
inv.write("Inventory: ", font=("Arial", 15, "bold"))
inv.setpos(-450, 270)
inv.write("- Water Bucket(w)", font=("Arial", 12, "normal"))
inv.setpos(-450, 240)
inv.write("- Shovel(s)", font=("Arial", 12, "normal"))
inv.setpos(-450, 210)
inv.write("- Pickaxe(p)", font=("Arial", 12, "normal"))
inv.setpos(-450, 180)
inv.write("- Axe(a)", font=("Arial", 12, "normal"))

#making thw stats writer
statswriter=turtle.Turtle()
statswriter.speed(0)
statswriter.penup()
statswriter.ht()
statswriter.setpos(350, 290)
statswriter.write("Gold = ", font=("Arial", 12, "bold"))

#making the pen for gold
money=turtle.Turtle()
money.speed(0)
money.ht()
money.penup()
money.setpos(410, 290)
money.write(gold, font=("Arial", 12, "bold"))

#store buyings
#making the variables for amount writing properties
AppleInv = 0
EggplantInv = 0
StrawberryInv = 0
SpinachInv = 0
BurgerInv = 0

#buying appleSeeds
def Buyapple():
	#making the variable gold becoming a global variable
	global gold
	#checking the amount of gold
	if gold > 24:
		#adding seed to Inventory
		global appleSeeds
		appleSeeds += 1
		gold -= 25
		money.clear()
		money.write(gold, font=("Arial", 12, "bold"))
		#making the AppleInv a global
		global AppleInv
		AppleInv = 1
	else:
		#informing the player that they didn't have enough gold
		warning.write("Not enough gold...", font=("Arial", 32, "bold"))
		time.sleep(2)
		warning.clear()

#buying eppplantSeeds
def Buyeggplant():
	#making gold a global variable
	global gold
	#checking the amout of gold
	if gold > 11:
		#adding the eggplant Seeds to the Inventory
		global eggplantSeeds
		eggplantSeeds += 1
		gold -= 12
		money.clear()
		money.write(gold, font=("Arial", 12, "bold"))
		global EggplantInv
		EggplantInv = 1
	else:
		#informing the player that they didn't have enough gold
		warning.write("Not enough gold...", font=("Arial", 32, "bold"))
		time.sleep(2)
		warning.clear()

#buying strawberry Seeds
def BuyStrawberry():
	#making gold a global variable
	global gold
	#checking amount of gold needed
	if gold > 19:
		#adding strawberry Seeds to the Inventory
		global strawberrySeeds
		strawberrySeeds += 1
		gold -= 20
		money.clear()
		money.write(gold, font=("Arial", 12, "bold"))
		global StrawberryInv
		StrawberryInv = 1
	else:
		#informing the player that they didn't enough gold to buy the seed
		warning.write("Not enough gold...", font=("Arial", 32, "bold"))
		time.sleep(2)
		warning.clear()

#buying the spinachSeeds
def BuySpinach():
	#making the gold a global variable
	global gold
	#checking the amount of gold
	if gold > 14:
		#adding the gold to Inventory
		global spinachSeeds
		spinachSeeds += 1
		gold -= 15
		money.clear()
		money.write(gold, font=("Arial", 12, "bold"))
		global SpinachInv
		SpinachInv = 1
	else:
		#informing the player that they didn't have enough gold
		warning.write("Not enough gold...", font=("Arial", 32, "bold"))
		time.sleep(2)
		warning.clear()

#buying the burger
def Buyburger():
	#making the gold a global variable
	global gold
	#checking the amount of gold
	if gold > 29:
		#adding the burger ro the Inventory
		global burgerSeeds
		burgerSeeds += 1
		gold -= 30
		money.clear()
		money.write(gold, font=("Arial", 12, "bold"))
		global BurgerInv
		BurgerInv = 1
	else:
		#informing the player that they didn't have enough gold to buy the seed
		warning.write("Not enough gold...", font=("Arial", 32, "bold"))
		time.sleep(2)
		warning.clear()

#making the definition of the tools upgrade
#defining upgrading axeLevel
def UpgradeAxe():
	#making the variable gold to become a global
	global gold
	#calculating the gold that the player had
	if gold > 149:
		global axeLevel
		axeLevel += 1
		gold -= 150
		money.clear()
		money.write(gold, font=("Arial", 12, "bold"))
	else:
		warning.write("Not enough Gold...", font=("Arial", 32, "bold"))
		time.sleep(2)
		warning.undo()

#defining upgrade pickaxe
def UpgradePickAxe():
	#making gold a global variable
	global gold
	#checking player's gold
	if gold > 149:
		global pickLevel
		pickLevel += 1
		gold -= 150
		money.clear()
		money.write(gold, font=("Arial", 12, "bold"))
	else:
		warning.write("Not enough Gold...", font=("Arial", 32, "bold"))
		time.sleep(2)
		warning.undo()

#defining upgrade Shovel
def UpgradeShovel():
	#making gold a global
	global gold
	#checking player's gold
	if gold > 99:
		global shovelLevel
		shovelLevel += 1
		gold -= 100
		money.clear()
		money.write(gold, font=("Arial", 12, "bold"))
	else:
		warning.write("Not enough Gold...", font=("Arial", 32, "bold"))
		time.sleep(2)
		warning.undo()

#defining the farming ability
#the farming with dirt1
def dirtCOL():
	field1 = 1
	pen.setpos(-200, 0)
	pen.write("dirt row 1 is now plantable", font=("Arial", 14, "bold"))
	time.sleep(2)
	pen.undo()

#farming with dirt 2
def dirt2COL():
	field2 = 1
	pen.setpos(-200, 0)
	pen.write("dirt row 2 is now plantable", font=("Arial", 14, "bold"))
	time.sleep(2)
	pen.undo()

#farming dirt 3
def dirt3COL():
	field3 = 1
	pen.setpos(-200, 0)
	pen.write("dirt row 3 is now plantable", font=("Arial", 14, "bold"))
	time.sleep(2)
	pen.undo()

#making borders
border=turtle.Turtle()
border.speed(0)
border.penup()
border.setposition(-300, 300)
border.pensize(10)
border.pendown()
#drwing the borders
for edges in range(4):
	border.forward(600)
	border.right(90)
border.hideturtle()

#making dirt patches
#dirt line 1
dirt = turtle.Turtle()
dirt.speed(0)
dirt.color("brown")
dirt.shape("square")
dirt.shapesize(10, 2)
dirt.penup()
dirt.setheading(0)
dirt.setposition(-200, 150)

#dirt line 2
dirt2 = turtle.Turtle()
dirt2.speed(0)
dirt2.color("brown")
dirt2.shape("square")
dirt2.shapesize(10, 2)
dirt2.penup()
dirt2.setheading(0)
dirt2.setposition(-150, 150)

#dirt line 3
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

#making the axe
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

#making the door of the house
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
#setting the nmber of rocks
numOfrocks = random.randint(3, 5)
#creating list to make the rocks
rockPlaces = []
for rocks in range(numOfrocks):
	#making each of the rock turtle
	rockPlaces.append(turtle.Turtle())

#defining each rock's shape and stats
for rock in rockPlaces:
	rock.speed(0)
	rock.penup()
	rock.shape("square")
	rock.color("gray")
	rock.setposition(random.randint(-150, 250), random.randint(-250, -100))
	#defining the ability to break rocks
	def DestroyRock():
		global pickLevel
		for rock in rockPlaces:
			#checking distance from each rocks to the player
			rockBreak = math.sqrt(math.pow(player.xcor()- rock.xcor(),2)+ math.pow(player.ycor()- rock.ycor(),2))
			if rockBreak < 20:
				#cheking the pickaxe's level
				if pickLevel < 5:
					PickCheck()
				else:
					rock.setpos(400, -400)

	#making the variable for detecting pick level
	PickT = False

	#making the Level Check
	def PickCheck():
		#repeating the code fo every rocks
		for rock in rockPlaces:
			#making the PickT a global variable
			global PickT
			#Cheking the PickT's stat
			if PickT == False:
				#calculating the distance of player to the closest rock
				rockBreak = math.sqrt(math.pow(player.xcor()- rock.xcor(),2)+ math.pow(player.ycor()- rock.ycor(),2))
				if rockBreak < 20:
					#making the rock check the level and do acrion
					rock.setpos(rock.xcor(), rock.ycor())
					PickT = True

			else:
				#calculating the player's distance to the colsest rock and destroying it
				rockBreak = math.sqrt(math.pow(player.xcor()- rock.xcor(),2)+ math.pow(player.ycor()- rock.ycor(),2))
				if rockBreak < 20:
					rock.setpos(-400, 400)
					#using the PickT to break the rock's other stats
					PickT = False



#making random trees
#setting the number of trees
numOftrees = random.randint(3, 5)
#making the tree list
treePlaces = []
for trees in range(numOftrees):
	#creating tree turtles
	treePlaces.append(turtle.Turtle())

#defining tree stats and info
for tree in treePlaces:
	tree.speed(0)
	tree.shape("circle")
	tree.penup()
	tree.color("darkgreen")
	tree.setposition(random.randint(-150, 250), random.randint(-250, -100))
	#defining the ability to chop trees
	def ChopTree():
		global axeLevel
		for tree in treePlaces:
			#checking the tree's distance with the player
			treeDoom = math.sqrt(math.pow(player.xcor()- tree.xcor(),2)+ math.pow(player.ycor()- tree.ycor(),2))
			if treeDoom < 20:
				if axeLevel < 5:
					AxeCheck()
				else:
					tree.setpos(400, 400)

	#make a variable for checking the axe level
	AxeT = False

	#axeChecking for the axe level
	def AxeCheck():
		#repeating the code to ecvery tree in the game
		for tree in treePlaces:
			#making the axe stat and level a global
			global AxeT
			#checking the axe's stats
			if AxeT == False:
				#calculating the distance of the player to the closest tree
				treeDoom = math.sqrt(math.pow(player.xcor()- tree.xcor(),2)+ math.pow(player.ycor()- tree.ycor(),2))
				if treeDoom < 20:
					#making the tree unbreakable with only 1 hit
					tree.setpos(tree.xcor(), tree.ycor())
					#changing the axe's stats
					AxeT = True
			else:
				#calculating the distance of the closest rock
				treeDoom = math.sqrt(math.pow(player.xcor()- tree.xcor(),2)+ math.pow(player.ycor()- tree.ycor(),2))
				if treeDoom < 20:
					#destroying the clsest rock
					tree.setpos(-400, 400)
					#changing the axe's stats
					AxeT = False


#making seeds
#seed list = apples, eggplant, strawberry, spinach, burger

#make the game running
running = True

#main loop
while running:
		player.showturtle()


		#detecting collisions of the player with each column of dirt
		#ollision with the first row of the dirt
		dirtcol1 = math.sqrt(math.pow(player.xcor()-dirt.xcor(),2)+ math.pow(player.ycor()- dirt.ycor(),2))
		if dirtcol1 < 20:

			#checking for a action when colliding with the dirt row
			turtle.listen()
			turtle.onkey(dirtCOL, "s")

		#collision with the dirt riw 2
		dirtcol2 = math.sqrt(math.pow(player.xcor()- dirt2.xcor(),2)+ math.pow(player.ycor()- dirt2.ycor(),2))
		if dirtcol2 < 20:

			#checking for action when colliding
			turtle.listen()
			turtle.onkey(dirt2COL, "s")

		#checking the collision with dirt row 3
		dirtcol3 = math.sqrt(math.pow(player.xcor()- dirt3.xcor(),2)+ math.pow(player.ycor()- dirt3.ycor(),2))
		if dirtcol3 < 20:

			#checking for action when colliding
			turtle.listen()
			turtle.onkey(dirt3COL, "s")

		#detecting collisions of player with trees
		for tree in treePlaces:
			#calculating the closest distance of the player to the tree
			treeDoom = math.sqrt(math.pow(player.xcor()- tree.xcor(),2)+ math.pow(player.ycor()- tree.ycor(),2))
			if treeDoom < 20:

				#listening for action in the collision
				turtle.listen()
				turtle.onkey(ChopTree, "a")

		#detecting collisions of player and rocks
		for rock in rockPlaces:
			#checking the distance of the player to the closest rock
			rockBreak = math.sqrt(math.pow(player.xcor()- rock.xcor(),2)+ math.pow(player.ycor()- rock.ycor(),2))
			if rockBreak < 20:

				#checking for action when colliding
				turtle.listen()
				turtle.onkey(DestroyRock, "p")

		#detecting collisions of player and the store
		goTostore = math.sqrt(math.pow(player.xcor()- store.xcor(),2)+ math.pow(player.ycor()- store.ycor(),2))
		if goTostore < 60:
			STOREOpen = True
			blocker.showturtle()
			player.setpos(-400, 400)
			#swtting the gold info
			money.setpos(0, -300)
			money.write(gold, font=("Arial", 12, "bold"))
			#making the items and tools list in the store
			#Title text
			pen.setpos(-475, 200)
			pen.write("WELCOME TO WONDER STORE! (Press q to quit)", font=("Arial", 30, "bold"))
			#list of seeds for sale
			pen.setpos(-400, 100)
			pen.write("Available seeds: ", font=("Arial", 20, "normal"))
			pen.setpos(-400, 60)
			pen.write("- Apple Seed(a) ~ price = $25", font=("Arial", 12, "normal"))
			pen.setpos(-400, 30)
			pen.write("- EggPlant seed(e) ~ price = $12", font=("Arial", 12, "normal"))
			pen.setpos(-400, 0)
			pen.write("- strawberry seed(s) ~ price = $20", font=("Arial", 12, "normal"))
			pen.setpos(-400, -30)
			pen.write("- spinach seed(p) ~ price = $15", font=("Arial", 12, "normal"))
			pen.setpos(-400, -60)
			pen.write("- burger seed(b) ~ price = $30", font=("Arial", 12, "normal"))
			pen.setpos(0, 100)
			#tools uprades
			pen.write("Upgrade Tools: ", font=("Arial", 20, "normal"))
			pen.setpos(0, 70)
			pen.write("- Shovel(t) ~ price = $100", font=("Arial", 12, "normal"))
			pen.setpos(0, 40)
			pen.write("- PickAxe(o) ~ price = $150", font=("Arial", 12, "normal"))
			pen.setpos(0, 10)
			pen.write("- Axe(w) ~ price = $150", font=("Arial", 12, "normal"))

			player.setpos(-200, -100)
			exiter.setpos(-175, -100)

			#store loop
			while STOREOpen:
				player.showturtle()
				exiter.showturtle()

				QUITstore = math.sqrt(math.pow(player.xcor()- exiter.xcor(),2)+ math.pow(player.ycor()- exiter.ycor(),2))
				if QUITstore < 20:
					STOREOpen = False
					blocker.ht()
					pen.clear()
					money.undo()
					exiter.ht()
					player.setpos(0, 0)
					money.setpos(410, 290)
					money.write(gold, font=("Arial", 12, "bold"))
					if AppleInv == 1:
						inv.setpos(inv.xcor(), inv.ycor()- 30)
						inv.write("- Apple Seed", font=("Arial", 12, "normal"))

					if EggplantInv == 1:
						inv.setpos(inv.xcor(), inv.ycor()-30)
						inv.write(" - Eggplant seed", font=("Arial", 12, "normal"))

					if StrawberryInv == 1:
						inv.setpos(inv.xcor(), inv.ycor()-30)
						inv.write("- Stawberry Seed", font=("Arial", 12, "normal"))

					if SpinachInv == 1:
						inv.setpos(inv.xcor(), inv.ycor()-30)
						inv.write("- Spinach Seed", font=("Arial", 12, "normal"))

					if BurgerInv == 1:
						inv.setpos(inv.xcor(), inv.ycor()-30)
						inv.write("- Burger", font=("Arial", 12, "normal"))


				#checking for action in the loop
				turtle.listen()

				#checking for seed buying actions
				turtle.onkey(Buyapple, "a")
				turtle.onkey(Buyeggplant, "e")
				turtle.onkey(BuyStrawberry, "s")
				turtle.onkey(BuySpinach, "p")
				turtle.onkey(Buyburger, "b")

				#checking for action of buying tools upgrade
				turtle.onkey(UpgradeShovel, "t")
				turtle.onkey(UpgradePickAxe, "o")
				turtle.onkey(UpgradeAxe, "w")

		#detecting collisions of player with house
		goTohome = math.sqrt(math.pow(player.xcor()- door.xcor(),2)+ math.pow(player.ycor()- door.ycor(),2))
		if goTohome < 20:
			#setting the house scene
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


			#house' main loop
			while HOUSE:
				player.showturtle()

				#detecting the collisions of player with the door
				Outside = math.sqrt(math.pow(player.xcor()- door.xcor(),2)+ math.pow(player.ycor()- door.ycor(),2))
				if Outside < 20:
					#quitting the house
					blocker.hideturtle()
					door.setpos(100, 110)
					chestP.hideturtle()
					player.setpos(100, 80)
					pen.clear()
					HOUSE = False


				#detecting the collisions of player and chest
				InvChest = math.sqrt(math.pow(player.xcor()- chestP.xcor(),2)+ math.pow(player.ycor()- chestP.ycor(),2))
				if InvChest < 20:
					#setting the scene

					blocker2.showturtle()
					pen.setpos(0, 150)
					pen.write("Chest: ", font=("Arial", 15, "normal"))

					player.setpos(100, 100)
					exiter.setpos(130, 100)
					exiter.showturtle()

					#chest main loop
					ChestOP = True
					while ChestOP:
						player.showturtle()

						QUITchest = math.sqrt(math.pow(player.xcor()- exiter.xcor(),2)+ math.pow(player.ycor()- exiter.ycor(),2))
						if QUITchest < 20:
							ChestOP = False
							blocker2.ht()
							pen.undo()
							exiter.ht()
							player.setpos(0, 0)



#end of code :)
# I hope you enjoy the game!
#P.S. This game isn't perfect yet :)
