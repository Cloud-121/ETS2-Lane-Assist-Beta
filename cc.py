#Importing the coolest euro truck sim 2 python api made by the poggest guy
from ets2sdkclient import ets2sdkclient
#Importing the boring stuff
import math
import time
from pynput.keyboard import Key, Controller
#Setting up the coolest trun on stuff
accon = True
debug = False
#Being so cool to give it a e, etc
e = ets2sdkclient()
keyboard = Controller()
keyu = '/'
keyd = '.'
#Being so cool and setting up a while loop
while(True):
    #Updating stuff
    time.sleep(1)
    e.update()
    #Checking to see if he is a cool kid
    if (accon == False):
        continue    #He not a cool kid

    #e.printalll
    limit = int(e.speedLimit * 3.6)
    speed = math.ceil(e.cruiseControlSpeed * 3.6)
    if (debug == True):
        print(limit, speed)
    #Checking to see if we need to do work
    if (e.CruiseControl == False or limit == 0):
        continue    #He not a cool kid
    if (debug == True):
        print("Pass check")
    #Doing the calculations to figure out how many times to move up and down
    diff = limit - speed
    move = int(diff / 5)
    #Doing the (Moving) stuff
    if (move < 0):
        keyboard.press(keyd)
        keyboard.release(keyd)
        move + 1
    if (move > 0 or diff == 4):
        keyboard.press(keyu)
        keyboard.release(keyu)
        move - 1
    #Just writing the debug stuff
    if (debug == True):
        print(diff, move)