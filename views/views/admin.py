from tkinter import *
from tkinter import ttk, messagebox
from views.changePassword import *
from classes.system_classes import *


class AdminView:
    """"This class performs admin level tasks like changing employee status,
     deleting employee and changing password"""

    def __init__(self):
        self.window = Tk()
        self.window.title('Admin Panel')
        self.window.geometry('1250x650+0+0')
        self.window.resizable(False, False)
        self.window.config(bg='gray')
        self.window.iconbitmap("admin.ico")
        self.admin = Admin()

        title = Label(self.window, text='Welcome to Admin section',
                      bg="lightgray", pady=5,
                      font=('helvetica', 15, 'bold'))
        title.pack(fill=BOTH)

        change_password = Button(self.window, text='Change Password',
                                 font=('times new roman', 15, 'bold'),
                                 bg='white', fg='black', width=30,
                                 command=self.change_pass)
        change_password.place(x=450, y=100)

        change_status = Button(self.window,
                               text='Change Employee Status',
                               font=('times new roman', 15, 'bold'),
                               bg='white', fg='black', width=30,
                               command=self.change_user)
        change_status.place(x=450, y=250)

        remove_employee = Button(self.window, text='Remove Employee',
                                 font=('times new roman', 15, 'bold'),
                                 bg='white', fg='black', width=30,
                                 command=self.remove_user)
        remove_employee.place(x=450, y=400)

        self.window.mainloop()

    def change_pass(self):
        ChangingPassword()

    def change_user(self):
        self.top = Toplevel()
        self.top.title('Change Status')
        self.top.geometry('450x320+400+150')
        self.top.resizable(False, False)

        label_title = Label(self.top, text='Change Employee Status',
                            font=('helvetica', 15, 'bold'),
                            bg='black', fg='white', pady=5)
        label_title.pack(fill=X)

        username_label = Label(self.top, text='Select Employee',
                               font=('helvetica', 10))
        username_label.place(x=74, y=80)
        self.user_combo = ttk.Combobox(self.top, font=('helvetica', 10),
                                       width=30)
        self.user_combo.place(x=170, y=80)

        self.change_status = Label(self.top, text='Employee Type',
                                   font=('helvetica', 10))
        self.change_status.place(x=74, y=150)
        self.type_combo = ttk.Combobox(self.top, font=('helvetica', 10),
                                       width=30)
        self.type_combo['values'] = ['user', 'admin']
        self.type_combo.place(x=170, y=150)

        self.change_status = Button(self.top, text='Change Status',
                                    font=('helvetica', 15),
                                    width=13, command=self.change_user_status)
        self.change_status.place(x=100, y=250)

        btn_cancel = Button(self.top, text='Cancel',
                            font=('helvetica', 15),
                            width=8, command=self.cancel)
        btn_cancel.place(x=285, y=250)

        self.combo_user_value()
        self.top.mainloop()

    def change_user_status(self):
        data = self.admin.get_user()
        user = self.user_combo.get()
        type = self.type_combo.get()
        if user == "" or type == "":
            messagebox.showerror('ERROR', 'All fields are required',
                                 parent=self.top)
            return True

        if self.admin.change_user(type, user):
            messagebox.showinfo('CHANGED', 'User status is changed'
                                           ' sucessfully',
                                parent=self.top)

        else:
            messagebox.showerror('ERROR', 'User is not changed',
                                 parent=self.top)

    def combo_user_value(self):
        user = []
        data = self.admin.get_user()
        for data in data:
            user.append(data[0])

        self.user_combo['values'] = user

    def cancel(self):
        self.top.destroy()

    def remove_user(self):
        self.top = Toplevel()
        self.top.title('Remove')
        self.top.geometry('450x320+400+150')
        self.top.resizable(False, False)

        label_title = Label(self.top, text='Remove password',
                            font=('helvetica', 15, 'bold'),
                            bg='black', fg='white',
                            pady=5)
        label_title.pack(fill=X)

        self.username_label = Label(self.top, text='Select User',
                                    font=('helvetica', 10))
        self.username_label.place(x=74, y=80)

        self.user_combo = ttk.Combobox(self.top, font=('helvetica', 10),
                                       width=30)
        self.user_combo.place(x=170, y=80)

        delete = Button(self.top, text='Delete User',
                        font=('helvetica', 15), width=13,
                        command=self.delete_user)
        delete.place(x=100, y=250)

        btn_cancel = Button(self.top, text='Cancel',
                            font=('helvetica', 15), width=8,
                            command=self.cancel)
        btn_cancel.place(x=285, y=250)

        self.combo_user_value()

        self.top.mainloop()

    def delete_user(self):
        user = self.user_combo.get()
        if user == "":
            messagebox.showerror('ERROR', 'Select a user to delete',
                                 parent=self.top)
            return False
        if self.admin.delete_user(user):
            messagebox.showinfo('DELETE', 'User is deleted successfully')
        else:
            messagebox.showerror('ERROR', 'Username is not deleted')


if __name__ == "__main__":
    AdminView()
