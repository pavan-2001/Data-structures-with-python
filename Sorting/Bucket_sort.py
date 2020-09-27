def insertion_sort(seq):
    for i in range(1,len(seq)):
        j=i-1
        key=seq[i]
        while j>=0 and seq[j]>key:
            seq[j+1]=seq[j]
            j-=1
        seq[j+1]=key
    return seq

def bucket_sort(seq):
    arr=[]
    buckets=10
    for i in range(buckets):
        arr.append([])
    for i in range(len(seq)):
        arr[int(buckets*seq[i])].append(seq[i])
    for i in range(len(arr)):
        arr[i]=insertion_sort(arr[i])
    k=0;
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            seq[k]=arr[i][j]
            k+=1
    return seq

def main():
    seq=[0.897,0.565,0.656,0.1234,0.665,0.3434]
    print(f'The sorted sequence is :\n{bucket_sort(seq)}')
main()

"""
Output-
The sorted sequence is :
[0.1234, 0.3434, 0.565, 0.656, 0.665, 0.897]
"""
