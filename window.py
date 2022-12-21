from tkinter import *
from PIL import Image, ImageTk
import main



root = Tk()

root.geometry('480x555')
root.config(bg="#4e586e")
root.minsize(480, 555)
root.maxsize(480, 555)
root.title("ChatBot",)

root.iconbitmap(r'imgs/img.ico')

logo = (Image.open("imgs/img.png"))
resized_logo = logo.resize((50, 50), Image.ANTIALIAS)
new_logo = ImageTk.PhotoImage(resized_logo)

logoLabel = Label(root, text="Welcome\nI am Bob", font=("Rosewood Std Fill", 16, 'bold'), padx=5, image=new_logo,
                  compound='left', bg='#4e586e', fg='white')
logoLabel.pack(pady=5)

centerFrame = Frame(root)
centerFrame.pack()

scrollBar = Scrollbar(centerFrame)
scrollBar.pack(side=RIGHT, fill=Y)


textArea = Text(centerFrame, font=("Helvetica", 16), height=18, width=37, yscrollcommand=scrollBar.set, wrap='word',
                state=DISABLED, bg="#242A38")
textArea.pack(side=LEFT)
scrollBar.config(command=textArea.yview)


question = Entry(root, font=('Helvetica', 16,), bd=0.5)
question.place(x=50, y=510, height=30, width=383)
question.bind('<Return>', main.enter)

sendImg = (Image.open("imgs/send.png"))
resized_sendImg = sendImg.resize((40, 40), Image.ANTIALIAS)
new_sendImg = ImageTk.PhotoImage(resized_sendImg)

exitImg = (Image.open("imgs/exit.png"))
resized_exitImg = exitImg.resize((40, 40), Image.ANTIALIAS)
new_exitImg = ImageTk.PhotoImage(resized_exitImg)

sendButton = Button(root, image=new_sendImg, bg='#4e586e', bd=0, activebackground='#4e586e', command=main.botreply)
sendButton.place(x=432, y=505)

exitButton = Button(root, image=new_exitImg, bg='#4e586e', bd=0, activebackground='#4e586e', command=main.close)
exitButton.place(x=6, y=506)
textArea.tag_config('u', foreground="white")
textArea.tag_config('b', foreground="#f78361")

root.mainloop()
