from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from classes.system_classes import *


class PatientApp:
    """"This class contains patient details"""

    def __init__(self):
        self.window = Tk()
        self.window.title('Patient Record Keeping System')
        self.window.geometry('1100x600+200+50')
        self.window.config(bg='lightgray')
        self.window.resizable(False, False)
        self.window.iconbitmap("patient.ico")
        self.patient = Patient()
        self.update_index = ""

        software_title = Label(self.window,
                               text='Patient Record Keeping System',
                               font=('times new roman', 15, 'bold italic'),
                               bg='lightgray')
        software_title.place(x=400, y=5)

        search_title = Label(self.window, text='Search By:',
                             font=('Helvetica', 10, 'bold'),
                             bg='lightgray')
        search_title.place(x=320, y=40)

        self.option_combo = ttk.Combobox(self.window, font=('Helvetica', 10),
                                         width=15, state='readonly')
        self.option_combo['value'] = ["name", 'email', 'contact_no']
        self.option_combo.current(1)
        self.option_combo.place(x=410, y=40)

        self.value_entry = Entry(self.window, font=('Helvetica', 10))
        self.value_entry.place(x=600, y=40)

        self.search_button = Button(self.window, text='SEARCH',
                                    font=('Helvetica', 10, 'bold'),
                                    command=self.search_data,
                                    activebackground="black",
                                    activeforeground='white', bd=1,
                                    relief=RIDGE)
        self.search_button.place(x=800, y=40)

        self.show_all_button = Button(self.window, text='ShowAll',
                                      font=('Helvetica', 10, 'bold'),
                                      command=self.show_all,
                                      activebackground="black",
                                      activeforeground='white', bd=1,
                                      relief=RIDGE)
        self.show_all_button.place(x=900, y=40)

        self.left_frame = Frame(self.window, height=500, width=400, bg='black')
        self.left_frame.place(x=10, y=80)

        self.left_frame_title = Label(self.left_frame, text='Add Information',
                                      bg='black', fg='white',
                                      font=('times new roman', 15, 'bold '))
        self.left_frame_title.place(x=130, y=10)

        self.patient_name = Label(self.left_frame, text='Name', bg='black',
                                  fg='white',
                                  font=('times new roman', 15, 'bold '))
        self.patient_name.place(x=20, y=50)
        self.patient_name_entry = Entry(self.left_frame,
                                        font=('times new roman', 15, 'bold '),
                                        width=20)
        self.patient_name_entry.place(x=120, y=50)

        self.patient_age = Label(self.left_frame, text='Age', bg='black',
                                 fg='white', font=('times new roman', 15,
                                                   'bold '))
        self.patient_age.place(x=20, y=90)
        self.patient_age_entry = Entry(self.left_frame,
                                       font=('times new roman', 15, 'bold '),
                                       width=20)
        self.patient_age_entry.place(x=120, y=90)

        self.patient_email = Label(self.left_frame, text='Email',
                                   bg='black', fg='white',
                                   font=('times new roman', 15, 'bold '))
        self.patient_email.place(x=20, y=130)
        self.patient_email_entry = Entry(self.left_frame,
                                         font=('times new roman', 15, 'bold '),
                                         width=20)
        self.patient_email_entry.place(x=120, y=130)

        self.patient_contact = Label(self.left_frame, text='Contact',
                                     bg='black',
                                     fg='white',
                                     font=('times new roman', 15, 'bold '))
        self.patient_contact.place(x=20, y=170)
        self.patient_contact_entry = Entry(self.left_frame,
                                           font=('times new roman', 15,
                                                 'bold '),
                                           width=20)
        self.patient_contact_entry.place(x=120, y=170)

        self.patient_gender = Label(self.left_frame, text='Gender', bg='black',
                                    fg='white',
                                    font=('times new roman', 15, 'bold '))
        self.patient_gender.place(x=20, y=210)
        self.patient_gender_check = ttk.Combobox(self.left_frame,
                                                 font=('times new roman', 15,
                                                       'bold'),
                                                 width=18,
                                                 state='readonly')
        self.patient_gender_check['values'] = ['Male', 'Female', 'Other']
        self.patient_gender_check.current(0)
        self.patient_gender_check.place(x=120, y=210)

        self.patient_department = Label(self.left_frame, text='DEP', bg='black',
                                        fg='white',
                                        font=('times new roman', 15, 'bold '))
        self.patient_department.place(x=20, y=250)
        self.patient_department_check = ttk.Combobox(self.left_frame,
                                                     font=('times new roman',
                                                           15,
                                                           'bold'), width=18,
                                                     state='readonly')
        self.patient_department_check['values'] = ['Noraml ward',
                                                   'Emergency', 'Operation',]
        self.patient_department_check.current(0)
        self.patient_department_check.place(x=120, y=250)

        self.patient_address = Label(self.left_frame, text='Address',
                                     bg='black',
                                     fg='white',
                                     font=('times new roman', 15, 'bold '))
        self.patient_address.place(x=20, y=290)
        self.patient_address_text = Text(self.left_frame, width=25, height=3)
        self.patient_address_text.place(x=120, y=290)

        self.add_patient_btn = Button(self.left_frame, text='ADD', bg='white',
                                      fg='black',
                                      font=('times new roman', 15, 'bold '),
                                      width=5, command=self.add_patient)
        self.add_patient_btn.place(x=15, y=380)

        self.update_patient_btn = Button(self.left_frame, text='UPDATE',
                                         bg='white', fg='black',
                                         font=('times new roman', 15, 'bold '),
                                         width=7, command=self.update_patient)
        self.update_patient_btn.place(x=95, y=380)

        self.delete_patient_btn = Button(self.left_frame, text='DELETE',
                                         bg='white', fg='black',
                                         font=('times new roman', 15, 'bold '),
                                         width=7, command=self.delete_patient)
        self.delete_patient_btn.place(x=200, y=380)

        self.clear_patient_btn = Button(self.left_frame, text='CLEAR',
                                        bg='white', fg='black',
                                        font=('times new roman', 15, 'bold '),
                                        width=6,
                                        command=self.clear_box)
        self.clear_patient_btn.place(x=300, y=380)

        self.logout_patient_btn = Button(self.left_frame, text='Exit',
                                       bg='white',
                                       fg='black',
                                       font=('times new roman', 15, 'bold '),
                                       width=5,
                                         command=self.logout_patient)
        self.logout_patient_btn.place(x=15, y=440)

        self.right_frame = Frame(self.window, bg='black')
        self.right_frame.place(x=420, y=80, height=500, width=650, )

        self.scroll_x = ttk.Scrollbar(self.right_frame, orient=HORIZONTAL)
        self.scroll_y = ttk.Scrollbar(self.right_frame, orient=VERTICAL)
        self.patient_tree = ttk.Treeview(self.right_frame,
                                         column=('name', 'age', 'email',
                                                 'contact', 'gender', 'DEP',
                                                 'Address'))

        self.scroll_x.config(command=self.patient_tree.xview)
        self.scroll_y.config(command=self.patient_tree.yview)
        self.scroll_x.pack(side=BOTTOM, fill=X)
        self.scroll_y.pack(side=RIGHT, fill=Y)
        self.patient_tree.config(xscrollcommand=self.scroll_x.set,
                                 yscrollcommand=self.scroll_y.set)

        self.patient_tree['show'] = 'headings'
        self.patient_tree.heading('name', text='Name')
        self.patient_tree.heading('age', text='Age')
        self.patient_tree.heading('email', text='Email')
        self.patient_tree.heading('contact', text='Contact')
        self.patient_tree.heading('gender', text='Gender')
        self.patient_tree.heading('DEP', text='Department')
        self.patient_tree.heading('Address', text='Address')
        self.patient_tree.pack(fill=BOTH, expand=1)
        self.show_patient_in_tree()

        self.window.mainloop()

    def add_patient(self):
        self.interface_value()
        if self.name == "" or self.age == "" or self.email == "" or \
                self.contact == "" or \
                self.gender == "" or self.department == "" or \
                self.address == "":
            messagebox.showerror('ERROR', 'All fields are required')
            return False
        else:
            try:
                isinstance(int(self.age), int)
            except ValueError:
                messagebox.showerror('ERROR', 'only numbers are allowed')
                return

        if self.patient.add_patient(self.name, self.age, self.email,
                                    self.contact, self.gender,
                                    self.department,
                                    self.address):
            messagebox.showinfo('patient', 'patient added successfully')
            self.show_patient_in_tree()
            self.clear_box()
        else:
            messagebox.showerror('Error', 'Student not added')

    def show_patient_in_tree(self):
        data = self.patient.view_patient()
        self.patient_tree.delete(*self.patient_tree.get_children())
        for i in data:
            self.patient_tree.insert("", "end", text=i[0], values=(i[1],
                                                                   i[2], i[3],
                                                                   i[4], i[5],
                                                                   i[6], i[7]))

        self.patient_tree.bind("<Double-1>", self.select_data)

    def select_data(self, event):
        self.selected_row = self.patient_tree.selection()[0]
        self.update_index = self.patient_tree.item(self.selected_row, 'text')
        self.selected_value = self.patient_tree.item(self.selected_row, 'values')
        self.patient_name_entry.delete(0, END)
        self.patient_name_entry.insert(0, self.selected_value[0])

        self.patient_age_entry.delete(0, END)
        self.patient_age_entry.insert(0, self.selected_value[1])

        self.patient_email_entry.delete(0, END)
        self.patient_email_entry.insert(0, self.selected_value[2])

        self.patient_contact_entry.delete(0, END)
        self.patient_contact_entry.insert(0, self.selected_value[3])

        self.patient_gender_check.delete(0, END)
        self.patient_gender_check.insert(0, self.selected_value[4])

        self.patient_department_check.set(value="")
        self.patient_department_check.set(value=self.selected_value[5])

        self.patient_address_text.delete('1.0', END)
        self.patient_address_text.insert(1.0, self.selected_value[6])

    def interface_value(self):
        self.name = self.patient_name_entry.get()
        self.age = self.patient_age_entry.get()
        self.email = self.patient_email_entry.get()
        self.contact = self.patient_contact_entry.get()
        self.gender = self.patient_gender_check.get()
        self.department = self.patient_department_check.get()
        self.address = self.patient_address_text.get('1.0', END)

    def clear_box(self):
        self.patient_name_entry.delete(0, END)
        self.patient_age_entry.delete(0, END)
        self.patient_email_entry.delete(0, END)
        self.patient_contact_entry.delete(0, END)
        self.patient_gender_check.delete(0, END)
        self.patient_department_check.delete(0, END)
        self.patient_address_text.delete(1.0, END)

    def update_patient(self):
        self.interface_value()
        if self.update_index == "":
            messagebox.showerror('ERROR', 'Select an patient to update '
                                          'detail first')
            return False

        if self.name == "" or self.age == "" or self.email == "" or \
                self.contact == "" or \
                self.gender == "" or self.department == "" or \
                self.address == "":
            messagebox.showerror('ERROR', 'All fields are required')
            return False
        else:
            try:
                isinstance(int(self.age), int)
            except ValueError:
                messagebox.showerror('ERROR', 'only numbers are allowed')
                return

        if self.patient.update_patient(int(self.update_index), self.name,
                                       self.age, self.email, self.contact,
                                       self.gender, self.department,
                                       self.address):
            messagebox.showinfo('UPDATE', 'patient detail is '
                                          'updated successfully')
            self.clear_box()
            self.show_patient_in_tree()
            self.update_index == ""

        else:
            messagebox.showerror('ERROR', 'patient detail addition failed')

    def delete_patient(self):
        self.interface_value()
        if self.update_index == "":
            messagebox.showerror('ERROR', 'Select an patient to update'
                                          ' detail first')
            return False

        if self.patient.delete_patient(int(self.update_index)):
            messagebox.showinfo('DELETE', 'patient detail is deleted'
                                          ' successfully')
            self.clear_box()
            self.show_patient_in_tree()

        else:
            messagebox.showerror('ERROR', 'patient detail deletion failed')

    def search_data(self):
        option = self.option_combo.get()
        value = self.value_entry.get()

        if option == "" or value == "":
            messagebox.showerror('ERROR', 'All fields are required')
            return False

        else:
            data = self.patient.search_patient(option, value)
            self.patient_tree.delete(*self.patient_tree.get_children())
            if len(data) >= 1:
                for detail in data:
                    self.patient_tree.insert("", 'end', text=detail[0],
                                             values=(detail[1], detail[2],
                                                     detail[3], detail[4],
                                                     detail[5], detail[6],
                                                     detail[7]))

                    self.patient_tree.bind("<Double-1>", self.select_data)
            else:
                messagebox.showerror('ERROR', 'FIELD NOT FOUND')

    def show_all(self):
        self.show_patient_in_tree()

    def logout_patient(self):
        self.window.destroy()


if __name__ == "__main__":
    PatientApp()
