from food_item import FoodItem
from menu import Menu
from users import Admin, Customer, Employee
from order import Order
from restaurant import Restaurant

restaurant=Restaurant("Mamar Hotel")

def customer_menu():
    name=input("Enter your Name: ")
    phone=input("Enter your phone Number: ")
    email=input("Enter your email account: ")
    address=input("Enter your Address: ")

    customer=Customer(name, phone, email, address)

    while True:
        print(f'Welcome {customer.name}!!!')
        print("1. View Menu")
        print("2. Add item to cart")
        print("3. View Cart")
        print("4. Pay Bill")
        print("5. Exit")

        choice=int(input("Enter your choice: "))
        if choice==1:
            customer.view_menu(restaurant)
        
        elif choice==2:
            item_name=input("Enter item name: ")
            item_quantity=int(input("Enter item quantity: "))
            customer.add_to_cart(restaurant, item_name, item_quantity)
        elif choice==3:
            customer.show_cart()
        elif choice==4:
            customer.pay_bill()
        elif choice==5:
            break
        else:
            print("Invalid Input!!!, Enter Valid Choice")
    
