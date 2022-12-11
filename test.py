from ets2sdkclient import ets2sdkclient
import math
import time
e = ets2sdkclient()
while(True):
    time.sleep(1)
    e.update()
    #e.printalll()
    limit = int(e.speedLimit * 3.6)
    speed = math.ceil(e.cruiseControlSpeed * 3.6)
    print(e.BlinkerLeftActive, limit, speed, e.BlinkerRightActive)