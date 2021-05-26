def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def is_operator(s):
    return s == '*' or s == '/' or s == '+' or s == '-' or s == '^'

def evaluate(op1, op2, operator):
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

def evaluate_postfix(exp):
    stack = []
    exp_list = exp.split()
    for x in exp_list:
        if is_number(x):
            stack.append(float(x))
        elif is_operator(x):
            op2 = stack.pop()
            op1 = stack.pop()
            res = evaluate(op1, op2, x)
            stack.append(res)

    return stack.pop()

exp = '24 3 * 5 4 * + 9 -'
exp2 = '10.0 2.0 + 5.0 - 15.0 3.0 / 2.0 2.0 ^ ^ *'

print(evaluate_postfix(exp2))