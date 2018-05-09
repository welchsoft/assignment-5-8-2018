import unittest
from grocery_lister import *
class TestGrocery(unittest.TestCase):

    def setUp(self):
        self.shoppinglist = Shopping_list('walmart','butts')
        self.user = User(12345)
        self.item = Item('milk')

    def test_add_items(self):
        list = ['stuff','things','junk','things']
        list_no_dupes = ['stuff','things','junk']
        for item in list:
            self.shoppinglist.add_items(item)
        self.assertEqual(self.shoppinglist.items,list_no_dupes)

    def test_add_shoppinglists(self):
        storelist = ['walmart', 'hmart','korean suppy', 'walmart']
        storelist_no_dupes = ['walmart', 'hmart','korean suppy']
        for store in storelist:
            self.user.add_shoppinglists(store)
        self.assertEqual(self.user.shoppinglists,storelist_no_dupes)

    def test_quantity(self):
        self.assertEqual(self.item.quantity,1)

    def test_modify_item(self):
        self.item.modify_item(2,5)
        self.assertEqual(self.item.quantity,2)
        self.assertEqual(self.item.price,10.0)

    def test_display_lists(self):
        self.user.display_lists()

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
