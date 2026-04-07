class Menu:
    def __init__(self):
        self.items=[]
    
    def find_item(self, new_item):
        for item in self.items:
            if item.name.lower()==new_item.lower():
                return item
        return False
    
    def add_item(self, item):
        itm=self.find_item(item.name)
        if itm:
            itm.quantity+=item.quantity
            print(f'Added {item.name}\'s quantity !!!')
        else:
            self.items.append(item)
            print(f'{item.name} is added!!!')

    def remove_item(self, item):
        found=self.find_item(item)
        if found:
            self.items.remove(found)
            print("Item is deleted")
        else:
            print("Item is not found") 

    def show_food(self):
        print("*************Menu List****************")
        print("Food Name\tPrice\tQuantity")
        for item in self.items:
            print(f'{item.name}\t\t{item.price}\t{item.quantity}') 