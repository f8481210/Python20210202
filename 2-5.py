import turtle,time #匯入烏龜和時間模組
t1 = turtle.Turtle()#創建一隻烏龜
t2 = turtle.Turtle()#創建一隻烏龜
win = turtle.Screen()
win.title('my window')
win.bgcolor('black')
t1.color('red')#改變畫筆顏色
t1.shape('turtle')
t1.forward(100)#往前走100格


t2.shape('circle')
t2.pensize(8)
t2.color('white')
t2.right(180)
t2.forward(100)