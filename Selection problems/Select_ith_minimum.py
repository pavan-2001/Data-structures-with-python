def partition(seq,beg,end):
    start=beg-1
    for i in range(beg,end):
        if seq[i]<seq[end]:
            start+=1
            seq[i],seq[start]=seq[start],seq[i]
    seq[start+1],seq[end]=seq[end],seq[start+1]
    return start+1

def randomized_select(seq,beg,end,i):
    if beg==end:
        return seq[beg]
    q=partition(seq,beg,end)
    if i==q:
        return seq[q]
    elif i<q:
        return randomized_select(seq,beg,q-1,i)
    else:
        return randomized_select(seq,q+1,end,i)
def main():
    seq=[]
    with open("input.txt","r") as file:
        for i in file:
            seq.append(int(i))
    print(randomized_select(seq,0,128,127))
main()

"""
Output-
9863010
"""
