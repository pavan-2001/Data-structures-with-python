import random
from timeit import default_timer
def Randomized_hiring_assistant(list,fees):
    cost=int(0)
    best=0
    num=int()
    for i in range(0,len(list)):
        num=list[i]
        if num>best:
            best=num
            cost+=fees
    return (best,cost,list)

def Randomize_in_place(list,fees):
    for i in range(0,len(list)):
        index=random.randint(0,len(list)-1)
        list[i],list[index]=list[index],list[i]
    return Randomized_hiring_assistant(list,fees)

def main():
    start=default_timer()
    print('Enter the cost of hiring of employment agency : ',end='')
    fees=int(input())
    print('Enter the no. of assistant : ',end='')
    n=int(input())
    a=input('Enter the list of assistants : ')
    list=[int(s) for s in a.split()]
    best,cost,list=Randomize_in_place(list,fees)
    elapsed=default_timer()-start
    print(f'The candidate with best qualification is {best}.\nThe cost of hiring is Rs {cost}.\nThe randomized list is : {list}\nThe time taken to execute is {elapsed:.2f} second.')
main()

"""
Output-
                               Worstcase input
Enter the cost of hiring of employment agency : 100
Enter the no. of assistant : 10
Enter the list of assistants : 1 2 3 4 5 6 7 8 9 10
The candidate with best qualification is 10.
The cost of hiring is Rs 400.
The randomized list is : [7, 5, 4, 2, 6, 8, 9, 1, 10, 3]
The time taken to execute is 6.66 second.

                               Bestcase input
Enter the cost of hiring of employment agency : 100
Enter the no. of assistant : 10
Enter the list of assistants : 10 9 8 7 6 5 4 3 2 1
The candidate with best qualification is 10.
The cost of hiring is Rs 400.
The randomized list is : [5, 8, 7, 3, 1, 9, 2, 4, 10, 6]
The time taken to execute is 15.15 second.

                               Average case input
Enter the cost of hiring of employment agency : 100
Enter the no. of assistant : 10
Enter the list of assistants : 1 2 3 4 10 5 6 7 8 9
The candidate with best qualification is 10.
The cost of hiring is Rs 200.
The randomized list is : [9, 8, 6, 5, 7, 1, 2, 10, 4, 3]
The time taken to execute is 14.43 second.
"""
