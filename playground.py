"""
    any .py file --> is called python module
    any folder contains set of modules --> python package

"""
""" 1- first method """
# import inputsmodule


# def calculator():
#     num1 = inputsmodule.askforInt('Please enter a number')
#     num2 = inputsmodule.askforInt('Please enter a number')
#     res = num1 + num2
#     print(res)
#
#
#
# calculator()

""" 2- second method """
# from inputsmodule import askforInt
#
# def calculator():
#     num1 = askforInt('Please enter a number')
#     num2 = askforInt('Please enter a number')
#     res = num1 + num2
#     print(res)
#
# calculator()


""" check this ?? """
# import  inputsmodule

# from inputsmodule import  askforString


""" import module from package """

" 1-import module"

# import iti.greeting

# iti.greeting.say_hello()

"2- import part of the module "
# from iti.greeting import say_goodbye
# say_goodbye("ahmed")

"3--- package with __init__.py "

# import  training
# training.sumnum(3,4)

#
# from training import sumnum
# sumnum(34,4)


# from training.mathmodule import mulnum
# print(mulnum(44,4))


from training import  mulnum
print(mulnum(5,4))









