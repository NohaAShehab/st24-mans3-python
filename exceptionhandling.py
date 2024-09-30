

# syntax error --> must be solved then app can start interpretation


# logical error
#
# def sumnum(num1, num2):
#     res = num1 * num2
#     print(res)
#
# sumnum(2,2)
#
# sumnum(3,2)

""" runtime error """
# num1=10
# num2=0
# res = num1/num2  # runtime error 0=> ZeroDivision Error
# print(res)


# print(name) # NameError: name 'name' is not defined

""" runtime error --> unexpected action caused the app to stop """


# ### exception handling.
# try:
#     # print(name)
#     num1 = 10
#     num2= 0
#     res = num1/ num2
#     print(res)
# except:
#     print("---Error happened ")
#
#
#
#



""" raising the exception """


def sumnum(num1: int, num2: int):
    if isinstance(num1, int) and isinstance(num2, int):
        print(num1, num2)
        return num1 + num2

    else:
        raise Exception("num1 and num2 must be integers, plz check and restart")


print(sumnum(4,4))

print(sumnum("rrr",5))

print("---------------------------------")























