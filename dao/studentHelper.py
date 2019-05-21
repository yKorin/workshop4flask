import cx_Oracle

from dao.db import OracleDb


class UserHelper:

    def __init__(self):
        self.db = OracleDb()




    def newUser(self, student_name,student_age):

        cursor = self.db.cursor


        status = cursor.var(cx_Oracle.STRING)

        cursor.callproc("STD.NEW_STUDENT", [ status,student_name,student_age])

        return  status.getvalue()

    def deleteStudent(self,student_name):

        cursor = self.db.cursor

        status = cursor.var(cx_Oracle.STRING)

        cursor.callproc("STD.DELETE_STUDENT",[status,student_name])
        return status.getvalue()

    def getAllUsers(self):
        cursor = self.db.cursor
        query = 'SELECT * from student '

        cursor.execute(query)
        result = cursor.fetchall()


        return result






if __name__ == "__main__":

    helper = UserHelper()

    print(helper.newUser('gjhasdfgj','22222'))
    print(helper.getAllUsers())



