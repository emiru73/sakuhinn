import tkinter
import random

root=tk.Tk()
root.geometry('700x560')
root['bg']='lightgrey'
#画像用のキャンバス作成
canvas=tk.Canvas(root,width=640,height=426,bd=0, highlightthickness=0, relief='ridge')
#キャンバスを設置(上下に20の余白)
canvas.pack(pady=20)
#画像を用意
photo1=tk.PhotoImage(file='cat1.png')
#画像を描画(中点x,中点y,画像)
canvas.create_image(320,213,image=photo1)
photo2=tk.PhotoImage(file='cat2.png')
canvas.create_image(340,233,image=photo2)
root.mainloop()


    root = tkinter.Tk()
    root.geometry('1270x270')
    q1 = tkinter.Label(root,text='このポケモンだ～れだ！')