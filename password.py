time = 4
x = int(time)
while True :
    password = input("請輸入密碼: ")
    while x > 1:
        if password == 'a123456':
            print('登入成功')
            break         
        elif password != 'a123456' and x == 2:
            x = x-1
            print("密碼錯誤! 剩下最後機會")
            password = input("請輸入密碼: ")
            if password == 'a123456':
                print('登入成功')
                break
            else:
                print("三次機會用完，今天不能在登入嘍!!!")    
        else :
            x = x-1
            print("密碼錯誤! 還有",x,"次機會")
            password = input("請輸入密碼: ")
    break