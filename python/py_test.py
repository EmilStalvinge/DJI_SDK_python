from Demoking.subbe import DemoPrint
from java import *
from dmc import Client


class py_class():

    def __init__(self, name):
     print(name)

    def py_return1(self,name):
     jocka= DemoPrint.demoprint(4)
     jockaking = jocka+1
     print(jockaking)
     print(name)
     client = Client("5cffd8f8cd98120001a2802d", "12345")
     client.spin()

    def py_return2(self,name):
     print(name)

    @property
    def py_return3(self):
     return 5


