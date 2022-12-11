#importing file
from ets2sdkclient import ets2sdkclient
#Stuff For Speed Limit And Cruise
import math
#Giving it cool names
e = ets2sdkclient()
#Updating the values
e.update()
#v < Use this to print all 
#e.printalll()

#Setting the values
limit = int(e.speedLimit * 3.6)
speed = math.ceil(e.cruiseControlSpeed * 3.6)
#Printing
print(limit)
print(speed)