'''Problem Statement-:  You have M questions and N seconds to complete a test. Each question has some points and takes some time to solve (which will be given as input). Find the maximum mark that can be scored by the student within the given time N.

Sample test case:

4 // number of questions
10 // Total time to attend the test
1 2 // one mark question – 2 seconds to solve.
2 3 // two mark question – 3 seconds to solve.
3 5 // three mark question – 5 seconds to solve.
4 7 // 4 mark question – 7 seconds to solve.'''

''' 0/1 Knapsack Problem'''

def total(n,t,mark,time):
     arr=[[0 for i in range(t+1)] for j in range(n+1)]
     for i in range(1,n+1):
          for j in range(t+1):
               if(time[i-1]<=j):
                    arr[i][j]=max(mark[i-1]+arr[i-1][j-time[i-1]],arr[i-1][j])
               else:
                    arr[i][j]=arr[i-1][j]
     return arr[n][t]

n=int(input())
t=int(input())
mark=[]
time=[]
for _ in range(n):
     l,m=input().split()
     mark.append(int(l))
     time.append(int(m))
print(total(n,t,mark,time))
     
 
