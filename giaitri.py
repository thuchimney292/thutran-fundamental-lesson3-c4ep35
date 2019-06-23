n=int(input('Enter n = '))
row1=0
row2=n-1
column1=0
column2=n-1
a = []
for i in range(n):
    a.append([])
    for j in range(n):
        a[i].append(0)
count=0
while count<n*n:
    for j in range(column1,column2+1):
        count+=1
        a[row1][j]=count
    row1+=1
    for i in range(row1,row2+1):
        count+=1
        a[i][column2]=count
    column2-=1
    for j in range(column2,column1-1,-1):
        count+=1
        a[row2][j]=count
    row2-=1
    for i in range(row2,row1-1,-1):
        count+=1
        a[i][column1]=count
    column1+=1
len_=len(str(n*n))
for i in range(n):
    for j in range(n):
        if len(str(a[i][j]))<len_:
            for k in range(len(str(a[i][j])),len_):
                print(end=' ')
        print(a[i][j],end=' ')
    print()
