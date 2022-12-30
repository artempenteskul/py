import tkinter as tk

from tkinter.messagebox import showinfo


class Gui(tk.Frame):
    def __init__(self, parent=None):
        tk.Frame.__init__(self, parent)
        button = tk.Button(self, text='PRESS', command=self.reply)
        button.pack()

    @staticmethod
    def reply():
        showinfo(title='POPUP', message='BUTTON PRESSED')


if __name__ == '__main__':
    window = Gui()
    window.pack()
    window.mainloop()
