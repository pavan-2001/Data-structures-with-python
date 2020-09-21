
#                       COUNTING SORT

from timeit import default_timer

#       COUNTING SORT ALGORIHTM

def Counting_sort(seq,highest_value):
    freq=[0]*(highest_value+1)
    c=[0]*(len(seq)+1)
    for i in range(0,len(seq)):
        freq[seq[i]]+=1
    for i in range(1,highest_value+1):
        freq[i]+=freq[i-1]
    i=len(seq)-1
    while i>=0:
        c[freq[seq[i]]]=seq[i]
        freq[seq[i]]-=1
        i-=1
    return c

def main():
    start=default_timer()
    seq=[]
    highest_value=-1e5
    with open("input.txt","r") as file:
        for i in file:
            seq.append(int(i))
            if int(i)>highest_value:
                highest_value=int(i)
    c=Counting_sort(seq,highest_value)
    with open("output.txt","a") as file:
        for i in range(1,len(seq)+1):
            file.write(str(c[i]))
            file.write('\n')
    elapsed=default_timer()-start
    print(f'The time taken to execute is {elapsed:.2f} seconds')
main()
