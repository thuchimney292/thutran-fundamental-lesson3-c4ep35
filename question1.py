items=["T-Shirt","Sweater"]
while True:
    want = input('Welcom to our shop, what do you want (C,R,U,D) ? ')
    if want == "c" or want == "C" :
        items.append(input("Enter new item: "))
    elif want == "U" or want =="u" :
        k = int(input("Update position: "))
        items[k-1]=input("New item : ")
    elif want == "D" or want == "d" :
        k = int(input('Delete position : '))
        del items[k-1]
    else:
        if want != "R" and want != "r" :
            print('Please re-enter')
            continue
    print('Our items =',items)
    check = input("Enter Y if you want to end :")
    if check == "Y" or check == "y" : break