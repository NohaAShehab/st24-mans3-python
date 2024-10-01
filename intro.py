

# employee = [1, "ahmed", 'os ']
#
# emp = {"id":1, "name":"ahmed", "dept":"os"}
# emp2 =  {"id":2, "empname":"ahmed", "dept":"os"}
#
# def printEmp(emp):
#     print(f'name={emp["name"]}, {emp["dept"]}, id={emp["id"]}')
#

# printEmp(emp)
# printEmp(emp2)
#

"""
    create my own datatype --> customization 
    --> add function printEmp
"""


# to create new datatype

class Employee:
    pass

emp = Employee() # object from the class --> preserve new place in the memory .>>>
### add properties in the runtime the object
print(emp)

# loosely dynamically typed lang.
emp.name='ahmed'
emp.email='<EMAIL>'
emp.salary=100000

print(emp)


emp2= Employee()
emp2.name='ahmed2'
emp2.email='<EMAIL>'
emp2.salary=100000



def printEmp(emp):
    print(f'{emp.name} is {emp.salary}, email is {emp.email}')

printEmp(emp2)
printEmp(emp)


emp3=Employee()
emp3.name='ahmed'
emp3.empemail='<EMAIL>'
emp3.salary=100000

printEmp(emp3)