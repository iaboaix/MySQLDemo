# -*- coding: UTF-8 -*-
from tkinter import *
from tkinter import messagebox,simpledialog
import pymysql


class MyDialog(simpledialog.Dialog):
    def body(self, master):
        Label(master, text="ip:").grid(row=0)
        Label(master, text="database:").grid(row=1)
        Label(master, text="username:").grid(row=2)
        Label(master, text="password:").grid(row=3)
        self.e1 = Entry(master)
        self.e2 = Entry(master)
        self.e3 = Entry(master)
        self.e4 = Entry(master)

        self.e1.grid(row=0, column=1)
        self.e2.grid(row=1, column=1)
        self.e3.grid(row=2, column=1)
        self.e4.grid(row=3, column=1)
        return(self.e1)

    def apply(self):
        ip = str(self.e1.get())
        database = str(self.e2.get())
        username=str(self.e3.get())
        password=str(self.e4.get())
        global db
        db = pymysql.connect(host = '127.0.0.1', port = 3306, user = 'root', password = '0000', db = 'db_school', charset = 'utf8')
        global cursor
        ## you need to implement connection operation here ##

        sql = '''SHOW TABLES'''
        try:
            cursor = db.cursor()
            # 执行sql语句
            cursor.execute(sql)
            # 提交到数据库执行
            db.commit()
            results = cursor.fetchall()
            var2.set(tuple(results))
        except:
            # Rollback in case there is any error
            db.rollback()
            print('error')
	


def on_click_connect():
	d = MyDialog(root)

def on_click_execute():
    ## you need to implement all the command here, if it is select sentence, you need to 
    ##  show all the contents of the table in the list box
    sql = entryi.get()
    try:
        cursor = db.cursor()
        # 执行sql语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
        results = cursor.fetchall()
        var3.set(tuple(results))
    except:
        # Rollback in case there is any error
        db.rollback()
        print('error')
    return
def low(x):
    return x.lower()
def on_click_fresh():
    ## you need to implement fresh database here ##
    return 

def about():  
    print('I am developer')

root = Tk(className="SqlWindow")
root.geometry("700x650")

frmLT = Frame(width=600, height=200)
frmLC = Frame(width=250, height=400)
frmLB = Frame(width=450, height=400)

frmLT.grid(row=0, columnspan=2,padx=1,pady=3)
frmLC.grid(row=1, column=0,padx=1,pady=3)
frmLB.grid(row=1, column=1)


button_connect = Button(frmLT)
button_connect['text'] = 'connect'
button_connect['command'] = on_click_connect
button_connect.grid(row=0, column=0, sticky=E)


label = Label(frmLC)
label['text'] = 'tables in database'
label.grid(sticky=N)


var2 = StringVar()
#var2.set(tuple([test1,test2,test3]))

lb = Listbox(frmLC, width=15, height=5, listvariable=var2)
lb.grid(sticky=N)


button_connect = Button(frmLB)
button_connect['text'] = 'fresh'
button_connect['command'] = on_click_fresh
button_connect.grid(row=0, column=3,sticky=E)

button_connect = Button(frmLB)
button_connect['text'] = 'execute'
button_connect['command'] = on_click_execute
button_connect.grid(row=0, column=2,sticky=E)
entryi=Entry(frmLB)
entryi['textvariable']=""
entryi.grid(row=0, column=1,sticky=E+W+N+S)


label = Label(frmLB)
label['text'] = 'selected table'
label.grid(row=3, column=1,sticky=W)

sql=""""show tables"""

try:
    # 执行SQL语句
    cursor.execute(sql)
    # 获取所有记录列表
    results = cursor.fetchall()
    var3.set(tuple(results))
except:
    print("Error: unable to fecth data")
var3 = StringVar()

lb2 = Listbox(frmLB, width=50, height=25, listvariable=var3)
lb2.grid(row=4, column=1,sticky=E)

root.mainloop()




