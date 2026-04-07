#customer
#employee
#admin

from abc import ABC
from order import Order
class User(ABC):
    def __init__(self, name, phone, email, address):
        self.name=name
        self.phone=phone
        self.email=email
        self.address=address

class Customer(User):
    def __init__(self, name, phone, email, address):
        super().__init__(name, phone, email, address)
        self.cart= Order()
    
    def view_menu(self, restaurant):
        restaurant.menu.show_food()
    
    def add_to_cart(self, restaurant, order_item, quantity):
        item=restaurant.menu.find_item(order_item)
        if item:
            if quantity > item.quantity:
                print("Item quantity exceeded.")
            else:
                item.quantity=quantity
                self.cart.add_item(item)
                print("Item is added")
        else:
            print("Item is not found")

    def show_cart(self):
        print("*****View Cart*****")
        print("Food Name\tPrice\tQuantity")
        for item,quantity in self.cart.items.items():
            print(f'{item.name}\t\t{item.price}\t{quantity}')
        print(f'Total price: {self.cart.total_price}')
    
    def pay_bill(self):
        print(f'Your {self.cart.total_price} Taka bill is paid')
        self.cart.clear()


class Employee(User):
    def __init__(self, name, phone, email, address, age, designation, salary):
        super().__init__(name, phone, email, address)
        self.age=age
        self.designation=designation
        self.salary=salary

class Admin(User):
    def __init__(self, name, phone,email, address):
        super().__init__(name, phone, email, address)
    
    def add_employee(self, restaurant, employee):
        restaurant.add_employee(employee)
    
    def view_employee(self, restaurant):
        restaurant.view_employee()
    
    def add_new_item(self, restaurant, item):
        restaurant.menu.add_item(item)
    
    def delete_item(self, restaurant,item):
        restaurant.menu.remove_item(item)
    
    def show_item(self, restaurant):
        restaurant.menu.show_food()
    
    
       

# adm = Admin("Rahim", '123456789', 'rahim@gmail.com', 'Dhaka')
# restaurant=Restaurant("Road Side Kitchen")
# em=Employee('Raj', '12349828', 'raj23@gmail.com', 'Savar', '23', 'Sales', '21000')
# adm.add_employee(restaurant,em)

# fditem=FoodItem('Pizza', 545, 4)
# fditem2=FoodItem('Pizza', 545, 4)
# fditem3=FoodItem('Burger', 325, 4)
# menu=Menu()
# menu.add_item(fditem)
# menu.add_item(fditem2)
# menu.add_item(fditem3)
# menu.show_food()

# fditem=FoodItem('Pizza', 545, 4)
# fditem2=FoodItem('Burger', 320, 7)
# fditem3=FoodItem('Pasta', 120, 12)
# restaurant=Restaurant("Road Side Kitchen")
# adm = Admin("Rahim", '123456789', 'rahim@gmail.com', 'Dhaka')
# adm.add_new_item(restaurant,fditem)
# adm.add_new_item(restaurant,fditem2)
# adm.add_new_item(restaurant,fditem3)
# adm.show_item(restaurant)

# customer1=Customer("Nahid", '0135272782', 'nahid@gmail.com', 'Dhaka')
# customer1.view_menu(restaurant)

# food_item=input("Enter Food Item: ")
# food_quantity=int(input("Enter Food Quantity: "))
# customer1.add_to_cart(restaurant, food_item, food_quantity)
# customer1.show_cart()



