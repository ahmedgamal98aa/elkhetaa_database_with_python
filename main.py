from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from db import Database 
db = Database("Employee.db") 



root = Tk()
root.title("Employee Mangment System-elkheta vl01")
root.geometry("1245x615+0+0")
root.resizable(False,False)
root.configure(bg="#EEE8AA")

name = StringVar()
age = StringVar()
jop = StringVar()
gender = StringVar()
email = StringVar()
contact = StringVar()


logo = PhotoImage(file="11.png")
lbl_logo = Label(root,image=logo)
lbl_logo.place( x=30, y=520, height=80, width=250)



#=========== entrie frame=======
entries_frame = Frame(root,bg="#2c3e50")
entries_frame.place(x=1,y=1,width=360,height=510)
title = Label(entries_frame, text="Employees-elkheta" , font=("calibri",18,"bold" ), bg="#2c3e50",fg="white")
title.place(x=10,y=1)

lbalName = Label(entries_frame,text="Name", font=("calibri",16, ), bg="#2c3e50",fg="white") 
lbalName.place(x= 10 , y=50)
txtName = Entry(entries_frame,textvariable =name,width=20,font=("calibri",16, ), bg="white",fg="#2c3e50")
txtName.place(x=120,y=50)

lbaljop = Label(entries_frame,text="Jop", font=("calibri",16, ), bg="#2c3e50",fg="white") 
lbaljop.place(x= 10 , y=90)
txtjop = Entry(entries_frame,textvariable =jop,width=20,font=("calibri",16, ), bg="white",fg="#2c3e50")
txtjop.place(x=120,y=90)

lbalGender = Label(entries_frame,text="Gender", font=("calibri",16, ), bg="#2c3e50",fg="white") 
lbalGender.place(x= 10 , y=130)
comogender = ttk.Combobox(entries_frame,textvariable =gender,state="readonly", width=18,font=("calibri",16, ))
comogender["values"] = ("Female "," Male ") 
comogender.place(x=120, y=130)

lbalage = Label(entries_frame,text="Age", font=("calibri",16, ), bg="#2c3e50",fg="white") 
lbalage.place(x= 10 , y=170)
txtage = Entry(entries_frame,textvariable =age,width=20,font=("calibri",16, ), bg="white",fg="#2c3e50")
txtage.place(x=120,y= 170)

lbalemail = Label(entries_frame,text="Email", font=("calibri",16, ), bg="#2c3e50",fg="white") 
lbalemail.place(x= 10 , y=210)
txtemail = Entry(entries_frame,textvariable =email,width=20,font=("calibri",16, ), bg="white",fg="#2c3e50")
txtemail.place(x=120,y= 210)

lbalecontact = Label(entries_frame,text="Contact", font=("calibri",16, ), bg="#2c3e50",fg="white") 
lbalecontact.place(x= 10 , y=250)
txtcontact = Entry(entries_frame,textvariable =contact,width=20,font=("calibri",16, ), bg="white",fg="#2c3e50")
txtcontact.place(x=120,y= 250)

lbaleAddress = Label(entries_frame,text="Address :", font=("calibri",16, ), bg="#2c3e50",fg="white") 
lbaleAddress.place(x= 10 , y=290)
txtAddress = Text(entries_frame, width=30 , height=2,font=("calibri",16, ), bg="white",fg="#2c3e50")
txtAddress.place(x= 10, y=330)


#=========== define frame=======

def hide():
    root.geometry("363x510+0+0")
def show():
    root.geometry("1245x615+0+0")

btnhide = Button(entries_frame,text="Hide data",command=hide,bg="#C71565",width=9,font=("calibri",11,"bold" ),cursor="hand2",bd=1,relief=SOLID)
btnhide.place(x=206,y=10)

btnshow = Button(entries_frame,text="Show data",command=show,bg="#BC8F8F",width=8,font=("calibri",11,"bold" ),cursor="hand2",bd=1,relief=SOLID)
btnshow.place(x=288,y=10)

def getdata(event):
    selected_row = tv.focus()
    data = tv.item(selected_row)
    global row
    row = data["values"]
    name.set(row[1])
    age.set(row[2])
    jop.set(row[3])
    email.set(row[4])
    gender.set(row[5])
    contact.set(row[6])
    txtAddress.insert(END,row[7])

