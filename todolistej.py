#Example of to do list:

##Modifications to apply for habit forming app:

"""
format:
different pages 1 for: (also add)
    - starting level: 3 levels.
    - actual task selection (which task you are going to do next)
    - task timer for pomodoro system.
    - notes on task pop up??
    - sub tasks on tasks?
Level bar and exp gain
    
functionality:
    - include timer
    - include intial level (backscene)
    - not allow repeating tasks.

Possibles:    
    - notes on tasks?
checkbox done
non repeating tasks
"""

"""
modifications for begginer app:
addTask recognizes blanks and doesnt act on them.


"""
#Imports:
from cProfile import label
import tkinter
from tkinter import *
from turtle import color
import re


#Structure/Format

root = Tk()
root.title("To-Do-List")
root.configure(background="grey25")
root.geometry("400x650+400+100")
root.resizable(False,False)
root.counter = 0

##Specifying the list:
task_list=[]

##Operating:

def addTask():
    task=task_entry.get()
    task2 = re.sub(r"\s+", "", task, flags=re.UNICODE)
    task_entry.delete(0,END)
    
    if task2 == "":
        pass
    elif task:
        with open("tasklist.txt","r+") as taskfile:
            if task not in taskfile:
                taskfile.write(f"\n{task}")
                task_list.append(task)
                listbox.insert(END,task)


def deleteTask():
    global task_list
    task = str(listbox.get(ANCHOR))
    if task in task_list:
        task_list.remove(task)
        with open("tasklist.txt","w") as taskfile:
            for task in task_list:
                taskfile.write(task+"\n")
        listbox.delete(ANCHOR)    

def openTaskFile():

    try:
        global task_list
        with open("tasklist.txt","r") as taskfile:
            tasks = taskfile.readlines()
            
        for task in tasks:
            if task != '\n':
                task_list.append(task)
                listbox.insert(END, task)
    except:
        file=open("tasklist.txt","w")
        file.close()

def updatecounter():
    root.counter += 1
    heading3['text'] = 'Completed today: ' + str(root.counter)




#PNGs and labels:
##App icon image
Image_icon=PhotoImage(file="images/task.png")
root.iconphoto(False,Image_icon)
##top bar (blue)
TopImage=PhotoImage(file="images/topbar1.png")
Label(root,image=TopImage).pack()
##Tasks icon: change for changing completed number with changing numbers (new def()).
noteImage=PhotoImage(file="images/task.png")
Button(root,image=noteImage,bg="#32405b",command=updatecounter).place(x=340,y=120)

##Title of the app front page:
heading=Label(root,text="OPEN QUESTS",font="Stencil 20 bold", fg= "red",bg="grey25")
heading.place(x=110,y=100)
heading2=Label(root,text="LEVEL 1",font="Stencil 20 bold", fg= "dark red",bg="dark goldenrod1")
heading2.place(x=153,y=20)
heading3=Label(root,text="Completed today: 0" + str(root.counter),font = "arial 10 bold",fg="red",bg="grey25")
heading3.place(x=5,y=150)
##deletion mechanism:
Delete_icon=PhotoImage(file="images/delete.png")
Button(root,image=Delete_icon,bd=0,command=deleteTask).pack(side=BOTTOM,pady=13)


#main
##Input box:
frame=Frame(root,width=400,height=50,bg="white")
frame.place(x=0,y=180)
##String input:
task=StringVar()
task_entry=Entry(frame,width=18,font="arial 20",bd=0)
task_entry.place(x=10,y=7)
task_entry.focus()
##Add task button:
button=Button(frame,text="ADD",font="arial 20 bold",width=6, bg="#5a95ff",fg="#fff",bd=0,command=addTask)
button.place(x=300,y=0)
##Listbox:
frame1=Frame(root,bd=3,width=700,height=280,bg="#32405b")
frame1.pack(pady=(160,0))
listbox=Listbox(frame1,font=("arial",12),width=40,height=16,bg="#32405b",fg="white",cursor="hand2",selectbackground="#5a95ff")
listbox.pack(side=LEFT,fill=BOTH,padx=2)
##Scrollbar:
scrollbar=Scrollbar(frame1)
scrollbar.pack(side = RIGHT,fill=BOTH)
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

openTaskFile()
                       


                 

root.mainloop()

#To check:
