def fibonacci(n):
    if n ==0:
        return 0
    if n ==1:
        return 1
    if n > 1:
        return  fibonacci(n-1) + fibonacci(n-2)

def lucas(n):
    if n == 0:
        return 2
    if n == 1:
        return 1
    if n > 1:
        return lucas(n-1) + lucas(n-2)
    
def sum_series(n,n2=0,n3=1):
    if n == 0:
        return n2
    if n == 1:
        return n3
    else:
        return sum_series(n-1,n2,n3) + sum_series(n-2,n2,n3)
        
