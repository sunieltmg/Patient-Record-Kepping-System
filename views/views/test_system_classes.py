import unittest
from classes.system_classes import *


class TestPatientData(unittest.TestCase):
    """Performs testing of different functions"""
    admin = Admin()
    patient = Patient()

    def test_add_patient1(self):
        result = self.patient.add_patient('Nishma', 19, 'nishma@gmail.com', '1234567890', 'female', 'Emergency',
                                          'Butwal')
        self.assertIs(result, True)

    def test_add_patient2(self):
        result = self.patient.add_patient('', 19, 'nishma@gmail.com', '1234567890', 'female', 'Emergency', 'Butwal')
        self.assertIs(result, False)

    def test_update_patient1(self):
        result=self.patient.update_patient(1,'Nishma',19,'nishma@gmail.com','1234567890','female','Emergency', 'Butwal')
        self.assertIs(result,True)

    def test_update_patient2(self):
        result=self.patient.update_patient(1,'', 19, 'nishma@gmail.com','1234567890','female','Emergency', 'Butwal')
        self.assertIs(result,False)

    def test_delete_patient1(self):
        result=self.patient.delete_patient(4)
        self.assertIs(result,True)

    def test_delete_patient2(self):
        result=self.patient.delete_patient("")
        self.assertIs(result,False)

    def test_change_password1(self):
        result=self.admin.change_password('123','abc','Nepali')
        self.assertIs(result,True)

    def test_change_password2(self):
        result=self.admin.change_password('','Nepali','Nepali')
        self.assertIs(result,False)

    def test_delete_user1(self):
        result=self.admin.delete_user('123')
        self.assertIs(result,True)

    def test_delete_user2(self):
        result=self.admin.delete_user("")
        self.assertIs(result,False)


if __name__ == "__main__":
    unittest.main()
