from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from dp import Database
db=Database("employee.db")
root=Tk()
root.title("Employee Management System")
root.geometry("1366x768+0+0")
root.config(bg='#2c3e50')
root.state('zoomed')

name= StringVar()
age= StringVar()
doj= StringVar()
gender= StringVar()

entries_frame=Frame(root,bg='#535c68')
entries_frame.pack(side=TOP,fill=X)

title= Label(entries_frame,text="Employee Management System",font=('colabric',15,'bold'),bg='#535c68',fg='white')
title.grid(row=0,columnspan=2,padx=10,pady=20)

lblname=Label(entries_frame,text='Name',font=('colabric',15),bg='#535c68',fg='white')
lblname.grid(row=1,column=0,padx=10,pady=20,sticky='w')
txtname=Entry(entries_frame,textvariable=name,font=('colabric',15))
txtname.grid(row=1,column=1,padx=10,pady=20,sticky='w')

lblage=Label(entries_frame,text="age",font=('colabric',15),bg='#535c68',fg='white')
lblage.grid(row=1,column=2,padx=10,pady=10,sticky='w')
txtage=Entry(entries_frame,textvariable=age,font=('colabric',15))
txtage.grid(row=1,column=3,padx=10,pady=10,sticky='w')

lbldoj=Label(entries_frame,text="D.O.B",font=("colabric",15,),bg='#535c68',fg='white')
lbldoj.grid(row=2,column=0,sticky='w')
txtdoj=Entry(entries_frame,textvariable=doj,font=("colabric",15,))
txtdoj.grid(row=2,column=1,padx=10,pady=10,sticky='w')

lblgender=Label(entries_frame,text="Gender",font=("colabric",15),bg='#535c68',fg='white')
lblgender.grid(row=2,column=2,sticky='w')
combogender=ttk.Combobox(entries_frame,font=("colabic",16),width=20,textvariable=gender,state="readonly")
combogender['value']=('Male','Female','Others')
combogender.grid(row=2,column=3,pady=10)

def getdata(event):
    select_values=tv.focus()
    data=tv.item(select_values)
    global row
    row=data["values"]
    #print(row)
    name.set(row[1])
    age.set(row[2])
    doj.set(row[3])
    gender.set(row[4])
def display():
    tv.delete(*tv.get_children())
    for row in db.fetch():
        tv.insert("",END,values=row)


def add_employee():
    if txtname.get() == "" or txtage.get() =="" or txtdoj.get()=="" or combogender.get()=="" :
        messagebox.showerror("Error in Input","Fill All Details")
        return
    db.insert( txtname.get(),txtage.get(),txtdoj.get(),combogender.get())
    messagebox.showinfo("success","Record Inserted")
    clear_employee()
    display()


def edit_employee():
    if txtname.get()== "" or txtage.get()== "" or txtdoj.get()== "" or combogender.get()== "":
        messagebox.showerror("Error in Input","Please Fill  All Details")
    db.update(row[0],txtname.get(), txtage.get(), txtdoj.get(), combogender.get())
    messagebox.showinfo("success", "Record Details Updated")
    clear_employee()
    display()

def delete_employee():
    db.remove(row[0])
    clear_employee()
    display()



def clear_employee():
    name.set("")
    age.set("")
    doj.set("")
    gender.set("")

btn_frame=Frame(entries_frame,bg='#535c68')
btn_frame.grid(row=3,column=0,columnspan=4,padx=10,pady=10,sticky='w')
btnAdd = Button(btn_frame,command=add_employee,text='Add Details',width=20,font=("colibri",15,'bold'),bg='#079992',fg='white').grid(row=0,column=0)
btnEdit = Button(btn_frame,command=edit_employee,text="Update Details",width=20,font=("colibri",15,'bold'),bg='#38ada9',fg='white').grid(row=0,column=1,padx=10)
btndelete=Button(btn_frame,command=delete_employee,text='Delete Details',width=20,font=('colibri',15,'bold'),bg='#16a085',fg='white').grid(row=0,column=2,padx=10)
btnclear=Button(btn_frame,command=clear_employee,text='Clear Details',width=20,font=('colibri',15,'bold'),bg='#1abc9c',fg='white').grid(row=0,column=3,padx=10)

style_frame=ttk.Style()
style_frame.configure("mystyle.Treeview",font=("colabric",'15'),rowheight=50)
style_frame.configure("mystyle.Treeview.Heading",font=("colabric",15))

tree_frame = Frame(root,bg='#ecf0f1')
tree_frame.place(x=0,y=250,width=1366,height=520)
tv=ttk.Treeview(tree_frame,columns=(1,2,3,4,5),style=("mystyle.Treeview"))
tv.heading('1',text='ID')
tv.column("1",width=10)
tv.heading('2',text='Name')
tv.heading('3',text="Age")
tv.heading('4',text='D.O.J')
tv.heading('5',text="Gender")
tv['show'] = 'headings'
tv.bind("<ButtonRelease-1>",getdata)
tv.pack(fill=X)

display()
display()
root.mainloop()


"""
btn_frame=Frame(entries_frame,bg='#535c68')
btn_frame.grid(row=3,column=0,padx=10,pady=10,sticky,sticky='w')
btn_Add=Button(btn_frame,command='add_employee',widht=20,font=('colibri',15,'bold'),bg='#16a085',fb='white')
"""