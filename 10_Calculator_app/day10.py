from art import logo

def add(a, b):
    return a + b

def substract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b


operations = {
    "+" : add,
    "-" : substract,
    "*" : multiply,
    "/" : divide
}

def calculator():
    print(logo)

    num1 = float(input("What's the first number?: "))
    for oper in operations:
        print(oper)
    shoudl_continue = True

    while shoudl_continue:
        oper_symbol = input("Pick an operation from the line above: ")
        num2 = float(input("What's the second number?: "))

        if oper_symbol in operations:
            calc_function = operations[oper_symbol]
            answer = calc_function(num1, num2)
            print(f"{num1} {oper_symbol} {num2} = {answer}")
        else:
            print("Wrong operation entered")

        continue_oper = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit: ")
        if continue_oper == "y":
            num1 = answer
        else:
            shoudl_continue = False
            calculator()

calculator()