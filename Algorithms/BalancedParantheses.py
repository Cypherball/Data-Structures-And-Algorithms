def is_opening_parantheses(ch):
    return ch == '(' or ch == '[' or ch == '{'

def is_balanced(exp):
    balancer = []
    for x in exp:
        if is_opening_parantheses(x):
            balancer.append(x)
        elif x == ')':
            if len(balancer) > 0 and balancer[-1] == '(':
                balancer.pop()
            else: return False
        elif x == ']':
            if len(balancer) > 0 and balancer[-1] == '[':
                balancer.pop()
            else: return False
        elif x == '}':
            if len(balancer) > 0 and balancer[-1] == '{':
                balancer.pop()
            else: return False
    return True

test = '{a+b}[c*(x/y*{a-b})]'

if is_balanced(test):
    print('Parantheses are balanced.')
else:
    print('Parantheses are NOT balanced.')