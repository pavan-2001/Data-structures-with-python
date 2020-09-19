from timeit import default_timer
def partition(seq,beg,end):
    start=beg-1
    for i in range(beg,end):
        if seq[i]<seq[end]:
            start+=1
            seq[start],seq[i]=seq[i],seq[start]
    seq[start+1],seq[end]=seq[end],seq[start+1]
    return (start+1)
def Quick_sort(seq,beg,end):
    if beg<end:
        q=partition(seq,beg,end)
        Quick_sort(seq,beg,q-1)
        Quick_sort(seq,q+1,end)
def main():
    start=default_timer()
    n=int(input('Enter the no. of elements : '))
    string=input('Enter the sequence : ')
    seq=[int(s) for s in string.split()]
    Quick_sort(seq,0,n-1)
    print(f'The sorted sequence is {seq}')
    elapsed=default_timer()-start
    print(f'The time taken to execute is {elapsed:.2f} seconds.')
main()
