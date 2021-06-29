import mysql.connector as connector


class DBHelper:  # create when operations are performed
    def __init__(self):  # simple constuctor created
        self.con = connector.connect(host='localhost',  # requirements for connecting with mysql
                                     port='3306',
                                     user='root',
                                     password='9850',
                                     database='pythontest')
        # query created
        query = 'create table if not exists user(userID int primary key,userName varchar(200),phone varchar(12))'
        # To call query we need constuctor i.e Self.con  and called fuction curser
        cur = self.con.cursor()
        cur.execute(query)
        print("Created")

    # Insert
    def insert_user(self, userID, userName, phone):
        query = "insert into user(userID,userName,phone) values({},'{}','{}')".format(
            userID, userName, phone)  # method created
        print(query)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("user saved to db")

    # Fetch all
    def fetch_all(self):
        query = "select * from user"
        cur = self.con.cursor()
        cur.execute(query)
        for row in cur:
            print("UserID:", row[0])
            print("UserName:", row[1])
            print("PhoneNo:", row[2])
            print()

    # delete
    def delete_user(self, userID):
        query = "DELETE FROM user WHERE userID={}".format(userID)
        print(query)
        c = self.con.cursor()
        c.execute(query)
        self.con.commit()
        print("Deleted")

    # update
    def update_user(self, userID, newName, newPhone):
        query = "UPDATE user SET userName='{}',phone='{}' WHERE userID={}".format(
            newName, newPhone, userID)
        print(query)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("Updated")