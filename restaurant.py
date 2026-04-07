class Restaurant:
    def __init__(self, name):
        self.name=name
        self.employees=[] #this part will work like a database
        self.menu=Menu()
    
    def add_employee(self, employee):
        self.employees.append(employee)
        print(f'{employee.name} is added!!!')
    
    def view_employee(self):
        print("Employee List:")
        for emp in self.employees:
            print(f'Name: {emp.name}, Phone: {emp.phone}, Email: {emp.email}, Address: {emp.address}')