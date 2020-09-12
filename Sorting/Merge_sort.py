def merge(sequence,beg,mid,end):
    n1=mid-beg+1
    n2=end-mid
    L=[0]*(n1+1)
    R=[0]*(n2+1)
    for i in range(0,n1):
        L[i]=sequence[beg+i]
    for i in range(0,n2):
        R[i]=sequence[mid+i+1]
    i=0
    j=0
    L[n1]=1e9
    R[n2]=1e9
    for k in range(beg,end+1):
        if(L[i]<=R[j]):
            sequence[k]=L[i]
            i+=1
        else:
            sequence[k]=R[j]
            j+=1


def merge_sort(sequence,beg,end):
    if beg<end:
        mid=((beg+end)//2)
        merge_sort(sequence,beg,mid)
        merge_sort(sequence,mid+1,end)
        merge(sequence,beg,mid,end)
def main():
    n=int(input('Enter the number of elements in your sequence : '))
    sequence=[]
    n1=n
    while n>0:
        sequence.append(int(input()))
        n-=1
    merge_sort(sequence,0,n1-1)
    print(sequence)
main()

"""
Output-
Enter the number of elements in your sequence : 10
10
1
9
2
8
3
7
4
6
5
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
"""
