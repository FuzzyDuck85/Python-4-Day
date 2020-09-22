from vehicle import *
class Motorbike(Vehicle):
    def __init__(self, number_of_wheels):
        Vehicle.__init__(self, number_of_wheels)
    def start_engine(self):
        vehicle_start = Vehicle.start_engine(self)
        return f"{vehicle_start} (I'm a motorbike), HELL YEAH!"
