import tkinter as tk
import URLUtils as m

def obrfabitka(event):
    pass


root = tk.Tk()
root.title("Linkser")
root.geometry('600x400+300+300')
root.resizable(width=False, height=False)

frame = tk.Frame(root, bg="#ffb700", bd=5)
frame.place(relx=0.15, rely=0.15, relwidth=0.7, relheight=0.30)

Label2 = tk.Label(frame, text="Выберите файл: ", bg="#ffb700").pack()

tk.Button(root, text="Обработать",
          width=20, command=m.main_Func).place(height="30", width="200", x=200, y=160)

#статус бар
StatusBar = tk.Label()
StatusBar.place(x=30, y=200)

root.mainloop()

