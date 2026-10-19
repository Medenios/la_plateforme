def calcule(num1, operator, num2):
    match operator:
        case "+":
            return num1 + num2
        case "-":
            return num1 - num2
        case "*":
            return num1 * num2
        case _:
            return num1 / num2


print(calcule(1, "*", 3))
