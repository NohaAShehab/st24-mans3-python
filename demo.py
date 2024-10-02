class Employee:
    def __init__(self, name, email, salary):
        self.name = name
        self._email = email
        # self.set_salary(salary)
        self.salary = salary  # call property setter while creating object

    @property
    def salary(self):
        return self.__salary

    # setter , getter
    @salary.setter
    def salary(self, salary):
        if isinstance(salary, int) or isinstance(salary, float) and salary > 0:
            self.__salary = salary
        else:
            raise Exception('Salary must be an integer or float greater than 0 ')




emp = Employee('John', '<EMAIL>', 1133)
print("-------------------------")
emp.name='noha'
print(emp.name)


class MM(object):
    pass