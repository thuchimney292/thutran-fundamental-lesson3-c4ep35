n=int(input('Enter the number of sheep you have : '))
month=int(input('Enter the number of months you want : '))
sizes=[]
for i in range(n):
    k=int(input('Enter the size of the sheep '+ str(i+1) +' : '))
    sizes.append(k)
print('Hello, My name is Thu and these are the ship sizes: ',sizes)
for i in range(month):
    print('MONTH '+str(i+1))
    for j in range(n):
        sizes[j]+=50
    print('One month has passed, now here is my flock : ',sizes)
    m=max(sizes)
    print('Now my biggest sheep has size ' + str(m)+ " let's shear it")
    sizes[sizes.index(m)]=8
    print('After shearing, here is my flock : ',sizes)
sumsize=0
for i in range(n):
    sumsize+=sizes[i]
print('My flock has size in total : ' + str(sumsize))
print('I would get '+str(sumsize)+'*2$ = '+str(2*sumsize))