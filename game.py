from random import choice
import pgzrun

#SHINee Game

import pgzrun

c = ["jjong", "key", "minho", "onew", "taemin"]

minho  = Actor(choice(c))
minho.topright = 0, 10
 
WIDTH = 500
HEIGHT = minho.height + 20
 
 
def draw():
    screen.clear()
    minho.draw()
 
 
def update():
    minho.left += 2
    if minho.left > WIDTH:
        minho.right = 0
 
pgzrun.go()
