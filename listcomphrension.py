a=int(input(' ENTER ANY NUMBER '))
b=int(input(' ENTER ANY NUMBER '))
c=int(input(' ENTER ANY NUMBER '))
n=int(input(' ENTER ANY NUMBER '))   #sum of a,b,c should not be equal to n


b=[[i,j,k] for i in range(0,a+1) for j in range(0,b+1) for k in range(0,c+1) if (i+j+k)!=n]
print(b)


"""temp=[]
for i in range (0,a+1):
    for j in range (0,b+1):
        for k in range (0,c+1):
            if (i+j+k!=n):
                temp.append([i,j,k])
                
print(temp)"""