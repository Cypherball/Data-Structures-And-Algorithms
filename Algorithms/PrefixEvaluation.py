def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def is_operator(s):
    return s == '*' or s == '/' or s == '+' or s == '-' or s == '^'

def evaluate(operator, op1, op2):
    if operator == '*':
        return op1 * op2
    elif operator == '/':
        return op1 / op2
    elif operator == '+':
        return op1 + op2
    elif operator == '-':
        return op1 - op2
    elif operator == '^':
        return op1 ** op2

def evaluate_prefix(exp):
    stack = []
    exp_list = exp.split()
    for i in range(len(exp_list) - 1, -1, -1):
        if is_number(exp_list[i]):
            stack.append(float(exp_list[i]))
        elif is_operator(exp_list[i]):
            op1 = stack.pop()
            op2 = stack.pop()
            res = evaluate(exp_list[i], op1, op2)
            stack.append(res)

    return stack.pop()

exp = '- + * 24 3 * 5 4 9'

print(evaluate_prefix(exp))