if __name__ == '__main__':
    n = int(input())
    arr = list(set(map(int,input().split())))
    arr.sort()
    print(arr[-2])




"""
a=[10,10,20,20,30,40]
b=set(a)
print(b)
c=list(b)
c.sort()
print(c[-2])
"""
