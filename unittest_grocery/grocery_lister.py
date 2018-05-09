class User:
    def __init__(self,ID):
        self.ID = ID
        self.shoppinglists = []

    def add_shoppinglists(self,shoplist):
        if shoplist not in self.shoppinglists:
            self.shoppinglists.append(shoplist)
        else:
            print("item already in list")

    def display_lists(self):
        for shoplist in self.shoppinglists:
            print(shoplist)

class Item:
    def __init__(self,name):
        self.name = name
        self.quantity = 1
        self.unit_price = 0.0
        self.price = 0.0
    def modify_item(self,new_quantity,unit_price):
        self.quantity = new_quantity
        self.unit_price = unit_price
        self.price = self.quantity * self.unit_price


class Shopping_list:
    def __init__(self,title,description):
        self.title = ''
        self.description = ''
        self.items = []

    def add_items(self,item):
        if item not in self.items:
            self.items.append(item)
        else:
            print("item already in list")
