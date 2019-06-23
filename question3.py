import random
keys=['champion','meticulous','hexagon']
key=random.choice(keys)
word=list(key)
random.shuffle(word)
for i in range(len(word)):
    print(word[i],end=' ')
print()
k=0
while k<3:
    answer=input('Your answer: ')
    if answer==key:
        print('Hura')
        break
    else:
        print('Uncorrect')
        k+=1
        if k==3:
            print('You lost')