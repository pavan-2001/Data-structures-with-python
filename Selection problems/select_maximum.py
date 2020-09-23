def select_maximum(seq):
    max=seq[0]
    for i in range(1,len(seq)):
        if seq[i]>max:
            max=seq[i]
    return max

def main():
    seq=[]
    with open("input.txt","r") as file:
        for i in file:
            seq.append(int(i))
    print(select_maximum(seq))
main()

"""
Output-
9925673
"""
