# Object Orientated Programming
from vehicle import *
class Car(Vehicle):
    def __init__(self, model):
        Vehicle.__init__(self, 4)
        self.model = model

    def get_model(self):
        return self.model
#     def __init__(self, make, model, top_speed):
#         self.make = make
#         self.model = model
#         self.top_speed = top_speed
#
#     def start_engine(self):
#         return "Brmmmm brm!"
#
# new_car = Car("Ford", "Focus", 130)
# print("The " + new_car.make + " " + new_car.model + " can travel at a top speed of " + str(new_car.top_speed) + " mph!")
# print(new_car.start_engine())
