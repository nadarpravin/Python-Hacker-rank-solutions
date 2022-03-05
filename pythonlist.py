"""n=int(input())
a=str(n)
b=[]
for i in a:
    b.append(a)
for i in b:
    b.clear()
    

b.insert(0,5)
b.insert(1,10)
b.insert(0,6)
print(b)
b.remove(6)
b.append(9)
b.append(1)
b.sort()
print(b)
b.pop()
b.reverse()
print(b)"""


if __name__ == '__main__':
    N = int(input())
    Output = [];
    for i in range(0,N):
        ip = input().split();
        if ip[0] == "print":
            print(Output)
        elif ip[0] == "insert":
            Output.insert(int(ip[1]),int(ip[2]))
        elif ip[0] == "remove":
            Output.remove(int(ip[1]))
        elif ip[0] == "pop":
            Output.pop();
        elif ip[0] == "append":
            Output.append(int(ip[1]))
        elif ip[0] == "sort":
            Output.sort();
        else:
            Output.reverse();

