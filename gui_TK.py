import tkinter as tk

url = 'https://pg.brandquad.ru/png/ede7c57abbb3991f1ad84e5c3e5bd38a/'

def main_Func():
    Label3["text"] = "{}\n{}".format(text1.get(),text2.get())

root = tk.Tk()
root.title("Linkser")
root.geometry('600x400+300+300')
root.resizable(width=False, height=False)

frame = tk.Frame(root, bg="#ffb700", bd=5)
frame.place(relx=0.15, rely=0.15, relwidth=0.7, relheight=0.30)

Label1 = tk.Label(frame, text="Введите путь до директории или оставьте пустым", bg="#ffb700").pack()

text1 = tk.StringVar()
Text1 = tk.Entry(frame, width="70", bd=3, textvariable=text1)
Text1.pack()

Label2 = tk.Label(frame, text="Введите наименование файла с ссылками", bg="#ffb700").pack()

text2 = tk.StringVar()
Text2 = tk.Entry(frame, width="70", bd=3, textvariable=text2)
Text2.pack()

tk.Button(root, text="Обработать",
       width=20, command=main_Func).place(height="30", width="200", x=200, y=160)

Label3 = tk.Label()
Label3.place(x=30, y=200)

root.mainloop()