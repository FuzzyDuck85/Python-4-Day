import unittest
import sys
sys.path.append(".")
sys.path.append("..")
from car import *

class TestCar(unittest.TestCase):
    def setUp(self):
        self.car = Car("Ferrari")

    def test_car_has_model(self):
        self.assertEqual("Ferrari", self.car.get_model())

    def test_car_can_start_engine(self):
      self.assertEqual("Vrrmmm", self.car.start_engine())

    def test_car_has_four_wheels(self):
        self.assertEqual(4, self.car.get_number_of_wheels())


if __name__ == "__main__":
  unittest.main()
