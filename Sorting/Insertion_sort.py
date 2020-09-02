import array
def INSERTION_SORT(a):
    for j in range(1,len(a)):
        i=j-1
        key=a[j]
        while i>=0 and a[i]>key:
            a[i+1]=a[i]
            i-=1
        a[i+1]=key
    return a
def main():
    num=int(input('Enter the number of elements you want to insert : '))
    storage=array.array('i')
    for i in range(0,num):
        val=int(input())
        storage.append(val)
    storage=INSERTION_SORT(storage)
    for i in storage:
        print(i,end=' ')
main()
    
"""
Output-
Enter the number of elements you want to insert : 5
28
38
1
367
0
The sorted array is :
0 1 28 38 367
"""
