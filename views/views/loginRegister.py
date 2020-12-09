from tkinter import *
from tkinter import messagebox
from classes.system_classes import *
from views.connection import *
from views.app import *
from views.admin import *



class LoginRegister:
    """In this class we register a user first then login with
    that username and password"""

    def __init__(self):
        self.window = Tk()
        self.myConnection = MyConnection()
        self.window.geometry('700x500+200+100')
        self.window.title('Login window')
        self.window.config(bg="black")
        self.window.iconbitmap("login.ico")

        self.admin=Admin()
        self.username = Label(self.window, text='Username',
                              font=('helvetica', 15),
                              padx=50, fg="white",
                              bg="black")
        self.username.place(x=120, y=50)
        self.username_entry_1 = Entry(self.window, font=('helvetica', 15),
                                      width=20)
        self.username_entry_1.place(x=300, y=50)

        password = Label(self.window, text='password',
                         font=('helvetica', 15),
                         padx=50, fg="white",
                         bg="black")
        password.place(x=120, y=100)
        self.password_entry_1 = Entry(self.window, width=20,
                                      font=('helvetica', 15))
        self.password_entry_1.place(x=300, y=100)

        self.login = Button(self.window, text='Login',
                            command=self.login_value,
                            font=('helvetica', 15),
                            width=15)
        self.login.place(x=300, y=200)

        self.register = Button(self.window, text='Register',
                               command=self.register_window,
                               font=('helvetica', 15),
                               width=15)
        self.register.place(x=300, y=300)

        self.window.mainloop()

    def register_window(self):
        self.window = Tk()
        self.window.title('Register window')
        self.window.geometry('700x500+200+100')
        self.window.config(bg="black")
        self.window.iconbitmap('login.ico')

        username = Label(self.window, text='Username',
                         font=('helvetica', 15),
                         padx=50, fg="white",
                         bg="black"
                         )
        username.place(x=120, y=50)
        self.username_entry_2 = Entry(self.window,
                                      font=('helvetica', 15),
                                      width=20)
        self.username_entry_2.place(x=300, y=50)

        password = Label(self.window, text='password',
                         font=('helvetica', 15),
                         padx=50, fg="white",
                         bg="black"
                         )
        password.place(x=120, y=100)
        self.password_entry_2 = Entry(self.window,
                                      font=("helvetica", 15),
                                      width=20)
        self.password_entry_2.place(x=300, y=100)

        self.register = Button(self.window, text='Register',
                               command=self.reg_value,
                               font=('helvetica', 15),
                               width=20)
        self.register.place(x=300, y=200)

    def reg_value(self):
        user = self.username_entry_2.get()
        password = self.password_entry_2.get()
        username_list=self.check_username()
        qry = "insert into registration(username,password)" \
              " values(%s,%s)"
        value = (user, password)
        if user == "" or password == "":
            messagebox.showerror('ERROR', "ALL FIELDS ARE REQUIRED")
            return False

        elif self.check_username_binary_search(username_list, user):
            messagebox.showerror('ERROR', 'User already exists,'
                                          'try another username',parent=self.window)
            return False

        else:
            self.myConnection.iud(qry, value)
            messagebox.showinfo('REGISTER', 'REGISTRATION SUCCESS')
            self.window.destroy()

    def login_value(self):
        user = self.username_entry_1.get()
        password = self.password_entry_1.get()
        qry = "select * from registration where username=%s and" \
              " password=%s"
        value = (user, password)
        data1=self.admin.get_user()
        data = self.myConnection.get_data_p(qry, value)
        print(len(data))

        if user == "" or password == "":
            messagebox.showerror('ERROR', "ALL FIELDS ARE REQUIRED")
        else:
            if len(data) == 1:
                if data[0][2] == 'admin':
                    self.window.destroy()
                    AdminView()

                else:
                    self.window.destroy()
                    PatientApp()

            else:
                messagebox.showerror('ERROR', ' password or username is'
                                              ' incorrect')

    def check_username_binary_search(self, username_list, key):
        lower = 0
        upper = len(username_list) - 1
        while lower <= upper:
            mid_value = (lower + upper) // 2
            if username_list[mid_value][0] == key:
                return True

            elif key > username_list[mid_value][0]:
                lower = mid_value + 1
            else:
                upper = mid_value - 1

        return False


    def check_username(self):
        qry="select username from registration"
        data=self.myConnection.get_data(qry)
        return data


if __name__ == "__main__":
    LoginRegister()
