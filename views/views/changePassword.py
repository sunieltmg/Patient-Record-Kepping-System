from tkinter import *
from tkinter import ttk, messagebox
from classes.system_classes import *


class ChangingPassword:
    """This class enables us to change password"""

    def __init__(self):
        self.top = Toplevel()
        self.top.title('Change Password')
        self.top.geometry('450x320+400+150')
        self.top.resizable(False, False)
        self.admin = Admin()

        label_title = Label(self.top, text='Change your password',
                            font=('helvetica', 15, 'bold'),
                            bg='black', fg='white', pady=5)
        label_title.pack(fill=X)

        username_label = Label(self.top, text='Username',
                               font=('helvetica', 10))
        username_label.place(x=74, y=80)
        self.username_entry = Entry(self.top, font=('helvetica', 10),
                                    width=30)
        self.username_entry.place(x=170, y=80)

        old_password_label = Label(self.top, text='Old Password',
                                   font=('helvetica', 10))
        old_password_label.place(x=54, y=120)
        self.old_password_entry = Entry(self.top, font=('helvetica', 10),
                                        width=30)
        self.old_password_entry.place(x=170, y=120)

        new_password_label = Label(self.top, text='New Password',
                                   font=('helvetica', 10))
        new_password_label.place(x=50, y=160)
        self.new_password_entry = Entry(self.top, font=('helvetica', 10),
                                        width=30, show="*")
        self.new_password_entry.place(x=170, y=160)

        confirm_password_label = Label(self.top, text='Confirm Password',
                                       font=('helvetica', 10))
        confirm_password_label.place(x=30, y=200)
        self.confirm_password_entry = Entry(self.top, font=('helvetica', 10),
                                            width=30, show="*")
        self.confirm_password_entry.place(x=170, y=200)

        btn_ok = Button(self.top, text='OK', font=('helvetica', 15), width=8,
                        command=self.change_password,
                        activebackground='black', activeforeground='white')
        btn_ok.place(x=170, y=250)

        btn_cancel = Button(self.top, text='Cancel', font=('helvetica', 15),
                            width=8, command=self.cancel,
                            activebackground='black',
                            activeforeground='white')
        btn_cancel.place(x=285, y=250)
        self.top.mainloop()

    def change_password(self):
        userName = self.username_entry.get()
        old_password = self.old_password_entry.get()
        new_password = self.new_password_entry.get()
        confirm_password = self.confirm_password_entry.get()

        if userName == "" or old_password == "" or new_password == "" or \
                confirm_password == "":
            messagebox.showerror('ERROR', 'All Fields are required',
                                 parent=self.top)
        elif self.admin.change_username(userName, old_password):
            self.updated()
        else:
            messagebox.showerror('ERROR', 'Username or password not matched',
                                 parent=self.top)

    def updated(self):
        userName = self.username_entry.get()
        old_password = self.old_password_entry.get()
        new_password = self.new_password_entry.get()
        confirm_password = self.confirm_password_entry.get()

        if new_password != confirm_password:
            messagebox.showerror('ERROR', 'New Password not matched',
                                 parent=self.top)
        elif self.admin.change_password(new_password, userName,
                                        old_password):
            messagebox.showinfo('SUCESS', 'Password udapted successfully',
                                parent=self.top)

    def cancel(self):
        self.top.destroy()


if __name__ == "__main__":
    ChangingPassword()
    print(ChangingPassword.__doc__)
