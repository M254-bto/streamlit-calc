def calculate(operator, x, y):
    if operator == "Add":
        return x + y
    elif operator == "Subtract":
        if x>y:
            return x - y
        elif y>x:
            return y - x
    if operator == "Multiply":
        return y*x
    if operator == "Divide":
        return x / y

