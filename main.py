def add(n1, n2):
    return n1 + n2


def substract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def devide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": devide
}


def calculator():
    num1 = float(input("Welcome to calculator, you can do math here! Insert your first number: "))
    for operation in operations:
        print(operation)
    operation_symbol = input("Which one of these functions do you want to provide? ")
    num2 = float(input("What is the second number? "))

    answer = operations[operation_symbol](num1, num2)

    print(f"{num1} {operation_symbol} {num2} = {answer}")
    pokracovat = input("Do you want to continue with your result? (yes/no) ")

    while pokracovat == "yes":
        operation_symbol = input("Pick another operation: ")
        num3 = float(input("Choose another number : "))
        calculation_function = operations[operation_symbol]
        second_answer = calculation_function(answer, num3)
        print(second_answer)
        pokracovat = input("Do you want to continue ? ")
        if pokracovat == "yes":
            answer = second_answer
    else:
        print("Bye")


calculator()
calculator()