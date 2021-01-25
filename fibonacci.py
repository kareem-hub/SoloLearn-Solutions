num = int(input())

def fibonacci(n):
    lst=[0,1]
    for a in range(2,n):
        lst.append(lst[a-1]+lst[a-2])
    for e in lst:
        print(e)
        
fibonacci(num)