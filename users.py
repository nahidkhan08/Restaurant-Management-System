#customer
#employee
#admin

from abc import ABC

class User(ABC):
    def __init__(self, name, phone, email, address):
        self.name=name
        self.phone=phone
        self.email=email
        self.address=address
    
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
    
    

class Restaurant:
    def __init__(self, name):
        self.name=name
        self.employees=[] #this part will work like a database
    
    def add_employee(self, employee):
        self.employees.append(employee)
        print(f'{employee.name} is added!!!')
    
    def view_employee(self):
        print("Employee List:")
        for emp in self.employees:
            print(f'Name: {emp.name}, Phone: {emp.phone}, Email: {emp.email}, Address: {emp.address}')

        

adm = Admin("Rahim", '123456789', 'rahim@gmail.com', 'Dhaka')
restaurant=Restaurant("Road Side Kitchen")
em=Employee('Raj', '12349828', 'raj23@gmail.com', 'Savar', '23', 'Sales', '21000')
adm.add_employee(restaurant,em)


