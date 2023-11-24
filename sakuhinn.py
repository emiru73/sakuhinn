# from tkinter import Tk,Label
import tkinter as tk
import random
from PIL import Image,ImageTk

window = tk.Tk()
window.title('クイズ')
window.geometry('1280x720')
image = Image.open("pika1.png")
    
image2 = image.resize((200,200))
image3=ImageTk.PhotoImage(image2)
lavel = tk.Label(window,image=image3)
lavel.pack()

# root = tk.Tk()
# label = tk.Label(root, text="ラベルです", font=("Arial", 30))
# label.pack() # ウィジェットの配置

# root.mainloop()
# root=tk.Tk()
# root.geometry('700x560')
# root['bg']='lightgrey'
# #画像用のキャンバス作成
# canvas=tk.Canvas(root,width=640,height=426,bd=0, highlightthickness=0, relief='ridge')
# #キャンバスを設置(上下に20の余白)
# canvas.pack(pady=20)
# #画像を用意
# photo1=tk.PhotoImage(file='cat1.png')
# #画像を描画(中点x,中点y,画像)
# canvas.create_image(320,213,image=photo1)
# photo2=tk.PhotoImage(file='cat2.png')
# canvas.create_image(340,233,image=photo2)
# root.mainloop()


#     root = tkinter.Tk()
#     root.geometry('1270x270')
#     q1 = tkinter.Label(root,text='このポケモンだ～れだ！')

# 問題と答えのリスト
questions = [
   {'image':'pika1.png','answer':'A'},
   {'image':'question2.png','answer':'B'},
   {'image':'question1.png','answer':'A'},
   {'image':'question1.png','answer':'A'}
]

# 問題のインデックス
current_question=0

# 問題をシャッフル
# random.shuffle(questions)

# 問題を表示する関数
def show_question(lavel):
    global current_question
    # print("test")
    # question = questions[current_question]
    # image_path = question['image']
    image = Image.open("pikat2.png")
    
    image2 = image.resize((200,200))
    image3=ImageTk.PhotoImage(image2)
    lavel["image"] = image3
    # answer = question["answer"]
    # image_label = tk.Label()
    # window = tk.Tk()
    # window.geometry('1280x720')
   
    
    # image_label = tk.Label(window)
  
    # answer_entry = tk.Entry(window)
   


# 画像を表示する

    # image_label.configure(image=tk.PhotoImage(file=image_path))
    # image_label.image = tk.PhotoImage(file=image_path)

# 答えのテキストボックスを表示
    # answer_entry.delete(0,tk.END)


# 答えチェック
def check_answer():
                window = tk.Tk()
                result_label = tk.Label(window)
                answer_entry = tk.Entry(window)
                user_answer = answer_entry.get()
                correct_answer = questions[current_question]['answer']
                if user_answer == correct_answer:
                         result_label.configure(text='正解！',fg='green')
                else:
                         result_label.configure(text='不正解!',fg='red')

# 次の問題
                next_question()

def next_question():
        global current_question 
        current_question +=1

        # 全ての問題が終了した場合
        if current_question >= len(questions):
                image_label.configure(image='')
                image_label.image = None
                answer_entry.delete(0,tk.END)

                answer_entry.contigure(state= 'disabled')
                check_button.configure(state='disabled')
                result_label.configure(text='クイズ終了！')
                
        else:
            show_question()

        # ｔｋウインドウを作成
        window = tk.Tk()
        # window.geometry('1280x720')

        # 画像を表示するラベル
        image_label = tk.Label(window)
        image_label.pack(pady=10)

        # 結果を表示するラベル
        result_label = tk.Label(window)
        result_label.pack(pady=10)

        # 答えのテキストボックス
        answer_entry = tk.Entry(window,font=('Arial,12'))
        answer_entry.pack(pady=10)

        # 答えをチェックするボタン
        check_button = tk.Button(window,text='答えをチェック',command = check_answer)
        check_button.pack(pady=10)

        # 最初の問題を表示
        show_question()

        # ウインドウを表示
# show_question(lavel)

window.mainloop()
