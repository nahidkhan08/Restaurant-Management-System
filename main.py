from food_item import FoodItem
from menu import Menu
from users import Admin, Customer, Employee
from order import Order
from restaurant import Restaurant
from admin_main_menu import admin_menu
from customer_main_menu import customer_menu

restaurant=Restaurant("Mamar Hotel")

while True:
    print(f'Welcome to {restaurant.name}!!!')
    print("1. Customer")
    print("2. Admin")
    print("3. Exit")

    choice=int(input("Enter your choice: "))
    if choice == 1:
        customer_menu()
    elif choice == 2:
        admin_menu()
    elif choice == 3:
        break
    else: 
        print("Invalid Input")