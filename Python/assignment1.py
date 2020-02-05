# Egor Ushakov ID Number 30009589

#Purpose: Take two integers as input and center the image based on those values

x=int(input("Enter an x value"))
y=int(input("Enter an y value"))

from SimpleGraphics import *
#Deep sky blue background
background("deep sky blue")

#Head of the Smiley Face 
setColor("yellow")
ellipse(x-200, y-200, 400, 400)

#Eyes of the Smiley Face 
setColor("blue")
ellipse(x+40, y-150, 50, 50 )
ellipse(x-130, y-150, 50, 50 )

#Lips(made up of an ellipse)
setColor("red")
ellipse(x-100, y+100, 200, 50) 

#Lips(line is used to separate the upper lip and the lower lip)
setColor("black")
line(x-100, y+125, x+100, y+125)

#Go-tie(Pie Slice)
setColor("brown")
pieSlice(x-50, x+50, 100, 100, 60, 60)

#Nose(pie slice)
setColor("brown")
pieSlice(x-75, y-60, 100, 100, 330, 60)

#Eyebrows
setColor("black")
rect(x-125, y-170, 75, 15)
rect(x+35, y-175, 75, 15)

#Ears 
setColor("yellow")
ellipse(x+150, y-75, 100, 175 )
ellipse(x-275, y-75, 100, 175 )

#Ear Hole 
setColor("black")
ellipse(x+180, y-50,60,100)
ellipse(x-260, y-50 ,60,100)

