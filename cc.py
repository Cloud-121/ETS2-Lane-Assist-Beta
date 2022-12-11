#Loading
import settingsInterface as settings
import time
import truck_telemetry

#Settings

#Realcode
#while(acc = settings.GetSettings("Experimentalsettings", "acc")):
truck_telemetry.init()
data = truck_telemetry.get_data()
speed = data["speed"]
print(speed)


