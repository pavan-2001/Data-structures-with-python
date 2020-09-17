from timeit import default_timer
def left(i):
    return (2*i)
def right(i):
    return ((2*i)+1)
def max_heapify(seq,i,heapsize):
    L=left(i)
    R=right(i)
    largest=i
    if(L<=heapsize) and (seq[L]>seq[largest]):
        largest=L
    if(R<=heapsize) and (seq[R]>seq[largest]):
        largest=R
    if largest!=i:
        temp=seq[i]
        seq[i]=seq[largest]
        seq[largest]=temp
        seq=max_heapify(seq,largest,heapsize)
    return seq
def build_max_heap(seq,heapsize):
    i=int((heapsize/2))
    while i>=1:
        seq=max_heapify(seq,i,heapsize)
        i-=1
    return seq
def heap_sort(seq,heapsize):
    seq=build_max_heap(seq,heapsize)
    i=heapsize
    while i>1:
        temp=seq[heapsize]
        seq[heapsize]=seq[1]
        seq[1]=temp
        heapsize-=1
        i-=1
        seq=max_heapify(seq,1,heapsize)
    return seq

def main():
    start=default_timer()
    n=int(input('Enter the no. of elements in your list : '))
    heapsize=n
    print('Enter the elements : ')
    seq=[]
    s=str(input())
    seq=[int(i) for i in s.split()]
    seq.insert(0,0)
    seq=heap_sort(seq,heapsize)
    print(f'The sorted sequence is ',end='')
    for i in range(1,n+1):
        print(seq[i],end=' ')
    print()
    elapsed=default_timer()-start
    print(f'The total time taken to execute is {elapsed:.2f} seconds.')
main()

"""
Output-
Enter the no. of elements in your list : 10
Enter the elements :
10 1 9 2 8 3 7 4 6 5
The sorted sequence is 1 2 3 4 5 6 7 8 9 10
The total time taken to execute is 2.24 seconds
"""
