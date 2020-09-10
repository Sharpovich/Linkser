import tkinter as tk
import URLUtils as m
from tkinter.filedialog import askopenfilename
import os


def openFile():
    filename = askopenfilename(
        parent=root,
        title="Файл для обработки ссылок и выгрузки в папку",
        initialdir=os.getcwd()
    )
    m.main_Func(filename)
    return filename


if __name__ == '__main__':
    root = tk.Tk()
    root.title("Linkser")
    root.geometry('400x200+300+300')
    root.resizable(width=False, height=False)
    frame = tk.Frame(root, bg="#ffb700", bd=5)
    frame.place(relx=0.15, rely=0.15, relwidth=0.7, relheight=0.30)
    Label2 = tk.Label(frame, text="Выберите файл, что бы начать обработку: ", bg="#ffb700").pack()
    tk.Button(root, text="файл", width=20,
              command=openFile,
              bg="#ffb700"
              ).place(height="70", width="100", x=150, y=100)
    root.mainloop()