def delet():
    db.remove(row[0])
    clear()
    displayAll()
    messagebox.showinfo("Success","delete all employee data (fe dhea)")


  

def clear():
    name.set("")
    age.set("")
    jop.set("")
    gender.set("")
    email.set("")
    contact.set("")
    txtAddress.delete(1.0,END)



def displayAll():
    tv.delete(*tv.get_children())
    for row in db.fetch():
        tv.insert("",END,values=row)

def add_employee():
    if txtName.get() == "" or txtage.get()=="" or txtAddress.get(1.0,END)=="" or txtcontact.get()=="" or txtemail.get()=="" or txtjop.get()=="" or comogender.get()=="" :
        messagebox.showerror("Error","please fill all the Entry (focus !!)")
        return
    db.insert(
        txtName.get(),
        txtage.get(),
        txtjop.get(),
        txtemail.get(),
        comogender.get(),
        txtcontact.get(),
        txtAddress.get(1.0,END) )
    messagebox.showinfo("Success","added a new employee(yaaa mraaaheb)")
    clear()
    displayAll()
def update():
     if txtName.get() == "" or txtage.get()=="" or txtAddress.get(1.0,END)=="" or txtcontact.get()=="" or txtemail.get()=="" or txtjop.get()=="" or comogender.get()=="" :
        messagebox.showerror("Error","please fill all the Entry")
        return 
     db.update(row[0],
             txtName.get(),
             txtage.get(),
             txtjop.get(),
             txtemail.get(),
             comogender.get(),
             txtcontact.get(),
             txtAddress.get(1.0,END))
     messagebox.showinfo("Success","the employee data is ubdated")
     clear()
     displayAll()









#=========== buttons frame======= 
btn_frame = Frame(entries_frame, bg="#EEE8AA", bd=1,relief=SOLID)
btn_frame.place(x=10, y=400,width=335,height=100)

btnadd = Button(btn_frame, 
                text="Add Details",
                width=14,
                height=1,
                font=("calibri",16, ), 
                bg="#16a085",
                fg="white",
                bd=0,
                cursor="hand2",
                command=add_employee
).place(x=4,y=5)


btnedit = Button(btn_frame, 
                text="Update Details",
                width=14,
                height=1,
                font=("calibri",16, ), 
                bg="#2980b9",
                fg="white",
                bd=0,
                cursor="hand2",
                command=update
).place(x=4,y=50)

btndelet = Button(btn_frame, 
                text="Delet Details",
                width=14,
                height=1,
                font=("calibri",16, ), 
                bg="#c0392b",
                fg="white",
                bd=0,
                cursor="hand2",
                command=delet
).place(x=170,y=5)

btnclear = Button(btn_frame, 
                text="clear Details",
                width=14,
                height=1,
                font=("calibri",16, ), 
                bg="#f39c12",
                fg="white",
                bd=0,
                cursor="hand2",
                command= clear
                
).place(x=170,y=50)

#=============table frame=============
tree_frame = Frame(root, bg="white") 
tree_frame.place(x=365, y=1,width=875, height=610)
style =ttk.Style()
style.configure("mystyle.Treeview",font=("calibri",13),rowheight=50)
style.configure("mystyle.Treeview.Heading",font=("calibri",13))
 

tv = ttk.Treeview(tree_frame, columns=(1,2,3,4,5,6,7,8),style="mystyle.Treeview")
tv.heading("1", text="ID")
tv.column("1",width=40)
tv.heading("2", text="Name")
tv.column("2",width=140)
tv.heading("3", text="Age")
tv.column("3",width=50)
tv.heading("4", text="Email")
tv.column("4",width=120)
tv.heading("5", text="Jop")
tv.column("5",width=150)
tv.heading("6", text="Gendre")
tv.column("6",width=90)
tv.heading("7", text="Contact")
tv.column("7",width=150)
tv.heading("8", text="Address")
tv.column("8",width=150)
tv["show"] = "headings"
tv.bind("<ButtonRelease-1>",getdata)
tv.place(x=1,y=1,height=610,width=875)
displayAll()




root.mainloop()