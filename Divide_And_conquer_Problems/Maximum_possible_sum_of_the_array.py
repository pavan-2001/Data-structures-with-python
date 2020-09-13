from timeit import default_timer
def Find_maximum_subarray_crossing_midpoint(seq,low,mid,high):
    left_sum=-1e9
    right_sum=-1e9
    sum=0
    left_index=mid
    right_index=mid+1
    j=mid
    while j>=low:
        sum+=seq[j]
        if sum>left_sum:
            left_sum=sum
            left_index=j
        j-=1
    sum=0
    i=mid+1
    while i<=high:
        sum+=seq[i]
        if sum>right_sum:
            right_sum=sum
            right_index=i
        i+=1
    return [left_index,right_index,(left_sum+right_sum)]

def Find_maximum_subarray(seq,low,high):
    if low==high:
        return [low,high,seq[low]]
    mid=(low+high)//2
    left=Find_maximum_subarray(seq,low,mid)
    right=Find_maximum_subarray(seq,mid+1,high)
    crossing_midpoint=Find_maximum_subarray_crossing_midpoint(seq,low,mid,high)
    ans=crossing_midpoint
    if ans[2]<crossing_midpoint[2]:
        ans=crossing_midpoint
    if ans[2]<left[2]:
        ans=left
    if ans[2]<right[2]:
        ans=right
    return ans

def main():
    start=default_timer()
    n=int(input('Enter the no. of elements in your sequence : '))
    seq=[0]*n
    for i in range(0,n):
        seq[i]=int(input())
    seq=Find_maximum_subarray(seq,0,n-1)
    stop=default_timer()
    elapsed=stop-start
    print(f'Starting index : {seq[0]+1}\nEnding index : {seq[1]+1}\nThe maximum possible sum is : {seq[2]}\nTotal time taken to execute is {elapsed:.2f} seconds')
main()
"""
Output-
Enter the no. of elements in your sequence : 10
10
-20
30
-40
50
-60
70
-80
90
30
Starting index : 9
Ending index : 10
The maximum possible sum is : 120
Total time taken to execute is 18.56 seconds
"""
