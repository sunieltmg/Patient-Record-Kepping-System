import mysql.connector
from tkinter import messagebox


class MyConnection:
    """Performs tasks like establishing databases connection and
    passing SQL query"""

    def __init__(self):
        try:
            self.my_connection = mysql.connector.connect(user='root',
                                                         passwd='Myjcdgg123kcda'
                                                                'bkcdpb456',
                                                         host='localhost',
                                                         database='patient_record_keeping_system')
            self.cur = self.my_connection.cursor()

        except Exception as e:
            messagebox.showerror('ERROR', f"Error occured due to: {str(e)}")

    def iud(self, qry, values):
        try:
            self.cur.execute(qry, values)
            self.my_connection.commit()
            return True
        except Exception as e:
            messagebox.showerror('ERROR', f"Error occured due to: {str(e)}")
            return False

    def get_data(self, qry):
        try:
            self.cur.execute(qry)
            data = self.cur.fetchall()
            return data
        except Exception as e:
            messagebox.showerror('ERROR', f"Error occured due to: {str(e)}")
            return False

    def get_data_p(self, qry, values):
        try:
            self.cur.execute(qry, values)
            data = self.cur.fetchall()
            return data
        except Exception as e:
            messagebox.showerror('ERROR', f"Error occured due to: {str(e)}")
            return False


if __name__ == "__main__":
    MyConnection()
