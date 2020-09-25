class Stack:
    def __init__(self):
        self.stack=[]
    # function to push an element into stack
    def push(self,value):
        self.stack.append(value)
    # function to pop an element from the stack
    def pop(self):
        self.stack.pop()
    # function to know the peek element/last inserted element in the stack
    def peek(self):
        if self.stack:
            return self.stack[-1]
        else:
            return None
    # function to check whether the stack is empty or not
    def isempty(self):
        if self.stack==[]:
            return True
        return False
    # function to check the size of the stack
    def size(self):
        return len(self.stack)

def main():
    stack=Stack()
    print(f'Is the stack empty : {stack.isempty()}')
    print(f'The size of the stack is {stack.size()}')
    stack.push(1)
    stack.push(2)
    print(f'The peek of the stack is {stack.peek()}')
    print(f'The size of the stack is {stack.size()}')
    stack.pop()
    print(f'The peek of the stack is {stack.peek()}')   
    stack.pop()
    print(f'The peek of the stack is {stack.peek()}')
    stack.pop()
main()

"""
Output-
Is the stack empty : True
The size of the stack is 0
The peek of the stack is 2
The size of the stack is 2
The peek of the stack is 1
The peek of the stack is None
Traceback (most recent call last):
  File "Stack.py", line 38, in <module>
    main()
  File "Stack.py", line 37, in main
    stack.pop()
  File "Stack.py", line 9, in pop
    self.stack.pop()
IndexError: pop from empty list
"""
