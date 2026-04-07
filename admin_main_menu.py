from food_item import FoodItem
from menu import Menu
from users import Admin, Customer, Employee
from order import Order
from restaurant import Restaurant

restaurant=Restaurant("Mamar Hotel")

def admin_menu():
    name=input("Enter your Name: ")
    phone=input("Enter your phone Number: ")
    email=input("Enter your email account: ")
    address=input("Enter your Address: ")

    admin=Admin(name, phone, email, address)

    while True:
        print(f'Welcome {admin.name}!!!')
        print("1. Add New Item")
        print("2. Add New Employee")
        print("3. View Employee")
        print("4. View Item")
        print("5. Delete Item")
        print("6. Exit")

        choice=int(input("Enter your choice: "))
        if choice==1:
            item_name=input("Enter Item Name: ")
            item_price=int(input("Enter Item Price: "))
            item_quantity=int(input("Enter Item Quantity: "))
            item=FoodItem(item_name, item_price, item_quantity)
            admin.add_new_item(restaurant,item)
        
        elif choice==2:
            name=input("Enter employee name: ")
            phone=input("Enter employee phone number: ")
            email=input("Enter employee email: ")
            address=input("Enter employee address: ")
            age=input("Enter employee age: ")
            designation=input("Enter employee designation: ")
            salary=input("Enter employee salary: ")
            employee=Employee(name, phone, email, address, age, designation, salary)
            admin.add_employee(restaurant, employee)

        elif choice==3:
            admin.view_employee(restaurant)
        elif choice==4:
            admin.show_item(restaurant)
        elif choice==5:
            item_name=input("Which Item you want to delete?")
            admin.delete_item(restaurant,item_name)
        elif choice==6:
            break
        else:
            print("Invalid Input!!!, Enter Valid Choice")
