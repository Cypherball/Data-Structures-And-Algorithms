# LIFO / FILO

class Stack:
    def __init__(self, size=100):
        if size < 1: size = 1
        self._stack = [None]*size
        self.top = -1
    
    def push(self, value):
        if self.top + 1 >= len(self._stack): return print('Stack Overflow!')
        self.top += 1 
        self._stack[self.top] = value
        return self._stack[self.top]

    def pop(self):
        if self.is_empty(): return None
        el = self._stack[self.top]
        self._stack[self.top] = None
        self.top -= 1
        return el
    
    def peek(self):
        if self.is_empty(): return None
        return self._stack[self.top]
        
    def is_empty(self):
        return self.top < 0

    def print_stack(self):
        if self.is_empty(): return print('Empty Stack!')
        for i in range(self.top, -1, -1):
            print(self._stack[i], end=' ')
        print()

stack = Stack(3)
stack.pop()
stack.print_stack()
stack.push(5)
stack.push(9)
stack.push(12)
stack.push(25)
stack.pop()
stack.print_stack()

#------REVERSE STRING USING STACK------#
print('\n\n-----REVERSING STRING-----\n')

string = 'Hello World'
print('String: ' + string)

string_stack = Stack()
for x in string:
    string_stack.push(x)

reversed = ''
while not string_stack.is_empty():
    reversed += string_stack.pop()

print('Reversed: ' + reversed)


#------BALANCED PARANTHESES USING STACK------#
print('\n\n-----BALANCED PARANTHESES USING STACK-----\n')

test1 = '{a+b}[c*(x/y*{a-b})]'

balancer = Stack()
balanced = True
for x in test1:
    if x == '(' or x == '[' or x == '{':
        balancer.push(x)
        #balancer.print_stack()
    elif x == ')':
        if balancer.peek() == '(':
            balancer.pop()
        else:
            balanced = False
            break
    elif x == ']':
        if balancer.peek() == '[':
            balancer.pop()
        else: 
            balanced = False
            break
    elif x == '}':
        if balancer.peek() == '{':
            balancer.pop()
        else:
            balanced = False
            break

if balanced and balancer.is_empty():
    print('Parantheses are balanced.')
else:
    print('Parantheses are NOT balanced.')
