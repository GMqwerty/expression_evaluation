def infix2postfix(expression):
    associativity = {
        "^": 1,
        "*": 0,
        "/": 0,
        "+": 0,
        "-": 0
    }

    precedence = {
        "^": 4,
        "*": 3,
        "/": 3,
        "+": 2,
        "-": 2
    }

    output = []
    operators = []

    for c in expression:
        if c.isnumeric():
            output.append(c)
        elif c in ["+", "-", "*", "/", "^"]:
            while operators:
                if operators[-1] != "(" and (precedence[operators[-1]] > precedence[c] or (precedence[operators[-1]] == precedence[c] and not associativity[c])):
                    output.append(operators.pop())
                else:
                    break
            operators.append(c)
        elif c == "(" :
            operators.append(c)
        elif c == ")":
            while operators:
                if operators[-1] != "(":
                    output.append(operators.pop())
                else:
                    break
            if operators:
                operators.pop()

    while operators:
        c = operators.pop()
        if c == "(":
            continue
        output.append(c)

    return output

def evaluate_postfix(expression):
    stack = []

    for c in expression:
        if c in ["+", "-", "*", "/", "^"]:
            b = stack.pop()
            a = stack.pop()
            if c == "+":
                result = a+b
            elif c == "-":
                result = a-b
            elif c == "*":
                result = a*b
            elif c == "/":
                result = a/b
            elif c == "^":
                result = pow(a, b)
            stack.append(result)
        else:
            stack.append(int(c))
    return stack[0]
