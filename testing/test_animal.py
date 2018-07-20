import unittest
#import sys
# sys.path.append('../')
from animal import Animal
from animal import Dog


class TestAnimal(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.bob = Dog("Bob")

    def test_animal_creation(self):

        bob = Dog("Bob")
        #could also put = self.bob

        self.assertIsInstance(bob, Dog)
        self.assertIsInstance(bob, Animal)

    def test_animal_can_set_legs(self):
        self.bob.set_legs(6)
        self.assertEqual(self.bob.legs, 6)

    def test_animal_walk(self):
        self.bob.set_legs(4)
        self.bob.walk()
        self.assertEqual(self.bob.speed, .8)
    
    def test_animal_species(self):
        self.bob.set_species("basically human")
        self.assertIs(self.bob.species, "basically human")

        
if __name__=='__main__':
    unittest.main()