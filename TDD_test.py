import unittest
import sys, os
from builder import *

sys.path.append(os.getcwd())

class Technic_Builder_Test(unittest.TestCase):
    director = Director()
    builder = Technic_Builder()
    director.builder = builder
    def test_Mvideo(self):
       print("\nМ.Видео: ")
       self.director.Mvideo()
       self.builder.product.list_parts()

    def test_DNS(self):
        print("\nDNS: ")
        self.director.DNS()
        self.builder.product.list_parts()

if __name__ == "__main__":
    unittest.main()