class node:
    def __init__(self,value=0,prev=None):
        self.value=value
        self.prev=prev
class stack(node):
    def __init__(self):
        self.length=0
        self.top=node()
    # function to push an element at the top of the stack
    def push(self,value):
        self.length+=1
        tempnode=node(value,self.top)
        self.top=tempnode
    # function to pop an element from the stack
    def pop(self):
        if self.length==0:
            print('error:Stack underflow')
        else:
            self.top=self.top.prev
            self.length-=1
    # function to get the size of the stack
    def Size(self):
        return self.length
    # function to check if the stack is empty or not
    def Isempty(self):
        if self.length==0:
            return True
        else:
            return False
    # function to get the peek or top most element of the stack
    def peek(self):
        if self.length==0:
            print('error: Stack underflow')
        else:
            return self.top.value
    # function to delete the stack 
    def delete(self):
        self.top=None
        print('You successfully deleted the stack.')
        self.length=0

def main():
    n=int(input('Enter the no. of elements to push : '))
    my_stack=stack()
    print('Enter the elements to push')
    for i in range(1,n+1):
        my_stack.push(input(f'{i}) '))
    for i in range(1,n+1):
        print(f'{i}) ',end='')
        print(f'The size of the stack : {my_stack.Size()}')
        print(f'   The peek of the stack : {my_stack.peek()}')
        my_stack.pop()
        print(f'   Is the stack empty : {my_stack.Isempty()}')
    print()
    my_stack.push(input('Enter the item to push: '))
    my_stack.delete()
    my_stack.pop()

main()

"""
Output-
Enter the no. of elements to push : 5
Enter the elements to push
1) INDIA
2) AMERICA
3) CHINA
4) BRAZIL
5) RUSSIA
1) The size of the stack : 5
   The peek of the stack : RUSSIA
   Is the stack empty : False
2) The size of the stack : 4
   The peek of the stack : BRAZIL
   Is the stack empty : False
3) The size of the stack : 3
   The peek of the stack : CHINA
   Is the stack empty : False
4) The size of the stack : 2
   The peek of the stack : AMERICA
   Is the stack empty : False
5) The size of the stack : 1
   The peek of the stack : INDIA
   Is the stack empty : True

Enter the item to push: GERMANY
You successfully deleted the stack.
error:Stack underflow
"""
