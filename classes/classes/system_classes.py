from views.connection import *


class Patient:
    """Performs tasks like add/update/delete/search patient"""

    def __init__(self):
        self.my_connection = MyConnection()

    def add_patient(self, name, age, email, contact, gender, dep, address):
        try:
            if name=="" or age=="" or email=="" or contact=="" or\
                    gender=="" or dep=="" or address=="":
                return False

            qry = "insert into patient_detail(name,age,email,contact,gender," \
                  "dep,address) values(%s,%s,%s,%s,%s,%s,%s)"
            value = (name, age, email, contact, gender, dep, address)
            self.my_connection.iud(qry, value)
            return True
        except Exception as e:
            print(e)
            return False

    def view_patient(self):
        qry = "select * from patient_detail"
        data=self.my_connection.get_data(qry)
        return data

    def update_patient(self, updateIndex, name, age, email, contact, gender,
                       dep, address):

        try:
            if updateIndex=="" or name=="" or age=="" or email=="" or contact==""\
                    or gender=="" or dep=="" or address=="":
                return False
            qry = "update patient_detail set name=%s, age=%s, email=%s, contact=%s," \
                  " gender=%s, dep=%s, address=%s where patient_id=%s"
            values = (name, age, email, contact, gender, dep, address, updateIndex)
            self.my_connection.iud(qry, values)
            return True
        except Exception as e:
            print(e)
            return False

    def delete_patient(self, updateIndex):
        try:
            if updateIndex=="":
                return False
            qry = "delete from patient_detail where patient_id=%s"
            values = (updateIndex,)
            self.my_connection.iud(qry, values)
            return True
        except Exception as e:
            print(e)
            return False

    def search_patient(self, option, value):
        qry = "select * from patient_detail where" + " " + option + " " + "LIKE '" \
                                                                           "" + value + "'"
        data = self.my_connection.get_data(qry)
        return data


class Admin:
    """This class contains query related to admin functionality"""

    def __init__(self):
        self.my_connection = MyConnection()

    def change_username(self, username, password):
        qry = "select username from registration where username=%s and" \
              " password=%s"
        values = (username, password)
        data = self.my_connection.get_data_p(qry, values)
        length = len(data)
        return length

    def change_password(self, password, username, oldPassword):
        try:
            if password=="" or username=="" or oldPassword=="":
                return False
            qry = "update registration set password=%s where username=%s " \
                  "and password=%s"
            values = (password, username, oldPassword)
            self.my_connection.iud(qry, values)
            return True
        except Exception as e:
            print(e)
            return False

    def get_user(self):
        qry = "select * from registration"
        data = self.my_connection.get_data(qry)
        return data

    def change_user(self, type, user):
        try:
            if type == "" or user == "":
                return False
            qry = "update registration set type=%s where username=%s"
            values = (type, user)
            self.my_connection.iud(qry, values)
            return True

        except Exception as e:
            print(e)
            return False

    def delete_user(self, user):
        try:
            if user == "":
                return False
            qry = "delete from registration where username=%s"
            values = (user,)
            self.my_connection.iud(qry, values)
            return True

        except Exception as e:
            print(e)
            return False


if __name__ == "__main__":
    Patient()
