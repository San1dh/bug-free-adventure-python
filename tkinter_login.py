from tkinter import *
from tkinter import messagebox

class login_interface(Frame):
    def __init__(self, master = None):
        Frame.__init__(self, master)
        self.master = master
        self.security()

    def security(self):
        self.master.title("login")
        self.master['background'] = '#000'
        self.pack(fill = BOTH, expand = 1)
        lbl = Label(self).grid(column = 0, row = 0)
        lbl = Label(self, text = "username").grid(column = 1, row = 1)
        lbl = Label(self, text = "password").grid(column = 1, row = 2)

        self.username = Entry(self)
        self.username.focus_set()
        self.username.grid(column = 2, row = 1)
                                            
        self.pwrd = Entry(self, show = "*")
        self.pwrd.focus_set()
        self.pwrd.grid(column = 2, row = 2)

        login = Button(self, text = "login", width = 20, bg = '#2652ff', fg = 'grey', command = self.login)
        login.grid(column = 2, row = 3)

    def login(self):
        if self.pwrd.get() == "12345678" and self.username.get() == "harry stylez":
            messagebox.showinfo("login", "login successful")
        else:
            messagebox.showinfo("error", "login failed, retype username/password")

window = Tk()
window.geometry("400x300")
app = login_interface(window)
app.mainloop()
