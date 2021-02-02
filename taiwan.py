import turtle,time #引進turtle函式庫
turtle.speed(10)  #設定畫筆速度
#定義畫長方形的方法
def rectangle(x,y,leng,wid,color):    
  #定義"rectangle"函式有五個變數輸入，xy是起點座標，leng跟wid是長跟寬，
  #color是顏色
  turtle.color(color)     #設定顏色為參數傳入的顏色
  turtle.penup()          #畫筆拿起來
  turtle.goto(x,y)        #移動到起點位置x,y
  time.sleep(1)
  turtle.down()           #下筆開始畫
  turtle.begin_fill()     #開始填滿
  turtle.forward(leng)    #前進leng的長度
  turtle.right(90)        #右轉90度
  turtle.forward(wid)     #前進wid的長度
  turtle.right(90)        #右轉90度
  turtle.forward(leng)    #前進leng的長度
  turtle.right(90)        #右轉90度
  turtle.forward(wid)     #前進wid的長度
  turtle.right(90)        #右轉90度
  turtle.end_fill()       #結束填滿
  time.sleep(1)
rectangle(-200,200,600,400,'red')   
#從(-200,200)開始畫一個長600寬400，紅色的長方形
time.sleep(1)
rectangle(-200,200,300,200,'blue')  
#從(-200,200)開始畫一個長300寬200，藍色的長方形
#定義畫太陽的方法
time.sleep(1)
def sun(x,y,length,color):    
    #定義 "sun" 函式，有四個輸入,x,y是起點座標，length是長度，color是顏色turtle.up()          #筆拿起來
    turtle.color(color)  #設定顏色為color
    turtle.penup()          #畫筆拿起來
    turtle.goto(x,y)     #移動到(x,y)
    time.sleep(1)
    turtle.setheading(345)   #面向345度的方向
    turtle.down()            #下筆開始畫
    turtle.begin_fill()      #開始填滿
    counter=0                #計數器=0
    while True:              #無線迴圈
      time.sleep(1)
      turtle.forward(length)    #往前length的距離
      turtle.left(150)          #左轉150度
      counter+=1                #計數器+1
      if counter>=12:         #如果計數器大於或等於12
        break                 #就跳出迴圈
    turtle.end_fill()        #結束填滿
sun(-150,100,175,'white')    #從(-150,100)開始畫一個175大小的白色太陽turtle.up()                  #筆拿起來
#畫圓
turtle.color('blue')  #藍色
turtle.penup()          #畫筆拿起來
turtle.goto(-104,100) #設定起點座標
turtle.setheading(270) #面向270度方向
turtle.down()         #下筆
time.sleep(1)
turtle.pensize(10)    #筆的粗細調成10
turtle.circle(44)     #畫一個半徑44的圓
turtle.up()           #筆拿起來