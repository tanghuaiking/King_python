def fib(n):
    a,b= 0,1
    count=1
    while count<n:
        a,b=b,a+b
        print(a)
        count=count+1
    
if __name__=='__main__':
    fib(10)
    
