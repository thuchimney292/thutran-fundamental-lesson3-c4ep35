n = int(input("Enter N = "))
m=n
if n==1:
     print('Không thể phân tích thành thừa số nguyên tố')
else :
    i=2
    while i<=m:
            while m % i ==0 :
                    print(i,end=' ')
                    m=m/i
            i+=1