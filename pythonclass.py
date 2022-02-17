class Employee():
    num_of_emp = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.fname = first
        self.lname = last
        self.wage = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_emp += 1

    def fullName(self):
        return '{} {}'.format(self.fname, self.lname)

    def apply_raise(self):
        self.pay = int(self.wage * self.raise_amount)
        return '{}'.format(self.pay)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

emp_1 = Employee('Corey', 'Dicks', 5000)
emp_2 = Employee('Test', 'User', 5040)
emp_2.raise_amount = 1.05
# print(Employee.fullName(emp_1))
# print(emp_2.fullName())
# print(Employee.num_of_emp)
print(emp_1.fname, emp_1.lname, emp_1.wage, emp_1.email)
