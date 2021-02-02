#2-3
import turtle,time #匯入烏龜和時間模組
alex = turtle.Turtle()#創建一隻烏龜
win = turtle.Screen()
win.title('my window')
win.bgcolor('black')
alex.color('red')#改變畫筆顏色
alex.shape('turtle')
alex.forward(100)#往前走100格
time.sleep(1)#程式睡1秒
alex.left(90)#向左轉90度
alex.forward(100)
time.sleep(1)
alex.left(90)
alex.forward(100)
time.sleep(1)
alex.left(90)
alex.forward(100)
