class my_queue:
    def __init__(self):
        # points to the front of the list
        self.head=0
        # points to last of the list
        #keeps the track of the length of the queue
        self.length=0
        self.list=[]
    def enqueue(self,value):
        self.list.append(value)
        self.length+=1
        if len(self.list)==1:
            self.head=0
    def dequeue(self):
        output=self.list[self.head]
        self.head+=1
        self.length-=1
        return output
    def empty(self):
        if self.length==0:
            return True
        else:
            return False
