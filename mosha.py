import tkinter as tk
from tkinter import messagebox

#ウインドウ
win = tk.Tk()
win.title("ブロック崩し")
win.geometry("425x625")
win.resizable(False, False)

#キャンバス
can = tk.Canvas(bg="black", width=400, height=600)
can.place(x=10, y=10)

#ゲームオーバー
def gameOver():
    messagebox.showinfo("Information", "GAME OVER!")
    exit()

#ゲームクリア
def gameClear():
    messagebox.showinfo("Information", "CONGRATULATIONS!!!!")
    exit()

#ボール
ball_x = 50; ball_y = 500; bx = 5; by = -5
def drawBall():
    global ball_x, ball_y, bx, by
    can.create_oval(ball_x, ball_y, ball_x+20, ball_y+20, fill="white")
    if ball_x<=0 or ball_x>=385 :
        bx *= -1
    if ball_y<=0 :
        by *= -1
    if ball_y>=603 :
        gameOver()
    if ball_y>=560 and ball_x>=rack_x-10 and ball_x<=rack_x+50 :
        by *= -1
    ball_x += bx; ball_y += by

#ラケット
rack_x =170; keyPress_R = False; keyPress_L = False
def rightKeyPress(event):
    global keyPress_R
    keyPress_R = True
def rightKeyRelease(event):
    global keyPress_R
    keyPress_R = False
def leftKeyPress(event):
    global keyPress_L
    keyPress_L = True
def leftKeyRelease(event):
    global keyPress_L
    keyPress_L = False
win.bind("<KeyPress-Right>", rightKeyPress)
win.bind("<KeyRelease-Right>", rightKeyRelease)
win.bind("<KeyPress-Left>", leftKeyPress)
win.bind("<KeyRelease-Left>", leftKeyRelease)
def drawRacket():
    global rack_x
    can.create_rectangle(rack_x, 580, rack_x+60, 595, fill="white")
    if keyPress_R==True and rack_x<=350:
        rack_x += 5
    if keyPress_L==True and rack_x>=-10:
        rack_x -= 5

#ブロック
block = []
for x in range(5) :
    for y in range(4) :
        block.append({"x":x*80+5, "y":y*40+10, "st":1})
def drawBlock() :
    global ball_x, ball_y, by
    block_count = 0
    for i in range(len(block)):

tk.mainloop()
        x = block[i]["x"]
        y = block[i]["y"]
        st = block[i]["st"]
        if ball_y<=y+30 and ball_x>=x-10 and ball_x<=x+60 and st==1 :
            by *=-1
            block[i]["st"] = 0
        if st==1 :
            can.create_rectangle(x, y, x+70, y+30, fill="white")
            block_count += 1
    if block_count == 0:
        gameClear()        

#表示ループ
def gameLoop():
    can.delete("all")
    drawBall()
    drawRacket()
    drawBlock()
    win.after(15, gameLoop)

gameLoop()

#ウインドウループ
win.mainloop() 
