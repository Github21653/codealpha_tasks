#Fibonacci Generator
def fibGen(n):
    arr=[]
    n1,n2=0,1
    for i in range(n):
        arr.append(n1)
        n3=n1+n2
        n1=n2
        n2=n3
    return arr
num = int(input("Enter the number of terms for the Fibonacci sequence: "))
print(fibGen(num))