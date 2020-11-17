class node:
    def __init__(self,value=0,next=None):
        self.value=value
        self.next=next
class queue(node):
    def __init__(self,head=None,tail=None):
        self.head=node()
        self.tail=node()
        self.length=0
    # operations on a queue.
    # 1) Queue_empty()
    # 2) Enqueue()
    # 3) Dequeue()

    # All these operations take O(1) n time.
    
    def Queue_empty(self):
        if self.length>=1:
            return False
        else:
            return True
    
    def Enqueue(self,value):
        tempnode=node(value)
        self.length+=1
        if self.length==1:
            self.head=tempnode
        self.tail.next=tempnode
        self.tail=tempnode
    
    def Dequeue(self):
        if self.length==0:
            print("Error : Queue underflow.")
            return  
        tempnode=self.head
        self.head=self.head.next
        self.length-=1
        return tempnode.value

def main():
    a=queue()
    print(f'Is the queue empty : {a.Queue_empty()}')
    a.Enqueue('apple')
    a.Enqueue('mango')
    a.Enqueue('grapes')
    a.Enqueue('banana')
    a.Enqueue('orange')
    print(f'Is the queue empty : {a.Queue_empty()}')
    while a.Queue_empty()!=True:
        print(a.Dequeue())
    print(f'Is the queue empty : {a.Queue_empty()}')
main()


"""
Output : 
Is the queue empty : True
Is the queue empty : False
apple
mango
grapes
banana
orange
Is the queue empty : True 

"""
