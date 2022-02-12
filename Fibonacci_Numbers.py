n=int(input("n: "))
fibonacci=[0 for k in range(n)]
fibonacci[1]=1
fibonacci[2]=1
for i in range(2,n):
    fibonacci[i]=fibonacci[i-2]+fibonacci[i-1]
print(fibonacci)