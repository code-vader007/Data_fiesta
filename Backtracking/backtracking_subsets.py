
def is_a_solution(arr,k,n):
    return(k==n)
def construct_candidates(arr,k,n,count,countcand):
    count[0]=True
    count[1]=False
    countcand=2
def process_solution(arr,k,n):
    A=[]
    for i in range(k+1):
        if(arr[i]==True):
            A.append(i)
    print(A)
def generate_subsets(n):
    a=[0,0,0,0]
    backtrack(a,0,n)
def backtrack(arr,k,n):
    count=[0,0]
    count[0]=True
    count[1]=False
    countcand=2
    if(is_a_solution(arr,k,n)):
        process_solution(arr,k,n)
    else:
        k=k+1
        construct_candidates(arr,k,n,count,countcand)
        for i in range(countcand):
            arr[k]=countcand[i]
            backtrack(arr,k,n)

print(generate_subsets(3))