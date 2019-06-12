from java import *
from dmc import Client
from dmc import telemetry

class pythontoserver_class():

    def __init__(self):
     client = Client("5cffd8f8cd98120001a2802d", "12345")
     client.spin()

    def position(self,latitude,longitude):
     pos = telemetry.Position(lat=latitude, lng=longitude)
     client.send_telemetry(pos)