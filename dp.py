import sqlite3
class Database:
    def __init__(self,db):
       self.con=sqlite3.connect(db)
       self.cur=self.con.cursor()
       qry="""
       create table if not exists employee(
       id integer primary key,
       name text,
       age text,
       doj text,
       gender text
       )
       """
       self.cur.execute(qry)
       self.con.commit()
    def insert(self,name,age,doj,gender ):
        self.cur.execute("Insert into employee values (NULL,?,?,?,?)",(name,age,doj,gender))
        self.con.commit()
    def fetch(self):
        self.cur.execute("select * from employee")
        row=self.cur.fetchall()
        return (row)

    def remove(self,id):
        self.cur.execute("Delete From employee where id=?",(id,))
        self.con.commit()

    def update(self,id,name,age,doj,gender):
        self.cur.execute("update employee set name=?,age=?,doj=?,gender=? where id=?",(name,age,doj,gender,id))
        self.con.commit()





"""
  1.create\h
insert into user (value) values (values)
  2.update
update users set value1=?,value2=?,value3=?, where id=?
  3.select 
select * from Users
  4.delect 
delet from users where id=?


"""




