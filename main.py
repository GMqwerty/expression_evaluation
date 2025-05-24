from postfix import *

expression = input("Expression: ")
tokens = []
is_number = False
number_start = 0
for i, c in enumerate(expression):
    if not c.isdigit():
        if is_number:
            tokens.append(expression[number_start:i])
        is_number = False
        if not c.isspace():
            tokens.append(c)
    elif c.isdigit():
        if is_number:
            continue
        else:
            is_number = True
            number_start = i
if is_number:
    tokens.append(expression[number_start:])
print(tokens)
postfix_expression = infix2postfix(tokens)
print(postfix_expression)
evaluate_postfix(postfix_expression)
print(value)