import tkinter as tk
from PIL import Image 
import random

class qapp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('ランダム画像切り替えクイズ')
        self.geometry('400x400')

        self.images = [
        {'image':'pika1.png','answer':'A'},
        {'image':'question2.png','answer':'B'},
        {'image':'question1.png','answer':'A'},
        {'image':'question1.png','answer':'A'}
]
    
        self.current_image = None
        self.correct_answer = None

        self.image_label = tk.Label(self)
        self.image_label.pack(pady=10)

        self.answer_entry = tk.Entry(self)
        self.answer_entry.pack(pady=10)

        # self.submit_button = tk.Button(self,text='答えを送信',command = self.check_answer)
        
        self.submit_button = tk.Button(self,text='答えを送信')
        self.submit_button.pack(pady=10)







        self.new_question()

    

    def new_question(self):
        self.currect_image = random.choice(self.images)
        self.correct_answer = self.get_answer(self.current_image)

        image = Image.open(self.current_image)
        image = image.resize((300,300))
        self.photo = tk.PhotoImage(image)

        self.image_label.config(image = self.photo)

    def check_answer(self):
        user_answer = self.answer_entry.get()

        if user_answer.lower() == self.correct_answer.lower():
            result ='正解'
        else:
            result ='不正解'

        self.answer_entry.delete(0,tk.END)
        self.new_question()

        result_label = tk.Label(self,text=result)
        result_label.pack(pady=10)

def get_answer(self,image):
    return image.split('','')[0][0]


if __name__ == '__main__':
        app = qapp()
        app.mainloop()
