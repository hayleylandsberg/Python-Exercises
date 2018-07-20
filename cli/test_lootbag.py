import unittest
from lootbag import LootBag

class TestBagOLoot(unittest.TestCase):

    @classmethod
    def setUpClass(self):
            self.bag = LootBag()
    
    def test_can_list_toys_from_bag_for_child(self):
        expected_result = "ball"
        actual_result = self.bag.list_toys_for_child("Mikey")

        self.assertIn(expected_result, actual_result)

    def test_add_toy_to_bag(self):
        bag = LootBag()
        toy = "ball"
        self.assertEqual(bag.add_toy_to_bag("ball", "Mikey"), "Toy added to bag")

        # toy = "truck"
        # toy_list = bag.list_toys_for_child("Mikey")
        # self.assertNotIn(toy, toy_list)
        # self.bag.add_toy_to_bag("truck", "Mikey")
        # toy_list = bag.list_toys_for_child("Mikey")
        # self.assertIn(toy, toy_list)

if __name__ == "__main__":
    unittest.main()