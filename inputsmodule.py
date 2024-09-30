# print("------------------customized inputs module--------------------------")

def askforInt(message='please enter a number'):
    while True:
        num = input(message)
        if num.isdigit():
            num=int(num)

            return num
        print('please enter a valid number')



def askforString(message='please enter a string'):
    while True:
        instring = input(message)
        if instring.isalpha():
            return instring
        print('please enter a valid string')



if __name__ == '__main__':
    # this code will run only if the inputsmodule is run
    print("--- customized input module ----")