from tkinter import *
import backend

def get_selected_row(event):
    try:
        global selectedTouple
        index=list1.curselection()[0]
        selectedTouple=list1.get(index)
        e1.delete(0,END)
        e1.insert(END,selectedTouple[1])
        e2.delete(0,END)
        e2.insert(END,selectedTouple[2])
        e3.delete(0,END)
        e3.insert(END,selectedTouple[3])
        e4.delete(0,END)
        e4.insert(END,selectedTouple[4])
    except IndexError:
        pass    


def view_command():
    list1.delete(0,END)
    for row in backend.view():
        list1.insert(END,row)

def search_command():
    list1.delete(0,END)
    for row in backend.search(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()):
        list1.insert(END,row)

def add_command():
    backend.insert(title_text.get(),author_text.get(),year_text.get(),isbn_text.get())
    list1.delete(0,END)
    tc=title_text.get()
    ac=author_text.get()
    yc=year_text.get()
    ic=isbn_text.get()
    list1.insert(END,(f"{tc,ac,yc,ic}"))

def delete_command():
    backend.delete(selectedTouple[0])

def update_command():
    backend.update(selectedTouple[0],title_text.get(),author_text.get(),year_text.get(),isbn_text.get())
    
root=Tk()
root.title("Book store")
# p1=PhotoImage(file='download.jpg')
# root.iconphoto(False,p1)
#root.geometry("744x465")

l1=Label(root,text='Title')
l1.grid(row=0,column=0)

l2=Label(root,text='Author')
l2.grid(row=0,column=2)

l3=Label(root,text='Year')
l3.grid(row=1,column=0)

l4=Label(root,text='ISBN')
l4.grid(row=1,column=2)

title_text=StringVar()
e1=Entry(root,textvariable=title_text)
e1.grid(row=0,column=1)

author_text=StringVar()
e2=Entry(root,textvariable=author_text)
e2.grid(row=0,column=3)

year_text=StringVar()
e3=Entry(root,textvariable=year_text)
e3.grid(row=1,column=1)

isbn_text=StringVar()
e4=Entry(root,textvariable=isbn_text)
e4.grid(row=1,column=3)

list1=Listbox(root,height=6,width=35)
list1.grid(row=2,column=0,rowspan=6,columnspan=2)

sb1=Scrollbar(root)
sb1.grid(row=2,column=2,rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind("<<ListboxSelect>>",get_selected_row)

b1=Button(root,text='View all',width=12, command=view_command)
b1.grid(row=2,column=3)

b2=Button(root,text='Search entry',width=12,command=search_command)
b2.grid(row=3,column=3)

b3=Button(root,text='Add entry',width=12,command=add_command)
b3.grid(row=4,column=3)

b4=Button(root,text='Update selected',width=12,command=update_command)
b4.grid(row=5,column=3)

b5=Button(root,text='Delete selected',width=12,command=delete_command)
b5.grid(row=6,column=3)

b6=Button(root,text='Close',width=12,command=root.destroy)
b6.grid(row=7,column=3)

root.mainloop()
