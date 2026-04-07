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
        self.employees=[]
    
    def add_employee(self, name, phone, email, address, age, designation, salary):
        employee= Employee(name, phone, email, address, age, designation, salary)
        self.employees.append(employee)
        print(f'{name} is added!!!')
    
    def view_employee(self):
        print("Employee Information:")
        for emp in self.employees:
            print(f'Name: {emp.name}, Phone: {emp.phone}, Email: {emp.email}, Address: {emp.address}')

adm = Admin("Rahim", '123456789', 'rahim@gmail.com', 'Dhaka')
adm.add_employee('Raj', '12349828', 'raj23@gmail.com', 'Savar', '23', 'Sales', '21000')
adm.view_employee()

