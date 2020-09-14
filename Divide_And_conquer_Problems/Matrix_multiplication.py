from timeit import default_timer
def Matrix_multiplication(A,B):
    m3=[]
    for i in range(0,len(A)):
        v=[0]*len(B[0])
        for j in range(0,len(B[0])):
            v[j]=0
            for k in range(0,len(B)):
                v[j]+=int(A[i][k])*int(B[k][j])
        m3.append(v)
    return m3

def main():
    start=default_timer()
    print("Enter the order of first matrix : ")
    r1,c1=map(int,input().split())
    print("Enter the order of second matrix : ")
    r2,c2=map(int,input().split())
    if c1!=r2:
        print("error: Incorrect order!!\nCan't multiply matrices")
    else:
        A=[]
        B=[]
        print('Enter the first matrix : ')
        for i in range(0,r1):
            v=[]
            v=input().split()
            A.append(v)
        print('Enter the second matrix : ')
        for i in range(0,r2):
            v=[]
            v=input().split()
            B.append(v)
        C=Matrix_multiplication(A,B)
        print(f'The order of the resultant matirx is {r1}X{c2}\nThe resultant matrix is : ')
        for i in range(0,r1):
            for j in range(0,c2):
                print(C[i][j],end=' ')
            print()
    stop=default_timer()
    elapsed=stop-start
    print(f'Time taken to execute {elapsed:.2f} seconds')
main()

"""
Output-
                      Testcase 1
Enter the order of first matrix :
3 3
Enter the order of second matrix :
3 4
Enter the first matrix :
1 2 3
4 5 6
7 8 9
Enter the second matrix :
1 2 3 4
5 6 7 8
9 10 11 12
The order of the resultant matirx is 3X4
The resultant matrix is :
38 44 50 56
83 98 113 128
128 152 176 200
Time taken to execute 23.06 seconds
      
                    Testcase 2
Enter the order of first matrix :
3 4
Enter the order of second matrix :
2 3
error: Incorrect order!!
Can't multiply matrices
Time taken to execute 6.37 seconds
"""
