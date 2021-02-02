import random #匯入random模組
n = random.randint(1,20) #題目
while True: #一直
    ans = int(input('number:'))
    if n == ans:
        print('答對')
        break
    else:
        print('答錯')
'''  
檔名：2-1  
電腦從1~20隨機選出一個數字，
在螢幕上要求使用者輸入所選擇的數字，
猜到對。
break
'''