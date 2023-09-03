class Employee:
    employee_id = 1

    def __init__(self, name):
        self.name = name
        self.emp_id = Employee.employee_id
        Employee.employee_id += 1

    def set_data(self, name):
        self.name = name
        self.emp_id = Employee.employee_id
        Employee.employee_id += 1

    def put_data(self):
        print(f'Employee name: {self.name}. ID: {self.emp_id}')


obj1 = Employee("Armen")
obj2 = Employee('Gor')
obj3 = Employee('Davit')

for i in (obj1, obj2, obj3):
    i.put_data()
