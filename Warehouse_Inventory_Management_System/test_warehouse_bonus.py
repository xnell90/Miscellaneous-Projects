"""
Python Coding Exercise: Warehouse (Bonus Tests)
===============================================

This module tests the functionality of your warehouse implementation, including
the two "bonus" problems. Run the tests like this: `python test_warehouse.py`

Your code should be in the file `warehouse.py`, which this module imports.

This also runs the "basic" tests in `test_warehouse.py`.

You may modify this while testing, but your code must pass the tests in the
original version. Only the original, unmodified tests will be used here.
"""

import unittest
from warehouse import Item, Warehouse, Shelf, Bin, Box, Bag

#==============================================================================
#
#==============================================================================

# Perform the basic tests
from test_warehouse import *


class BonusTest(unittest.TestCase):
    """ Test the "bonus" functionality.
    """

    def setUp(self):
        """ Create some objects: one Warehouse, one Shelf, three of each
            Container type (Bin, Box, Bag), and three each of four different
            sizes of Item.
        """
        self.warehouse = Warehouse()
        self.shelf = Shelf()
        self.bin1, self.bin2, self.bin3 = [Bin() for _ in range(3)]
        self.box1, self.box2, self.box3 = [Box() for _ in range(3)]
        self.bag1, self.bag2, self.bag3 = [Bag() for _ in range(3)]

        self.itemS1, self.itemS2, self.itemS3 = [Item(1) for _ in range(3)]
        self.itemM1, self.itemM2, self.itemM3 = [Item(6) for _ in range(3)]
        self.itemL1, self.itemL2, self.itemL3 = [Item(10) for _ in range(3)]
        self.itemXL1, self.itemXL2, self.itemXL3 = [Item(15) for _ in range(3)]


    def test_shelfConstraint(self):
        """ Bonus 1: Test that a Shelf can only contain Items larger than 7
            volume units. Containers smaller than 7 units are allowed.
        """
        # Shelves can contain Containers smaller than 7 units, but not Items.
        self.assertTrue(self.shelf.add(self.bag1))

        # Shelves cannot contain items smaller than 7 units.
        self.assertTrue(self.shelf.add(self.itemXL1))
        self.assertTrue(self.shelf.add(self.itemL1))
        self.assertFalse(self.shelf.add(self.itemM1))
        self.assertFalse(self.shelf.add(self.itemS1))

        # Shelves can contain Containers with smaller Items.
        self.assertTrue(self.bin1.add(self.itemS1))
        self.assertTrue(self.shelf.add(self.bin1))


    def test_exclusivity(self):
        """ Bonus 2: Test that moving an Item from one Container to another
            automatically removes it from the first Container.
        """
        self.assertTrue(self.bin1.add(self.itemS1))
        self.assertTrue(self.bin1.contains(self.itemS1))
        self.assertFalse(self.bin2.contains(self.itemS1))

        self.assertTrue(self.bin2.add(self.itemS1))
        self.assertTrue(self.bin2.contains(self.itemS1))
        self.assertFalse(self.bin1.contains(self.itemS1))


    def test_extract(self):
        """ Bonus 3: Test the `extract()` method, which removes an item from
            a Container or any Container within it.
        """
        self.assertTrue(self.warehouse.add(self.shelf))
        self.assertTrue(self.shelf.add(self.bin1))
        self.assertTrue(self.bin1.add(self.box1))
        self.assertTrue(self.box1.add(self.bag1))

        self.assertTrue(self.bag1.add(self.itemS1))
        self.assertTrue(self.bag1.add(self.itemS2))

        self.assertIsNotNone(self.bag1.extract(self.itemS1))
        self.assertIsNotNone(self.warehouse.extract(self.itemS2))

        # Make sure they've actually been removed
        self.assertIsNone(self.bag1.extract(self.itemS1))
        self.assertIsNone(self.warehouse.extract(self.itemS2))


if __name__ == "__main__":
    unittest.main()
