import mysql.connector
import tkinter as tk

# تابع برای اتصال به پایگاه داده SQL Server
myDB = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="class")

con = myDB.cursor()


def insert_Data():
    Name = entry_Name.get()
    LastName = entry_LastName.get()
    age = entry_age.get()

    try:
        sql = "insert into class (Name,LastName,age) values (%s,%s,%s)"
        var = (Name, LastName, age)
        con.execute(sql, var)
        myDB.commit()
    except:
        myDB.rollback()
        print("Error")


def update_Data():
    Name = entry_Name.get()
    LastName = entry_LastName.get()
    age = entry_age.get()

    try:
        vals = (Name, LastName, age)
        sql_query = (''' UPDATE Data
                set Name=%s, LastName=%s,age=%s
                WHERE LastName=%s
                ''')
        con.execute(sql_query, vals)
        myDB.commit()
    except:
        myDB.rollback()
        print('Error')


# Deleting a data
def delete_Data():
    LastName = entry_Name.get()
    age = entry_age.get()
    try:
        delete_query = f''' delete  from  book  where LastName ={LastName}'''
        con.execute(delete_query, )
        myDB.commit()
        print("done")

    except:
        myDB.rollback()
        print("Error")


def show_Data():
    con.execute('''select * from class''')
    result = con.fetchone()
    for x in result:
        print(x[0])


def clear_Data():
    entry_Name.delete(0, tk.END)
    entry_LastName.delete(0, tk.END)
    entry_age.delete(0, tk.END)


root = tk.Tk()
root.title('Class Database')

label_Name = tk.Label(root, text='Name:')
label_LastName = tk.Label(root, text='LastName:')
label_age = tk.Label(root, text='age:')

entry_Name = tk.Entry(root)
entry_LastName = tk.Entry(root)
entry_age = tk.Entry(root)

listbox = tk.Listbox(root, width=40, height=10)
button_insert = tk.Button(root, text='add', command=insert_Data)
button_update = tk.Button(root, text='Update', command=update_Data)
button_delete = tk.Button(root, text='Delete', command=delete_Data)
button_show = tk.Button(root, text='show', command=show_Data)

# قرار دادن ویجت‌ها در صفحه

label_Name.grid(row=0, column=0)
label_LastName.grid(row=1, column=0)
label_age.grid(row=2, column=0)

entry_Name.grid(row=0, column=1)
entry_LastName.grid(row=1, column=1)
entry_age.grid(row=2, column=1)

listbox.grid(row=15, column=0, columnspan=2)
button_insert.grid(row=9, column=0)
button_update.grid(row=10, column=0)
button_delete.grid(row=8, column=0)
button_show.grid(row=11, column=0)
root.mainloop()
