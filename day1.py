from turtle import *

#we want to paint a house

#step 1: draw a square 
speed(10)
width(7)
color("brown")
forward(200)
left(90)
     
forward(200)
left(90)
forward(200)
left(90)
forward(200)
#end of square

#drawing a door 

left(90)
forward(70)
color("black")

begin_fill()
left(90)               #proporties of door 
forward(95)
right(90)
forward(50)
right(90)
forward(95)
end_fill()

penup()
goto(200,200)
pendown()
left(220)
color("blue")        #proporties of the roof
begin_fill()
forward(160)
left(100)
forward(155)
end_fill()

#end of the roof

#drawing the windows

penup()
goto(120,130)
pendown()

color("green")
begin_fill()

left(220)
forward(50)
right(90)
forward(50)    
right(90)
forward(50)
right(90)
forward(50)               #windows
penup()
goto(30,135)
pendown()      
right(90)
forward(45)
right(90)
forward(45)
right(90)
forward(45)
right(90)
forward(45)
end_fill()


exitonclick()
