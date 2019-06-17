from java import *
from dmc import Client
from dmc import telemetry
from dmc import mission
import threading
import logging
logger = logging.getLogger("communication")


class pythontoserver_class():

    client = Client("5cffd8f8cd98120001a2802d", "12345")
    def __init__(self):
        self.client = Client("5cffd8f8cd98120001a2802d", "12345")

    def position(self,latitude,longitude):
        pos = telemetry.Position(lat=latitude, lng=longitude)
        self.client.send_telemetry(pos)
        print("POS SENT")


    def velocity_callback(self, xd, yd,zd):

        vel = telemetry.Velocity(linear=(xd,yd,zd))
        self.client.send_telemetry(vel)
        print("VEL SENT")


    def battery_callback(self, volt, cur,psu,per):

        bat = telemetry.Battery(voltage=volt, current=cur,psu_status=psu, percentage=per)
        self.client.send_telemetry(bat)
        print("BAT SENT")


    def home_callback(self,lat,lng,alt):
        sethome = mission.Home(lat=lat, lng=lng,alt=alt)
        self.client.set_home(sethome)

    def spin(self):
        print("start SPIN")
        self.client.spin()
        print("end")

    def main(self):
        print("Main Started")
        t = threading.Thread(target = self.spin)
        t.daemon = True # helpful if you want it to die automatically
        t.start()
        self.client.on("set_mission", self.on_set_mission)
        print("Main End")

    def on_set_mission(self, msg):
        wps = msg.waypoints
        print(wps[2].lat)


