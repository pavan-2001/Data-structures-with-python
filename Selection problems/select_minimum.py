def select_min(seq):
    min=seq[0]
    for i in range(1,len(seq)):
        if seq[i]<min:
            min=seq[i]
    return min

def main():
    seq=[]
    with open("input.txt","r") as file:
        for item in file:
            seq.append(int(item))
    print(select_min(seq))
main()

"""
Output-
140743
"""
