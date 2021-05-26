def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def is_operator(s):
    return s == '*' or s == '/' or s == '+' or s == '-' or s == '^'

def is_exponent(c):
    return c == '^'

def is_opening_parantheses(s):
    return s == '(' or s == '[' or s == '{'

def is_closing_parantheses(s):
    return s == ')' or s == ']' or s == '}'

def get_operator_priority(operator):
    if operator == '+' or operator == '-':
        return 1
    elif operator == '*' or operator == '/':
        return 2
    elif operator == '^':
        return 3

def has_higher_priority(operator1, operator2):
    op1_priority = get_operator_priority(operator1)
    op2_priority = get_operator_priority(operator2)
    if (op1_priority == op2_priority):
        # return false if operator 1 is exponent (Right Associative)
        return not is_exponent(operator1)
    return op1_priority > op2_priority

def add_spacing_to_expression(exp):
    # Used as preprocessing before splitting the string into list for easier processing of multi-digit numb ers
    # Not the most elegant or efficient solution
    return exp.replace('(', ' ( ').replace(')', ' ) ').replace('*', ' * ').replace('/', ' / ').replace('+', ' + ').replace('-', ' - ').replace('^', ' ^ ')


def convertInfixToPostfix(exp):
    exp = add_spacing_to_expression(exp)
    exp_list = exp.split()
    res = []
    stack = []
    for x in exp_list:
        #print(stack)
        if is_number(x):
            res.append(float(x))
        elif is_operator(x):
            while len(stack) > 0 and stack[-1] != '(' and has_higher_priority(stack[-1], x):
                res.append(stack.pop())
            stack.append(x)
        elif x == '(':
            stack.append(x)
        elif x == ')':
            while len(stack) > 0 and stack[-1] != '(':
                res.append(stack.pop())
            stack.pop()
    while len(stack) > 0:
        res.append(stack.pop())
    return res

exp = '(10+2-5) * (15 / 3) ^ 2 ^ 2'
# should output postfix as '10.0 2.0 + 5.0 - 15.0 3.0 / 2.0 2.0 ^ ^ *' and evaluate to 4375

postfix = convertInfixToPostfix(exp)

[print(ch, end = ' ') for ch in postfix]
