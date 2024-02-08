class EmployeeClass:

    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    def displayEmployee(self):
        print("Employee id is {} , salary is {} , and name is {} ".format(self.emp_id, self.salary, self.name))


obj = EmployeeClass("12", "shabana", "200")
obj.displayEmployee()
