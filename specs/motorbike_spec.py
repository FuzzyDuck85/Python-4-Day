import unittest
import sys
sys.path.append(".")
sys.path.append("..")
from motorbike import *

class TestMotorbike(unittest.TestCase):
    def setUp(self):
        self.motorbike = Motorbike(2)

    def test_car_has_four_wheels(self):
        self.assertEqual(2, self.motorbike.get_number_of_wheels())

    def test_motorbike_can_start_engine(self):
        self.assertEqual("Vrrmmm (I'm a motorbike), HELL YEAH!", self.motorbike.start_engine())

if __name__ == "__main__":
  unittest.main()
