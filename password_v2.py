
password = 'a123456'
count = 3 
while True:
    pwd = input("請輸入密碼: ")
    if pwd == password:
        print('登入成功!!!')
        break
    else:
        count -=1
        if count != 0:
            print('密碼錯誤!  還有', count, '次機會')
        elif count == 0:
            print('你不能登入了!!!')    
            break
        
