'''
2-2
使用者在1-20之間猜個數字，
若比答案大，則告知太大，
若比答案小，則告知太小，
只能猜五次，五次猜完沒猜到就結束，
猜對後告訴使用者“玩了幾次”。
'''
import random

ans = random.randint(1,20)
counter = 0 # 計算猜幾次

while True:
    guess = int(input('請在1~20間猜一個數字(只能猜五次): '))
    if guess>20 or guess<0:
        print('輸入錯誤，請重新輸入!!!')
        counter = counter +1
    else:
        if counter == 5:
            print('just 5 times')
            break
        elif guess > ans:
            print('小一點')
            counter =counter+ 1
        elif guess < ans:
            print('大一點')
            counter =counter+ 1
        else:
            print('Bingo!!!')
            counter =counter+ 1
            print('你猜了'+str(counter)+'次就答對了')
            break