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
    sizes[sizes.index(m)]=8
    print('Now my biggest sheep has size ' + str(m)+ " let's shear it")
    print('After shearing, here is my flock : ',sizes)
