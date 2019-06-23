#password có ít nhất một kí tự số, 1 kí tự a-z hoặc A-Z, 1 kí tự đặc biệt (@, %, $)
check=False
special=['%','@','$']
while not check:
    pass_word=input("Enter your password: ")
    if len(pass_word)>8:
        number=False
        string=False
        k=False
        for i in range(len(pass_word)):
            if "0"<=pass_word[i] <="9": 
                number=True
            elif "a"<=pass_word[i]<="z" or "A"<=pass_word[i]<="Z": 
                string=True
            else: 
                if pass_word[i] in special:
                    k=True
        if number and string and k:
            print("Success")
            check=True
        else: print("Not safely")
    else:
        print("Not safely")