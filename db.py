import sqlite3
class Database:
    def __init__(self,db):
        self.con = sqlite3.connect(db)
        self.cur = self.con.cursor()


        sql = """
        CREATE TABLE IF NOT EXISTS employees(
            id Integer Primary Key,
            name text,
            age text,
            jop text,
            email text,
            gender text,
            contact text,
            address text
        )
        """
        self.cur.execute(sql)
        self.con.commit()

    def insert(self,name,age,jop,email,gender,contact,address):
        self.cur.execute("insert into employees values (null,?,?,?,?,?,?,?)",
                         (name,age,jop,email,gender,contact,address))
        self.con.commit()
    
    def fetch(self):
        self.cur.execute("SELECT * FROM employees ")
        rows = self.cur.fetchall()
        return rows
    
    def remove(self,id):
        self.cur.execute("delete from employees where id=? ",(id,))
        self.con.commit()

    def update(self,id,name,age,jop,email,gender,contact,address):
        self.cur.execute("update employees set name=?,age=?,email=?,jop=?,gender=?,contact=?,address=? where id=?",
                         (name,age,jop,email,gender,contact,address, id))
        self.con.commit()