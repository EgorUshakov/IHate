from SimpleGraphics import *
# Change the background to sky blue 
background("deep sky blue")

#Draw a rectangle using named colors
setColor("green")
rect(0, 400, 890, 200)

#Sun
setColor("yellow")
ellipse(700, 0, 200, 200)

#Rectangle for house
setColor("purple")
rect(220, 200, 300, 200)

#Rectangle for Window
setOutline("black")
setColor("gold1")
rect(410, 250, 75, 75)

#Lines for Wind
setColor("black")
line(410, 290, 485, 290)
line(450, 250, 450, 330)

#Rectangle is used for a door
rect(240, 240, 100, 160)

#polygon is used to create the roof
setColor("brown")
polygon(220, 200, 520, 200, 360, 100) 

#The sky is created through the overlapping ellipses 
setColor("snow")
ellipse(100, 0, 200, 100)
ellipse(150, 0, 250, 100)

#Name 
setColor("black") 
text(700, 550, "Egor Ushakov")