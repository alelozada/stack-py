from inspect import stack
from stacks import Stack

stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)
stack.push('A')
stack.push('B')
stack.push('C')

print(stack.top())
print(stack.bottom())

print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())

print(stack.top())
print(stack.bottom())