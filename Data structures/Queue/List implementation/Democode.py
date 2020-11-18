from timeit import default_timer 
from Queue_list import*
def main():
    start=default_timer()
    a=my_queue()
    print(f'Is the queue empty : {a.empty()}')
    with open("input.txt","r") as file:
        for i in file:
            a.enqueue(i)
    print(f'Is the queue empty : {a.empty()}')
    with open("output.txt","a") as file:
        while a.empty()!=True:
            file.write(a.dequeue())
    print(f'Is the queue empty : {a.empty()}')
    end=default_timer()-start
    print(f'Total time taken to execute : {end:.2f}sec')
main()

"""
Output : 
Is the queue empty : True
Is the queue empty : False
Is the queue empty : True
Total time taken to execute : 0.00sec
"""
