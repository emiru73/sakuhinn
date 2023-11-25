from PIL import Image,ImageTk
import tkinter as tk

# 画像切り替え 関数
def change_quiz():
    global current_quiz
#     if 
    current_quiz = (current_quiz + 1) % len(quizlist) # クイズ番号を1増やす(最後のインデックスの場合、0になる)
    image_label["image"] = quizlist[current_quiz]["image"] # 表示画像を変更


# 現在のクイズ番号
current_quiz = 0

# ウィンドウ用意
root = tk.Tk()
root.geometry("800x600")

# クイズの画像パス(文字列)と問題文　用意
quizlist =[
    {"image":"img/pikat2_quiz.png","quiz":"問題文1"},
    {"image":"img/pika1.png","quiz":"問題文2"},
#     {"image":"pikat2.png","quiz":"問題文2"},
#     {"image":"pikat2.png","quiz":"問題文2"},
#     {"image":"pikat2.png","quiz":"問題文2"},
#     {"image":"pikat2.png","quiz":"問題文2"},
#     {"image":"pikat2.png","quiz":"問題文2"},
#     {"image":"pikat2.png","quiz":"問題文2"},
#     {"image":"pikat2.png","quiz":"問題文2"},
#     {"image":"pikat2.png","quiz":"問題文2"},
#     {"image":"pikat2.png","quiz":"問題文2"},
#     {"image":"pikat2.png","quiz":"問題文2"},
#     {"image":"pikat2.png","quiz":"問題文2"},
#     {"image":"pikat2.png","quiz":"問題文2"},
#     {"image":"pikat2.png","quiz":"問題文2"},
#     {"image":"pikat2.png","quiz":"問題文2"},
]

# 画像パスの文字列から画像読み込む
for quiz in quizlist:
    img_open = Image.open(quiz["image"])
    quiz["image"] = ImageTk.PhotoImage(img_open.resize((200,200)))

# 画像を表示するためのラベルウィジェット準備
image_label = tk.Label(root,image=quizlist[current_quiz]["image"])
image_label.pack()

# ボタンウィジェット準備
button = tk.Button(root,text="次へ",command=change_quiz)
button.pack()

def button_on():
    but_2.place_forget()
    but_1.place(x=150, y=100)

def button_off():
    but_1.place_forget()
    but_2.place(x=150, y=200)

root = tk.Tk()
cvs =tk.Canvas(width=300, height=300, bg='#ffffff')
but_1 = tk.Button(text='ボタンを押す', command = button_off)
but_2 = tk.Button(text='ボタンを出す', command = button_on)
but_1.place(x=150, y=100)
cvs.pack()

# メインループ
root.mainloop()