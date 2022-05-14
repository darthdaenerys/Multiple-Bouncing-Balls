
# import libraries and packages
from vpython import *
import time
import winsound

# vpython canvas
canvas(width=1320,height=680)

# beep parameters
frequency=5000
duration=100

# ball and room parameters
xpos1=0
ypos1=0
zpos1=0
xpos2=2
ypos2=3
zpos2=4
deltax1=.2
deltay1=.3
deltaz1=.5
deltax2=.5
deltay2=.3
deltaz2=.2
b1radius=.3
b2radius=.4
wallthickness=.1
roomheight=10
roomlength=10
roomdepth=10
roomcolor=color.cyan

# creating the room
floor=box(pos=vector(0,-roomheight/2,0),size=vector(roomlength,wallthickness,roomdepth),color=color.green,opacity=0.8)
ceiling=box(pos=vector(0,roomheight/2,0),size=vector(roomlength,wallthickness,roomdepth),color=color.green,opacity=0.8)
left=box(pos=vector(-roomlength/2,0,0),size=vector(wallthickness,roomheight,roomdepth),color=roomcolor,opacity=0.8)
right=box(pos=vector(roomlength/2,0,0),size=vector(wallthickness,roomheight,roomdepth),color=roomcolor,opacity=0.8)
back=box(pos=vector(0,0,-roomdepth/2),size=vector(roomlength,roomheight,wallthickness),color=roomcolor,opacity=0.8)

# creating balls
ball1=sphere(pos=vector(xpos1,ypos1,zpos1),radius=b1radius,color=color.yellow,make_trail=True,retain=8)
ball2=sphere(pos=vector(xpos2,ypos2,zpos2),radius=b2radius,color=color.magenta,make_trail=True,retain=8)
attach_light(ball1)
attach_light(ball2)

while True:
    rate(30)

    # checking the bouncing conditions
    if xpos1+deltax1+b1radius>=roomlength/2 or xpos1+deltax1-b1radius<=-roomlength/2:
        deltax1=-deltax1
    if ypos1+deltay1+b1radius>=roomheight/2 or ypos1+deltay1-b1radius<=-roomheight/2:
        deltay1=-deltay1
    if zpos1+deltaz1+b1radius>=roomdepth/2 or zpos1+deltaz1-b1radius<=-roomdepth/2:
        deltaz1=-deltaz1
    
    if xpos2+deltax2+b2radius>=roomlength/2 or xpos2+deltax2-b2radius<=-roomlength/2:
        deltax2=-deltax2
    if ypos2+deltay2+b2radius>=roomheight/2 or ypos2+deltay2-b2radius<=-roomheight/2:
        deltay2=-deltay2
    if zpos2+deltaz2+b2radius>=roomdepth/2 or zpos2+deltaz2-b2radius<=-roomdepth/2:
        deltaz2=-deltaz2
    
    if abs(xpos1-xpos2)<=b1radius+b2radius+.4 and abs(ypos1-ypos2)<=b1radius+b2radius+.4 and abs(zpos1-zpos2)<=b1radius+b2radius+.4:
        deltax1=-deltax1
        deltax2=-deltax2
        deltay1=-deltay1
        deltay2=-deltay2
        deltaz1=-deltaz1
        deltaz2=-deltaz2
        winsound.Beep(frequency, duration)
        ball1.color=color.red
        ball2.color=color.red
        time.sleep(.1)

    # incrementing the position of balls in x,y,z axis
    xpos1+=deltax1
    ypos1+=deltay1
    zpos1+=deltaz1

    xpos2+=deltax2
    ypos2+=deltay2
    zpos2+=deltaz2

    # reflecting the changes in the animation
    ball1.pos=vector(xpos1,ypos1,zpos1)
    ball2.pos=vector(xpos2,ypos2,zpos2)
    ball1.color=color.yellow
    ball2.color=color.magenta