"""

Python Coding Exercise: Warehouse
=================================

This module tests the functionality of your warehouse implementation. Run the
tests like this: `python test_warehouse.py`

Your code should be in the file `warehouse.py`, which this module imports.

You may modify this while testing, but your code must pass the tests in the
original version. Only the original, unmodified tests will be used here.

If you implemented the "bonus" problems, you should run
`test_warehouse_bonus.py` instead. That script includes these tests.

"""

import unittest
from warehouse import Item, Warehouse, Shelf, Bin, Box, Bag

#==============================================================================
#
#==============================================================================

class BasicTest(unittest.TestCase):
    """ A set of tests for the basic required functionality.
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


    def test_structure(self):
        """ Test basic ability to place Containers within other Containers.
        """
        # A Warehouse can contain a Shelf
        self.assertTrue(self.warehouse.add(self.shelf))
        self.assertTrue(self.warehouse.contains(self.shelf))

        # Shelves can contain Bins
        self.assertTrue(self.shelf.add(self.bin1))
        self.assertTrue(self.shelf.contains(self.bin1))
        self.assertTrue(self.shelf.add(self.bin2))
        self.assertTrue(self.shelf.contains(self.bin2))

        # Bins can contain Boxes
        self.assertTrue(self.bin1.add(self.box1))
        self.assertTrue(self.bin1.contains(self.box1))
        self.assertTrue(self.bin1.add(self.box2))
        self.assertTrue(self.bin1.contains(self.box2))

        # Boxes can contain Bags
        self.assertTrue(self.box1.add(self.bag1))
        self.assertTrue(self.box1.contains(self.bag1))
        self.assertTrue(self.box1.add(self.bag2))
        self.assertTrue(self.box1.contains(self.bag2))

        # A Shelf "contains" nested Containers within it
        self.assertTrue(self.shelf.contains(self.bin1))
        self.assertTrue(self.shelf.contains(self.box1))
        self.assertTrue(self.shelf.contains(self.box2))
        self.assertTrue(self.shelf.contains(self.bag1))
        self.assertTrue(self.shelf.contains(self.bag2))
        self.assertFalse(self.shelf.contains(self.box3))


    def test_contents(self):
        """ Test the ability to add Items to Containers and find their
            contents.
        """
        # Reuse the work done by `test_structure()` to set up hierarchy
        self.test_structure()

        # Bins and Boxes can contain Items
        self.assertTrue(self.bin2.add(self.itemS1))
        self.assertTrue(self.bin2.contains(self.itemS1))
        self.assertTrue(self.box1.add(self.itemS2))
        self.assertTrue(self.box1.contains(self.itemS2))

        # Containers "contain" Items in nested Containers within them
        self.assertTrue(self.bin1.contains(self.itemS2))
        self.assertTrue(self.shelf.contains(self.itemS1))
        self.assertTrue(self.shelf.contains(self.itemS2))


    def test_limits(self):
        """ Test capacity limits.
        """
        # Containers can only hold smaller Containers, not the same or larger.
        # Bins cannot contain Bins
        self.assertFalse(self.bin1.add(self.bin3))
        self.assertFalse(self.bin1.contains(self.bin3))

        # Boxes cannot contain Boxes
        self.assertFalse(self.box1.add(self.box3))
        self.assertFalse(self.box1.contains(self.box3))

        # Bags cannot contain Bags
        self.assertFalse(self.bag1.add(self.bag3))
        self.assertFalse(self.bag1.contains(self.bag3))

        # Containers cannot contain Items that are too large
        self.assertFalse(self.bag1.add(self.itemM1))
        self.assertFalse(self.bag1.contains(self.itemM1))
        self.assertFalse(self.box1.add(self.itemL1))
        self.assertFalse(self.box1.contains(self.itemL1))
        self.assertFalse(self.bin1.add(self.itemXL1))
        self.assertFalse(self.bin1.contains(self.itemXL1))

        # bin1 should be empty now, otherwie the next assertions will fail
        self.assertEqual(len(self.bin1), 0)

        # Bins can't fit more than two Boxes
        self.assertTrue(self.bin1.add(self.box1))
        self.assertTrue(self.bin1.add(self.box2))
        self.assertFalse(self.bin1.add(self.box3))
        self.assertFalse(self.bin1.contains(self.box3))


    def test_remove(self):
        """ Test item removal.
        """
        # Add some items to remove.
        self.assertTrue(self.box1.add(self.itemS1))
        self.assertTrue(self.box1.add(self.itemS2))
        self.assertTrue(self.box1.add(self.itemS3))

        # Test removal mode 1: no arguments, removes last added object.
        self.assertIs(self.box1.remove(), self.itemS3)
        self.assertFalse(self.box1.contains(self.itemS3))

        # Test removal mode 2: removing a specific object.
        self.assertIs(self.box1.remove(self.itemS1), self.itemS1)
        self.assertFalse(self.box1.contains(self.itemS1))

        # Check that itemS2 is still there.
        self.assertTrue(self.box1.contains(self.itemS2))


    def test_pack(self):
        """ Test the `pack()` method (puts an object in the first nested
            container with space for it).
        """
        # An oddly-sized, space-filling Item
        fillerItem = Item(5)

        # Add a Box to a Bin; make the Bin too full to add another Item
        self.assertTrue(self.bin1.add(self.box1))
        self.assertTrue(self.bin1.add(fillerItem))

        # self.itemS1 should get packed into the Box inside the Bin
        self.assertTrue(self.bin1.pack(self.itemS1))
        self.assertTrue(self.box1.contains(self.itemS1))


#==============================================================================
#
#==============================================================================

if __name__ == "__main__":
    unittest.main()
