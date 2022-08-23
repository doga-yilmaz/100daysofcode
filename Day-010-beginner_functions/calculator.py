def add (n1,n2):
    return n1 + n2

def subtract (n1,n2):
    return n1 - n2

def multiply (n1,n2):
    return n1 * n2

def divide (n1,n2):
    return n1 / n2

operations = {
    "+": add, 
    "-": subtract,
    "*": multiply,
    "/": divide 
}


def calculation():
    num1 = float(input("What is the first number?:  "))
    for symbol in operations:
            print(symbol)
    end_calculation = False

    while not end_calculation:
        operation_symbol = input("Pick an operation:  ")
        num2 = float(input("What is the next number?:  "))
        calculation_function = operations[operation_symbol]
        answer = round(float(calculation_function(n1=num1, n2=num2)),2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")
        
        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start new calculation.:   ") == "y":
            num1 = answer
        else:
            end_calculation = True
            calculation()
calculation()
