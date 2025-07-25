# importing libraries

import pandas as pd
import pymysql as sqlcon
mydb=sqlcon.connect(host="localhost",user="root",passwd="Yesha@2106",database="project")
mycursor=mydb.cursor()

import matplotlib.pyplot as pl
import numpy as np
from playsound import playsound
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

#welcome screen

root=Tk()
root.title("Voting Booth")
root.geometry("1856x1161")

#login screen
     
def login():
    root=Tk()
    root.title("Login")
    root.geometry("650x350")

    my_canvas=Canvas(root,width=500,height=400)
    my_canvas.pack(fill="both",expand=True)

    bg=PhotoImage(file="2.png",master=my_canvas)

    my_canvas.create_image(0,0,image=bg,anchor="nw")

    global entry1
    global entry2

    my_canvas.create_text(110,40,text="Username",font=("Castellar",20),fill="black")
    my_canvas.create_text(110,110,text="Password",font=("Castellar",20),fill="black")

    entry1=Entry(root,font=("Castellar",20),bd=10)
    entry1.place(x=200,y=20)

    entry2=Entry(root,font=("Castellar",20),bd=10,show="*")
    entry2.place(x=200,y=90)


    def enter():
        username=entry1.get()
        password=entry2.get()
        
        if(username=="" or password==""):
            messagebox.showinfo("","Blank Not allowed")
            
        elif(username=="WVM" and password=="7890"):

#select post

            root = Tk()
            root.title("Post")
            root.geometry("1856x1161")

            my_canvas=Canvas(root,width=800,height=500)

            my_canvas.pack(fill="both",expand=True)

            abc=PhotoImage(file="4.png",master=my_canvas)

            my_canvas.create_image(0,0,image=abc,anchor="nw")

            my_canvas.create_text(750,70,text="Select Post",font=("Castellar",90,"bold"),fill="black")

            def headgirl():
                
                #voting for headgirl
                buttona['state']='disabled'
                buttonb['state']='disabled'
                buttonc['state']='disabled'
                buttond['state']='disabled'
                buttone['state']='disabled'
                buttonf['state']='disabled'
                buttong['state']='disabled'

                
                #mycursor.execute("Create table Headgirl (ID int(3),Name varchar(40),Class varchar(30),Age int(3),Votes int(8));")

                #mycursor.execute("insert into headgirl values(1,'Shreya Thakkar','XII COMM',16,0);")
                #mycursor.execute("insert into headgirl values(2,'Srushti Ghunake','XII SCI',16,0);")
                #mycursor.execute("insert into headgirl values(3,'Sreya Pillai','XII SCI',16,0);")

                root1 = Tk()
                root1.title('Head Girl')
                root1.geometry('1856x1161')

                my_canvas=Canvas(root1,width=1856,height=1161)
                my_canvas.pack(fill="both",expand=True)

                bg=PhotoImage(file="4.png",master=my_canvas)

                my_canvas.create_image(0,0,image=bg,anchor="nw")

                my_canvas.create_text(700,50,text="Head Girl",font=("Castellar",80),fill="purple")

                def vote1():
                    
                    #adding votes to database and disabling other buttons with a sound
                    mycursor.execute("update headgirl set votes = votes + 1 where Name = 'Shreya Thakkar';")
                    mydb.commit()
                    button1['state']='disabled'
                    button2['state']='disabled'
                    button3['state']='disabled'
                    playsound('sound.mp3')
                    
                #adding image and details
                a=PhotoImage(file="shreya.png",master=my_canvas)
                my_canvas.create_image(150,220,image=a)
                my_canvas.create_text(470,150,text="Name : Shreya Thakkar",font=("Castellar",20),fill="black")
                my_canvas.create_text(410,200,text="Class : XII COMM",font=("Castellar",20),fill="black")
                button1=Button(root1,text="Vote",font=("Castellar",20),height=1,width=10,command=vote1)
                button1_window=my_canvas.create_window(300,250,anchor="nw",window=button1)

                def vote2():

                    #adding votes to database and disabling other buttons with a sound
                    mycursor.execute("update headgirl set votes = votes + 1 where Name = 'Srushti Ghunake';")
                    mydb.commit()
                    button1['state']='disabled'
                    button2['state']='disabled'
                    button3['state']='disabled'
                    playsound('sound.mp3')

                # adding image and details
                b=PhotoImage(file="srushti.png",master=my_canvas)
                my_canvas.create_image(900,240,image=b)
                my_canvas.create_text(1240,150,text="Name : Srushti Ghunake",font=("Castellar",20),fill="black")
                my_canvas.create_text(1150,200,text="Class : XII SCI",font=("Castellar",20),fill="black")
                button2=Button(root1,text="Vote",font=("Castellar",20),height=1,width=10,command=vote2)
                button2_window=my_canvas.create_window(1070,250,anchor="nw",window=button2)

                def vote3():

                    #adding votes to database and disabling other buttons with a sound
                    mycursor.execute("update headgirl set votes = votes + 1 where Name = 'Sreya Pillai';")
                    mydb.commit()
                    button1['state']='disabled'
                    button2['state']='disabled'
                    button3['state']='disabled'
                    playsound('sound.mp3')

                # adding image and details
                c=PhotoImage(file="sreya.png",master=my_canvas)
                my_canvas.create_image(150,510,image=c)
                my_canvas.create_text(470,450,text="Name : Sreya Pillai",font=("Castellar",20),fill="black")
                my_canvas.create_text(410,500,text="Class : XII SCI",font=("Castellar",20),fill="black")
                button3=Button(root1,text="Vote",font=("Castellar",20),height=1,width=10,command=vote3)
                button3_window=my_canvas.create_window(300,550,anchor="nw",window=button3)
                
                
                def result():

                    #result screen
                    root = Tk()
                    root.title('Password')
                    root.geometry('650x350')

                    my_canvas=Canvas(root,width=650,height=350)
                    my_canvas.pack(fill="both",expand=True)

                    bc=PhotoImage(file="4.png",master=my_canvas)
                    my_canvas.create_image(0,0,image=bc)

                    global entry3

                    my_canvas.create_text(110,40,text="Password",font=("Castellar",20),fill="black")

                    entry3=Entry(root,font=("Castellar",20),bd=10,show="*")
                    entry3.place(x=200,y=20)

                    def enter1():

                        #password checking
                        Password=entry3.get()

                        if Password=="7890":

                            root= Tk()
                            root.title('Head Girl')
                            root.geometry('1012x405')

                            bottomframe=Frame(root)
                            bottomframe.pack(side=BOTTOM)

                            def graph():
                                
                                #graph
                                mycursor.execute("select votes from headgirl;")
                                details=mycursor.fetchall()
                                x=[]
                                y=["Shreya","Sreya","Srushti"]
                                for i in details:
                                    x.append(i[0])
                                pl.title("Head Girl")
                                pl.xlabel("Candidates")
                                pl.ylabel("No. of Votes")
                                pl.bar(y,x)
                                pl.show()

                                                            
                            graph=Button(bottomframe,text="Graph",command=graph,font=("Castellar",20),height=1,width=10)
                            graph.pack()


                            def back():

                                #back to select post
                                buttona['state']='active'
                                buttonb['state']='active'
                                buttonc['state']='active'
                                buttond['state']='active'
                                buttone['state']='active'
                                buttonf['state']='active'
                                buttong['state']='active'
                                enter()
                                
                            back=Button(bottomframe,text="Back",command=back,font=("Castellar",20),height=1,width=10)
                            back.pack()

                            #result table

                            mycursor.execute("Select * from headgirl order by votes desc;")
                            rows=mycursor.fetchall()

                            frn=Frame(root)
                            frn.pack(side=TOP)

                            tv=ttk.Treeview(root)
                            tv.pack()

                            tv["columns"]=("ID","Name","class","age","votes")
                            tv['show']='headings'

                            s=ttk.Style(root)
                            s.theme_use("clam")

                            s.configure(".",font=("Helvetica",15))
                            s.configure("Treeview.Heading",foreground='white',font=("Helvetica",15,"bold"))

                            tv.column("ID",anchor=tk.CENTER)
                            tv.column("Name",anchor=tk.CENTER)
                            tv.column("class",anchor=tk.CENTER)
                            tv.column("age",anchor=tk.CENTER)
                            tv.column("votes",anchor=tk.CENTER)

                            tv.heading("ID",text="ID",anchor=tk.CENTER)
                            tv.heading("Name",text="Name",anchor=tk.CENTER)
                            tv.heading("class",text="class",anchor=tk.CENTER)
                            tv.heading("age",text="age",anchor=tk.CENTER)
                            tv.heading("votes",text="votes",anchor=tk.CENTER)

                            for i in rows:
                                tv.insert('','end',values=i)

                        else:
                            messagebox.showinfo("","Incorrect username or password")

                    
                    button8=Button(root,text="enter",font=("Castellar",20),height=1,width=10,command=enter1)
                    button8_window=my_canvas.create_window(200,200,anchor="nw",window=button8)
            
                button5=Button(root1,text="Result",font=("Castellar",20),height=1,width=10,command=result)
                button5_window=my_canvas.create_window(1300,700,anchor="nw",window=button5)

                def enable():

                    #enables all voting buttons
                    button1['state']='active'
                    button2['state']='active'
                    button3['state']='active'

                button11=Button(root1,text="Enable",font=("Castellar",20),height=1,width=10,command=enable)
                button11_window=my_canvas.create_window(900,700,anchor="nw",window=button11)

                def clear():
                    # clears all the votes added for all candidates after checking password

                            root = Tk()
                            root.title('Password')
                            root.geometry('650x350')

                            my_canvas=Canvas(root,width=650,height=350)
                            my_canvas.pack(fill="both",expand=True)

                            k1=PhotoImage(file="4.png",master=my_canvas)

                            my_canvas.create_image(0,0,image=k1)

                            global entry4

                            my_canvas.create_text(110,40,text="Password",font=("Castellar",20),fill="black")

                            entry4=Entry(root,font=("Castellar",20),bd=10,show="*")
                            entry4.place(x=200,y=20)

                            def enter2():
                                Password=entry4.get()

                                if Password=="7890":
                                    mycursor.execute("update headgirl set votes = 0;")
                                    mydb.commit()
                                    messagebox.showinfo("","votes cleared")

                            button10=Button(root,text="enter",font=("Castellar",20),height=1,width=10,command=enter2)
                            button10_window=my_canvas.create_window(200,200,anchor="nw",window=button10)

               
                button9=Button(root1,text="clear votes",font=("Castellar",20),height=1,width=10,command=clear)
                button9_window=my_canvas.create_window(50,700,anchor="nw",window=button9)

                
                def back():
                    buttona['state']='active'
                    buttonb['state']='active'
                    buttonc['state']='active'
                    buttond['state']='active'
                    buttone['state']='active'
                    buttonf['state']='active'
                    buttong['state']='active'
                    enter()

                button10=Button(root1,text="back",font=("Castellar",20),height=1,width=10,command=back)
                button10_window=my_canvas.create_window(500,700,anchor="nw",window=button10)


                root.mainloop()

            def headboy():

                #voting for headboy

                buttona['state']='disabled'
                buttonb['state']='disabled'
                buttonc['state']='disabled'
                buttond['state']='disabled'
                buttone['state']='disabled'
                buttonf['state']='disabled'
                buttong['state']='disabled'

                #creating table and adding data in database

                #mycursor.execute("Create table Headboy (ID int(3),Name varchar(40),Class varchar(30),Age int(3),Votes int(8));")

                #mycursor.execute("insert into headboy values(1,'Pratham Nandwani','XII COMM',17,0);")
                #mycursor.execute("insert into headboy values(2,'Abhishek Deshmukh','XII SCI',17,0);")
                #mycursor.execute("insert into headboy values(3,'Yash Dhanuka','XII COMM',16,0);")
                #mycursor.execute("insert into headboy values(4,'Ujjwal Rai','XII COMM',18,0);")
                #mydb.commit()

                root1 = Tk()
                root1.title('Head Boy')
                root1.geometry('1856x1161')

                my_canvas=Canvas(root1,width=1856,height=1161)
                my_canvas.pack(fill="both",expand=True)

                bg=PhotoImage(file="4.png",master=my_canvas)

                my_canvas.create_image(0,0,image=bg,anchor="nw")

                my_canvas.create_text(700,50,text="Head Boy",font=("Castellar",80),fill="purple")

                def vote1():
                    
                    #adding votes to database and disabling other buttons with a sound
                    mycursor.execute("update headboy set votes = votes + 1 where Name = 'Pratham Nandwani';")
                    mydb.commit()
                    button1['state']='disabled'
                    button2['state']='disabled'
                    button3['state']='disabled'
                    button4['state']='disabled'
                    playsound('sound.mp3')

                # adding image and details
                a=PhotoImage(file="pratham.png",master=my_canvas)
                my_canvas.create_image(175,210,image=a)
                my_canvas.create_text(520,150,text="Name : Pratham Nandwani",font=("Castellar",20),fill="black")
                my_canvas.create_text(430,200,text="Class : XII COMM",font=("Castellar",20),fill="black")
                button1=Button(root1,text="Vote",font=("Castellar",20),height=1,width=10,command=vote1)
                button1_window=my_canvas.create_window(320,250,anchor="nw",window=button1)

                def vote2():

                    #adding votes to database and disabling other buttons with a sound
                    mycursor.execute("update headboy set votes = votes + 1 where Name = 'Abhishek Deshmukh';")
                    mydb.commit()
                    button1['state']='disabled'
                    button2['state']='disabled'
                    button3['state']='disabled'
                    button4['state']='disabled'
                    playsound('sound.mp3')

                # adding image and details
                b=PhotoImage(file="abhishek.png",master=my_canvas)
                my_canvas.create_image(900,210,image=b)
                my_canvas.create_text(1250,150,text="Name : Abhishek Deshmukh",font=("Castellar",20),fill="black")
                my_canvas.create_text(1140,200,text="Class : XII SCI",font=("Castellar",20),fill="black")
                button2=Button(root1,text="Vote",font=("Castellar",20),height=1,width=10,command=vote2)
                button2_window=my_canvas.create_window(1080,250,anchor="nw",window=button2)

                def vote3():

                    #adding votes to database and disabling other buttons with a sound
                    mycursor.execute("update headboy set votes = votes + 1 where Name = 'Yash Dhanuka';")
                    mydb.commit()
                    button1['state']='disabled'
                    button2['state']='disabled'
                    button3['state']='disabled'
                    button4['state']='disabled'
                    playsound('sound.mp3')

                # adding image and details
                c=PhotoImage(file="yash.png",master=my_canvas)
                my_canvas.create_image(175,510,image=c)
                my_canvas.create_text(500,450,text="Name : Yash Dhanuka",font=("Castellar",20),fill="black")
                my_canvas.create_text(430,500,text="Class : XII COMM",font=("Castellar",20),fill="black")
                button3=Button(root1,text="Vote",font=("Castellar",20),height=1,width=10,command=vote3)
                button3_window=my_canvas.create_window(320,550,anchor="nw",window=button3)

                def vote4():

                    #adding votes to database and disabling other buttons with a sound
                    mycursor.execute("update headboy set votes = votes + 1 where Name = 'Ujjwal Rai';")
                    mydb.commit()
                    button1['state']='disabled'
                    button2['state']='disabled'
                    button3['state']='disabled'
                    button4['state']='disabled'
                    playsound('sound.mp3')

                # adding image and details
                d=PhotoImage(file="ujjwal.png",master=my_canvas)
                my_canvas.create_image(875,510,image=d)
                my_canvas.create_text(1150,450,text="Name : Ujjwal Rai",font=("Castellar",20),fill="black")
                my_canvas.create_text(1140,500,text="Class : XII COMM",font=("Castellar",20),fill="black")
                button4=Button(root1,text="Vote",font=("Castellar",20),height=1,width=10,command=vote4)
                button4_window=my_canvas.create_window(1040,550,anchor="nw",window=button4)

                def result():

                    #result screen
                    root = Tk()
                    root.title('Password')
                    root.geometry('650x350')

                    my_canvas=Canvas(root,width=650,height=350)
                    my_canvas.pack(fill="both",expand=True)

                    purple=PhotoImage(file="1.1.png",master=my_canvas)

                    my_canvas.create_image(0,0,image=purple,anchor="nw")

                    global entry3

                    my_canvas.create_text(110,40,text="Password",font=("Castellar",20),fill="black")

                    entry3=Entry(root,font=("Castellar",20),bd=10,show="*")
                    entry3.place(x=200,y=20)

                    def enter1():

                        #password checking
                        Password=entry3.get()

                        if Password=="7890":

                            root= Tk()
                            root.title('Head Boy')
                            root.geometry('1012x405')

                            bottomframe=Frame(root)
                            bottomframe.pack(side=BOTTOM)

                            def graph():
                                
                                #graph
                                mycursor.execute("select votes from headboy;")
                                details=mycursor.fetchall()
                                x=[]
                                y=["Pratham","Abhishek","Yash","Ujjwal"]
                                for i in details:
                                    x.append(i[0])
                                pl.title("Head Boy")
                                pl.xlabel("Candidates")
                                pl.ylabel("No. of Votes")
                                pl.bar(y,x)
                                pl.show()

                                                            
                            graph=Button(bottomframe,text="Graph",command=graph,font=("Castellar",20),height=1,width=10)
                            graph.pack()
                            
                            
                            def back():

                                #back to select post
                                buttona['state']='active'
                                buttonb['state']='active'
                                buttonc['state']='active'
                                buttond['state']='active'
                                buttone['state']='active'
                                buttonf['state']='active'
                                buttong['state']='active'
                                enter()
                                
                            back=Button(bottomframe,text="Back",command=back)
                            back.pack()

                            #result table

                            mycursor.execute("Select * from headboy order by votes desc;")
                            rows=mycursor.fetchall()

                            frn=Frame(root)
                            frn.pack(side=TOP)

                            tv=ttk.Treeview(root)
                            tv.pack()

                            tv["columns"]=("ID","Name","class","age","votes")
                            tv['show']='headings'

                            s=ttk.Style(root)
                            s.theme_use("clam")

                            s.configure(".",font=("Helvetica",15))
                            s.configure("Treeview.Heading",foreground='white',font=("Helvetica",15,"bold"))

                            tv.column("ID",anchor=tk.CENTER)
                            tv.column("Name",width=250,anchor=tk.CENTER)
                            tv.column("class",anchor=tk.CENTER)
                            tv.column("age",anchor=tk.CENTER)
                            tv.column("votes",anchor=tk.CENTER)

                            tv.heading("ID",text="ID",anchor=tk.CENTER)
                            tv.heading("Name",text="Name",anchor=tk.CENTER)
                            tv.heading("class",text="class",anchor=tk.CENTER)
                            tv.heading("age",text="age",anchor=tk.CENTER)
                            tv.heading("votes",text="votes",anchor=tk.CENTER)

                            for i in rows:
                                tv.insert('','end',values=i)

                        else:
                            messagebox.showinfo("","Incorrect username or password")

                    
                    button8=Button(root,text="enter",font=("Castellar",20),height=1,width=10,command=enter1)
                    button8_window=my_canvas.create_window(200,200,anchor="nw",window=button8)
            
                button5=Button(root1,text="Result",font=("Castellar",20),height=1,width=10,command=result)
                button5_window=my_canvas.create_window(1200,700,anchor="nw",window=button5)

                def enable():

                    #enables all voting buttons
                    button1['state']='active'
                    button2['state']='active'
                    button3['state']='active'
                    button4['state']='active'

                button11=Button(root1,text="Enable",font=("Castellar",20),height=1,width=10,command=enable)
                button11_window=my_canvas.create_window(600,700,anchor="nw",window=button11)

                def clear():

                    #clears all votes added for all candidates after checking password

                            root = Tk()
                            root.title('Password')
                            root.geometry('650x350')

                            my_canvas=Canvas(root,width=650,height=350)
                            my_canvas.pack(fill="both",expand=True)

                            k1=PhotoImage(file="4.png",master=my_canvas)

                            my_canvas.create_image(0,0,image=k1,anchor="nw")

                            global entry4

                            my_canvas.create_text(110,40,text="Password",font=("Castellar",20),fill="black")

                            entry4=Entry(root,font=("Castellar",20),bd=10,show="*")
                            entry4.place(x=200,y=20)

                            def enter2():
                                Password=entry4.get()

                                if Password=="7890":
                                    mycursor.execute("update headboy set votes = 0;")
                                    mydb.commit()
                                    messagebox.showinfo("","votes cleared")

                            button10=Button(root,text="enter",font=("Castellar",20),height=1,width=10,command=enter2)
                            button10_window=my_canvas.create_window(200,200,anchor="nw",window=button10)

               
                button9=Button(root1,text="clear votes",font=("Castellar",20),height=1,width=10,command=clear)
                button9_window=my_canvas.create_window(50,700,anchor="nw",window=button9)

                root.mainloop()

            def deputyheadgirl():
                
                #voting for deputyheadgirl
                
                buttona['state']='disabled'
                buttonb['state']='disabled'
                buttonc['state']='disabled'
                buttond['state']='disabled'
                buttone['state']='disabled'
                buttonf['state']='disabled'
                buttong['state']='disabled'

                #creating table and adding data in database

                #mycursor.execute("Create table deputyheadgirl (ID int(3),Name varchar(40),Class varchar(30),Age int(3),Votes int(8));")

                #mycursor.execute("insert into deputyheadgirl values(1,'Saumya Shringirishi','XI COMM',15,0);")
                #mycursor.execute("insert into deputyheadgirl values(2,'Kirti Donge','XI COMM',15,0);")
                #mycursor.execute("insert into deputyheadgirl values(3,'S. Tanushree Bhat','XI SCI',16,0);")
                #mycursor.execute("insert into deputyheadgirl values(4,'Vidhi Patel','XI SCI',16,0);")
                #mydb.commit()

                root1 = Tk()
                root1.title('Deputy Head Girl')
                root1.geometry('1856x1161')

                my_canvas=Canvas(root1,width=1856,height=1161)
                my_canvas.pack(fill="both",expand=True)

                bg=PhotoImage(file="4.png",master=my_canvas)

                my_canvas.create_image(0,0,image=bg,anchor="nw")

                my_canvas.create_text(700,50,text="Deputy Head Girl",font=("Castellar",80),fill="purple")

                def vote1():

                    #adding votes to database and disabling other buttons with a sound
                    mycursor.execute("update deputyheadgirl set votes = votes + 1 where Name = 'Saumya Shringirishi';")
                    mydb.commit()
                    button1['state']='disabled'
                    button2['state']='disabled'
                    button3['state']='disabled'
                    button4['state']='disabled'
                    playsound('sound.mp3')

                # adding image and details
                a=PhotoImage(file="saumya.png",master=my_canvas)
                my_canvas.create_image(150,220,image=a)
                my_canvas.create_text(510,150,text="Name : Saumya Shringirishi",font=("Castellar",20),fill="black")
                my_canvas.create_text(450,200,text="Class : XI COMM",font=("Castellar",20),fill="black")
                button1=Button(root1,text="Vote",font=("Castellar",20),height=1,width=10,command=vote1)
                button1_window=my_canvas.create_window(340,250,anchor="nw",window=button1)

                def vote2():

                    #adding votes to database and disabling other buttons with a sound
                    mycursor.execute("update deputyheadgirl set votes = votes + 1 where Name = 'Kirti Donge';")
                    mydb.commit()
                    button1['state']='disabled'
                    button2['state']='disabled'
                    button3['state']='disabled'
                    button4['state']='disabled'
                    playsound('sound.mp3')

                # adding image and details
                b=PhotoImage(file="kirti.png",master=my_canvas)
                my_canvas.create_image(1000,220,image=b)
                my_canvas.create_text(1290,150,text="Name : Kirti Donge",font=("Castellar",20),fill="black")
                my_canvas.create_text(1260,200,text="Class : XI COMM",font=("Castellar",20),fill="black")
                button2=Button(root1,text="Vote",font=("Castellar",20),height=1,width=10,command=vote2)
                button2_window=my_canvas.create_window(1140,250,anchor="nw",window=button2)

                def vote3():

                    #adding votes to database and disabling other buttons with a sound
                    mycursor.execute("update deputyheadgirl set votes = votes + 1 where Name = 'S. Tanushree Bhat';")
                    mydb.commit()
                    button1['state']='disabled'
                    button2['state']='disabled'
                    button3['state']='disabled'
                    button4['state']='disabled'
                    playsound('sound.mp3')

                # adding image and details
                c=PhotoImage(file="tanushree.png",master=my_canvas)
                my_canvas.create_image(150,510,image=c)
                my_canvas.create_text(500,450,text="Name : S. Tanushree Bhat",font=("Castellar",20),fill="black")
                my_canvas.create_text(420,500,text="Class : XI SCI",font=("Castellar",20),fill="black")
                button3=Button(root1,text="Vote",font=("Castellar",20),height=1,width=10,command=vote3)
                button3_window=my_canvas.create_window(340,550,anchor="nw",window=button3)

                def vote4():

                    #adding votes to database and disabling other buttons with a sound
                    mycursor.execute("update deputyheadgirl set votes = votes + 1 where Name = 'Vidhi Patel';")
                    mydb.commit()
                    button1['state']='disabled'
                    button2['state']='disabled'
                    button3['state']='disabled'
                    button4['state']='disabled'
                    playsound('sound.mp3')

                # adding image and details
                d=PhotoImage(file="vidhi.png",master=my_canvas)
                my_canvas.create_image(1000,510,image=d)
                my_canvas.create_text(1280,450,text="Name : Vidhi Patel",font=("Castellar",20),fill="black")
                my_canvas.create_text(1250,500,text="Class : XI SCI",font=("Castellar",20),fill="black")
                button4=Button(root1,text="Vote",font=("Castellar",20),height=1,width=10,command=vote4)
                button4_window=my_canvas.create_window(1140,550,anchor="nw",window=button4)

                def result():

                    #result screen
                    root = Tk()
                    root.title('Password')
                    root.geometry('650x350')

                    my_canvas=Canvas(root,width=650,height=350)
                    my_canvas.pack(fill="both",expand=True)

                    purple=PhotoImage(file="4.png",master=my_canvas)

                    my_canvas.create_image(0,0,image=purple,anchor="nw")

                    global entry3

                    my_canvas.create_text(110,40,text="Password",font=("Castellar",20),fill="black")

                    entry3=Entry(root,font=("Castellar",20),bd=10,show="*")
                    entry3.place(x=200,y=20)

                    def enter1():

                        #password checking
                        Password=entry3.get()

                        if Password=="7890":

                            root= Tk()
                            root.title('Deputy Head Girl')
                            root.geometry('1012x405')

                            bottomframe=Frame(root)
                            bottomframe.pack(side=BOTTOM)

                            def graph():
                                
                                #graph
                                mycursor.execute("select votes from deputyheadgirl;")
                                details=mycursor.fetchall()
                                x=[]
                                y=["Saumya","Kirti","Tanushree","Vidhi"]
                                for i in details:
                                    x.append(i[0])
                                pl.title("Deputy Head Girl")
                                pl.xlabel("Candidates")
                                pl.ylabel("No. of Votes")
                                pl.bar(y,x)
                                pl.show()

                                                            
                            graph=Button(bottomframe,text="Graph",command=graph,font=("Castellar",20),height=1,width=10)
                            graph.pack()

                            def back():

                                #back to select post
                                buttona['state']='active'
                                buttonb['state']='active'
                                buttonc['state']='active'
                                buttond['state']='active'
                                buttone['state']='active'
                                buttonf['state']='active'
                                buttong['state']='active'
                                enter()
                                
                            back=Button(bottomframe,text="Back",command=back)
                            back.pack()

                            #result table

                            mycursor.execute("Select * from deputyheadgirl order by votes desc;")
                            rows=mycursor.fetchall()

                            frn=Frame(root)
                            frn.pack(side=TOP)

                            tv=ttk.Treeview(root)
                            tv.pack()

                            tv["columns"]=("ID","Name","class","age","votes")
                            tv['show']='headings'

                            s=ttk.Style(root)
                            s.theme_use("clam")

                            s.configure(".",font=("Helvetica",15))
                            s.configure("Treeview.Heading",foreground='white',font=("Helvetica",15,"bold"))

                            tv.column("ID",anchor=tk.CENTER)
                            tv.column("Name",width=250,anchor=tk.CENTER)
                            tv.column("class",anchor=tk.CENTER)
                            tv.column("age",anchor=tk.CENTER)
                            tv.column("votes",anchor=tk.CENTER)

                            tv.heading("ID",text="ID",anchor=tk.CENTER)
                            tv.heading("Name",text="Name",anchor=tk.CENTER)
                            tv.heading("class",text="class",anchor=tk.CENTER)
                            tv.heading("age",text="age",anchor=tk.CENTER)
                            tv.heading("votes",text="votes",anchor=tk.CENTER)

                            for i in rows:
                                tv.insert('','end',values=i)

                        else:
                            messagebox.showinfo("","Incorrect username or password")

                    
                    button8=Button(root,text="enter",font=("Castellar",20),height=1,width=10,command=enter1)
                    button8_window=my_canvas.create_window(200,200,anchor="nw",window=button8)
            
                button5=Button(root1,text="Result",font=("Castellar",20),height=1,width=10,command=result)
                button5_window=my_canvas.create_window(1200,700,anchor="nw",window=button5)

                def enable():

                    #enables all voting buttons
                    button1['state']='active'
                    button2['state']='active'
                    button3['state']='active'
                    button4['state']='active'

                button11=Button(root1,text="Enable",font=("Castellar",20),height=1,width=10,command=enable)
                button11_window=my_canvas.create_window(600,700,anchor="nw",window=button11)

                def clear():

                    #clears all votes added for all candidates after checing password

                            root = Tk()
                            root.title('Password')
                            root.geometry('650x350')

                            my_canvas=Canvas(root,width=650,height=350)
                            my_canvas.pack(fill="both",expand=True)

                            k1=PhotoImage(file="4.png",master=my_canvas)

                            my_canvas.create_image(0,0,image=k1,anchor="nw")

                            global entry4

                            my_canvas.create_text(110,40,text="Password",font=("Castellar",20),fill="black")

                            entry4=Entry(root,font=("Castellar",20),bd=10,show="*")
                            entry4.place(x=200,y=20)

                            def enter2():
                                Password=entry4.get()

                                if Password=="7890":
                                    mycursor.execute("update deputyheadgirl set votes = 0;")
                                    mydb.commit()
                                    messagebox.showinfo("","votes cleared")

                            button10=Button(root,text="enter",font=("Castellar",20),height=1,width=10,command=enter2)
                            button10_window=my_canvas.create_window(200,200,anchor="nw",window=button10)

               
                button9=Button(root1,text="clear votes",font=("Castellar",20),height=1,width=10,command=clear)
                button9_window=my_canvas.create_window(50,700,anchor="nw",window=button9)

                root.mainloop()

            def deputyheadboy():

                #voting for deputyheadboy

                buttona['state']='disabled'
                buttonb['state']='disabled'
                buttonc['state']='disabled'
                buttond['state']='disabled'
                buttone['state']='disabled'
                buttonf['state']='disabled'
                buttong['state']='disabled'

                #creating table and adding data in database

                #mycursor.execute("Create table deputyheadboy (ID int(3),Name varchar(40),Class varchar(30),Age int(3),Votes int(8));")

                #mycursor.execute("insert into deputyheadboy values(1,'Rohan Yadav','XI SCI',15,0);")
                #mycursor.execute("insert into deputyheadboy values(2,'Chirag Kejriwal','XI SCI',16,0);")
                #mycursor.execute("insert into deputyheadboy values(3,'Vansh Chavda','XI SCI',15,0);")
                #mydb.commit()
                
                root1 = Tk()
                root1.title('Deputy Head Boy')
                root1.geometry('1856x1161')

                my_canvas=Canvas(root1,width=1856,height=1161)
                my_canvas.pack(fill="both",expand=True)

                bg=PhotoImage(file="4.png",master=my_canvas)

                my_canvas.create_image(0,0,image=bg,anchor="nw")

                my_canvas.create_text(700,50,text="Deputy Head Boy",font=("Castellar",80),fill="purple")

                def vote1():

                    #adding votes to database and disabling other buttons with a sound
                    mycursor.execute("update deputyheadboy set votes = votes + 1 where Name = 'Rohan Yadav';")
                    mydb.commit()
                    button1['state']='disabled'
                    button2['state']='disabled'
                    button3['state']='disabled'
                    playsound('sound.mp3')

                # adding image and details
                a=PhotoImage(file="rohan.png",master=my_canvas)
                my_canvas.create_image(150,220,image=a)
                my_canvas.create_text(480,150,text="Name : Rohan Yadav",font=("Castellar",20),fill="black")
                my_canvas.create_text(430,200,text="Class : XI SCI",font=("Castellar",20),fill="black")
                button1=Button(root1,text="Vote",font=("Castellar",20),height=1,width=10,command=vote1)
                button1_window=my_canvas.create_window(320,250,anchor="nw",window=button1)

                def vote2():

                    #adding votes to database and disabling other buttons with a sound
                    mycursor.execute("update deputyheadboy set votes = votes + 1 where Name = 'Chirag Kejriwal';")
                    mydb.commit()
                    button1['state']='disabled'
                    button2['state']='disabled'
                    button3['state']='disabled'
                    playsound('sound.mp3')

                # adding image and details
                b=PhotoImage(file="chirag.png",master=my_canvas)
                my_canvas.create_image(850,220,image=b)
                my_canvas.create_text(1200,150,text="Name : Chirag Kejriwal",font=("Castellar",20),fill="black")
                my_canvas.create_text(1150,200,text="Class : XI SCI",font=("Castellar",20),fill="black")
                button2=Button(root1,text="Vote",font=("Castellar",20),height=1,width=10,command=vote2)
                button2_window=my_canvas.create_window(1030,250,anchor="nw",window=button2)

                def vote3():

                    #adding votes to database and disabling other buttons with a sound
                    mycursor.execute("update deputyheadboy set votes = votes + 1 where Name = 'Vansh Chavda';")
                    mydb.commit()
                    button1['state']='disabled'
                    button2['state']='disabled'
                    button3['state']='disabled'
                    playsound('sound.mp3')

                # adding image and details
                c=PhotoImage(file="vansh.png",master=my_canvas)
                my_canvas.create_image(150,520,image=c)
                my_canvas.create_text(480,450,text="Name : Vansh Chavda",font=("Castellar",20),fill="black")
                my_canvas.create_text(430,500,text="Class : XI SCI",font=("Castellar",20),fill="black")
                button3=Button(root1,text="Vote",font=("Castellar",20),height=1,width=10,command=vote3)
                button3_window=my_canvas.create_window(320,550,anchor="nw",window=button3)
                

                def result():

                    #result screen
                    root = Tk()
                    root.title('Password')
                    root.geometry('650x350')

                    my_canvas=Canvas(root,width=650,height=350)
                    my_canvas.pack(fill="both",expand=True)

                    purple=PhotoImage(file="4.png",master=my_canvas)

                    my_canvas.create_image(0,0,image=purple,anchor="nw")

                    global entry3

                    my_canvas.create_text(110,40,text="Password",font=("Castellar",20),fill="black")

                    entry3=Entry(root,font=("Castellar",20),bd=10,show="*")
                    entry3.place(x=200,y=20)

                    def enter1():

                        #password checking
                        Password=entry3.get()

                        if Password=="7890":

                            root= Tk()
                            root.title('Deputy Head Boy')
                            root.geometry('1012x405')

                            bottomframe=Frame(root)
                            bottomframe.pack(side=BOTTOM)

                            def graph():
                                
                                #graph
                                mycursor.execute("select votes from deputyheadboy;")
                                details=mycursor.fetchall()
                                x=[]
                                y=["Rohan","Chirag","Vansh"]
                                for i in details:
                                    x.append(i[0])
                                pl.title("Deputy Head Boy")
                                pl.xlabel("Candidates")
                                pl.ylabel("No. of Votes")
                                pl.bar(y,x)
                                pl.show()

                                                            
                            graph=Button(bottomframe,text="Graph",command=graph,font=("Castellar",20),height=1,width=10)
                            graph.pack()

                            def back():

                                #back to select post
                                buttona['state']='active'
                                buttonb['state']='active'
                                buttonc['state']='active'
                                buttond['state']='active'
                                buttone['state']='active'
                                buttonf['state']='active'
                                buttong['state']='active'
                                enter()
                                
                            back=Button(bottomframe,text="Back",command=back)
                            back.pack()

                            #resullt table

                            mycursor.execute("Select * from deputyheadboy order by votes desc;")
                            rows=mycursor.fetchall()

                            frn=Frame(root)
                            frn.pack(side=TOP)

                            tv=ttk.Treeview(root)
                            tv.pack()

                            tv["columns"]=("ID","Name","class","age","votes")
                            tv['show']='headings'

                            s=ttk.Style(root)
                            s.theme_use("clam")

                            s.configure(".",font=("Helvetica",15))
                            s.configure("Treeview.Heading",foreground='white',font=("Helvetica",15,"bold"))

                            tv.column("ID",anchor=tk.CENTER)
                            tv.column("Name",width=250,anchor=tk.CENTER)
                            tv.column("class",anchor=tk.CENTER)
                            tv.column("age",anchor=tk.CENTER)
                            tv.column("votes",anchor=tk.CENTER)

                            tv.heading("ID",text="ID",anchor=tk.CENTER)
                            tv.heading("Name",text="Name",anchor=tk.CENTER)
                            tv.heading("class",text="class",anchor=tk.CENTER)
                            tv.heading("age",text="age",anchor=tk.CENTER)
                            tv.heading("votes",text="votes",anchor=tk.CENTER)

                            for i in rows:
                                tv.insert('','end',values=i)

                        else:
                            messagebox.showinfo("","Incorrect username or password")

                    
                    button8=Button(root,text="enter",font=("Castellar",20),height=1,width=10,command=enter1)
                    button8_window=my_canvas.create_window(200,200,anchor="nw",window=button8)
            
                button5=Button(root1,text="Result",font=("Castellar",20),height=1,width=10,command=result)
                button5_window=my_canvas.create_window(1200,700,anchor="nw",window=button5)

                def enable():

                    #enables all voting buttons
                    button1['state']='active'
                    button2['state']='active'
                    button3['state']='active'

                button11=Button(root1,text="Enable",font=("Castellar",20),height=1,width=10,command=enable)
                button11_window=my_canvas.create_window(600,700,anchor="nw",window=button11)

                def clear():

                    #clears all votes added for all candidates after checking password
                    
                            root = Tk()
                            root.title('Password')
                            root.geometry('650x350')

                            my_canvas=Canvas(root,width=650,height=350)
                            my_canvas.pack(fill="both",expand=True)

                            k1=PhotoImage(file="4.png",master=my_canvas)

                            my_canvas.create_image(0,0,image=k1,anchor="nw")

                            global entry4

                            my_canvas.create_text(110,40,text="Password",font=("Castellar",20),fill="black")

                            entry4=Entry(root,font=("Castellar",20),bd=10,show="*")
                            entry4.place(x=200,y=20)

                            def enter2():
                                Password=entry4.get()

                                if Password=="7890":
                                    mycursor.execute("update deputyheadboy set votes = 0;")
                                    mydb.commit()
                                    messagebox.showinfo("","votes cleared")

                            button10=Button(root,text="enter",font=("Castellar",20),height=1,width=10,command=enter2)
                            button10_window=my_canvas.create_window(200,200,anchor="nw",window=button10)

               
                button9=Button(root1,text="clear votes",font=("Castellar",20),height=1,width=10,command=clear)
                button9_window=my_canvas.create_window(10,700,anchor="nw",window=button9)

                root.mainloop()

            def sportscaptain():

                #voting for sportscaptain

                buttona['state']='disabled'
                buttonb['state']='disabled'
                buttonc['state']='disabled'
                buttond['state']='disabled'
                buttone['state']='disabled'
                buttonf['state']='disabled'
                buttong['state']='disabled'

                #creating table and adding data in database

                #mycursor.execute("Create table sportscaptain (ID int(3),Name varchar(40),Class varchar(30),Age int(3),Votes int(8));")

                #mycursor.execute("insert into sportscaptain values(1,'Sweta Singh','XII COMM',17,0);")
                #mycursor.execute("insert into sportscaptain values(2,'Ujwal Prashar','XII SCI',16,0);")
                #mycursor.execute("insert into sportscaptain values(3,'Kashish Sharma','XII COMM',16,0);")
                #mydb.commit()
                
                root1 = Tk()
                root1.title('Sports Captain')
                root1.geometry('1856x1161')

                my_canvas=Canvas(root1,width=1856,height=1161)
                my_canvas.pack(fill="both",expand=True)

                bg=PhotoImage(file="4.png",master=my_canvas)

                my_canvas.create_image(0,0,image=bg,anchor="nw")

                my_canvas.create_text(700,50,text="Sports Captain",font=("Castellar",80),fill="purple")

                def vote1():
                    
                    #adding votes to database and disabling other buttons with a sound
                    mycursor.execute("update sportscaptain set votes = votes + 1 where Name = 'Sweta Singh';")
                    mydb.commit()
                    button1['state']='disabled'
                    button2['state']='disabled'
                    button3['state']='disabled'
                    playsound('sound.mp3')

                # adding image and details
                a=PhotoImage(file="shweta.png",master=my_canvas)
                my_canvas.create_image(150,220,image=a)
                my_canvas.create_text(500,150,text="Name : Shweta Singh",font=("Castellar",20),fill="black")
                my_canvas.create_text(450,200,text="Class : XII COMM",font=("Castellar",20),fill="black")
                button1=Button(root1,text="Vote",font=("Castellar",20),height=1,width=10,command=vote1)
                button1_window=my_canvas.create_window(320,250,anchor="nw",window=button1)

                def vote2():

                    #adding votes to database and disabling other buttons with a sound
                    mycursor.execute("update sportscaptain set votes = votes + 1 where Name = 'Ujwal Prashar';")
                    mydb.commit()
                    button1['state']='disabled'
                    button2['state']='disabled'
                    button3['state']='disabled'
                    playsound('sound.mp3')

                # adding image and details
                b=PhotoImage(file="ujwal.png",master=my_canvas)
                my_canvas.create_image(850,220,image=b)
                my_canvas.create_text(1200,150,text="Name : Ujwal Prashar",font=("Castellar",20),fill="black")
                my_canvas.create_text(1150,200,text="Class : XII SCI",font=("Castellar",20),fill="black")
                button2=Button(root1,text="Vote",font=("Castellar",20),height=1,width=10,command=vote2)
                button2_window=my_canvas.create_window(1050,250,anchor="nw",window=button2)

                def vote3():

                    #adding votes to database and disabling other buttons with a sound
                    mycursor.execute("update sportscaptain set votes = votes + 1 where Name = 'Kashish Sharma';")
                    mydb.commit()
                    button1['state']='disabled'
                    button2['state']='disabled'
                    button3['state']='disabled'
                    playsound('sound.mp3')

                # adding image and details
                c=PhotoImage(file="kashish.png",master=my_canvas)
                my_canvas.create_image(150,510,image=c)
                my_canvas.create_text(500,450,text="Name : Kashish Sharma",font=("Castellar",20),fill="black")
                my_canvas.create_text(450,500,text="Class : XII COMM",font=("Castellar",20),fill="black")
                button3=Button(root1,text="Vote",font=("Castellar",20),height=1,width=10,command=vote3)
                button3_window=my_canvas.create_window(320,550,anchor="nw",window=button3)


                def result():

                    #result screen
                    root = Tk()
                    root.title('Password')
                    root.geometry('650x350')

                    my_canvas=Canvas(root,width=650,height=350)
                    my_canvas.pack(fill="both",expand=True)

                    purple=PhotoImage(file="4.png",master=my_canvas)

                    my_canvas.create_image(0,0,image=purple,anchor="nw")

                    global entry3

                    my_canvas.create_text(110,40,text="Password",font=("Castellar",20),fill="black")

                    entry3=Entry(root,font=("Castellar",20),bd=10,show="*")
                    entry3.place(x=200,y=20)

                    def enter1():

                        #passowrd checking
                        Password=entry3.get()

                        if Password=="7890":

                            root= Tk()
                            root.title('Sports Captain')
                            root.geometry('1012x405')

                            bottomframe=Frame(root)
                            bottomframe.pack(side=BOTTOM)

                            def graph():
                                
                                #graph
                                mycursor.execute("select votes from sportscaptain;")
                                details=mycursor.fetchall()
                                x=[]
                                y=["Sweta","Ujwal","Kashish"]
                                for i in details:
                                    x.append(i[0])
                                pl.title("Sports Captain")
                                pl.xlabel("Candidates")
                                pl.ylabel("No. of Votes")
                                pl.bar(y,x)
                                pl.show()

                                                            
                            graph=Button(bottomframe,text="Graph",command=graph,font=("Castellar",20),height=1,width=10)
                            graph.pack()

                            def back():

                                #back to select post
                                buttona['state']='active'
                                buttonb['state']='active'
                                buttonc['state']='active'
                                buttond['state']='active'
                                buttone['state']='active'
                                buttonf['state']='active'
                                buttong['state']='active'
                                enter()
                                
                            back=Button(bottomframe,text="Back",command=back)
                            back.pack()

                            #result table

                            mycursor.execute("Select * from sportscaptain order by votes desc;")
                            rows=mycursor.fetchall()

                            frn=Frame(root)
                            frn.pack(side=TOP)

                            tv=ttk.Treeview(root)
                            tv.pack()

                            tv["columns"]=("ID","Name","class","age","votes")
                            tv['show']='headings'

                            s=ttk.Style(root)
                            s.theme_use("clam")

                            s.configure(".",font=("Helvetica",15))
                            s.configure("Treeview.Heading",foreground='white',font=("Helvetica",15,"bold"))

                            tv.column("ID",anchor=tk.CENTER)
                            tv.column("Name",width=250,anchor=tk.CENTER)
                            tv.column("class",anchor=tk.CENTER)
                            tv.column("age",anchor=tk.CENTER)
                            tv.column("votes",anchor=tk.CENTER)

                            tv.heading("ID",text="ID",anchor=tk.CENTER)
                            tv.heading("Name",text="Name",anchor=tk.CENTER)
                            tv.heading("class",text="class",anchor=tk.CENTER)
                            tv.heading("age",text="age",anchor=tk.CENTER)
                            tv.heading("votes",text="votes",anchor=tk.CENTER)

                            for i in rows:
                                tv.insert('','end',values=i)

                        else:
                            messagebox.showinfo("","Incorrect username or password")

                    
                    button8=Button(root,text="enter",font=("Castellar",20),height=1,width=10,command=enter1)
                    button8_window=my_canvas.create_window(200,200,anchor="nw",window=button8)
            
                button5=Button(root1,text="Result",font=("Castellar",20),height=1,width=10,command=result)
                button5_window=my_canvas.create_window(1200,700,anchor="nw",window=button5)

                def enable():

                    #enables all voting button
                    button1['state']='active'
                    button2['state']='active'
                    button3['state']='active'

                button11=Button(root1,text="Enable",font=("Castellar",20),height=1,width=10,command=enable)
                button11_window=my_canvas.create_window(550,700,anchor="nw",window=button11)

                def clear():

                    #clears all votes for all candidates after checking password

                            root = Tk()
                            root.title('Password')
                            root.geometry('650x350')

                            my_canvas=Canvas(root,width=650,height=350)
                            my_canvas.pack(fill="both",expand=True)

                            k1=PhotoImage(file="4.png",master=my_canvas)

                            my_canvas.create_image(0,0,image=k1,anchor="nw")

                            global entry4

                            my_canvas.create_text(110,40,text="Password",font=("Castellar",20),fill="black")

                            entry4=Entry(root,font=("Castellar",20),bd=10,show="*")
                            entry4.place(x=200,y=20)

                            def enter2():
                                Password=entry4.get()

                                if Password=="7890":
                                    mycursor.execute("update sportscaptain set votes = 0;")
                                    mydb.commit()
                                    messagebox.showinfo("","votes cleared")

                            button10=Button(root,text="enter",font=("Castellar",20),height=1,width=10,command=enter2)
                            button10_window=my_canvas.create_window(200,200,anchor="nw",window=button10)

               
                button9=Button(root1,text="clear votes",font=("Castellar",20),height=1,width=10,command=clear)
                button9_window=my_canvas.create_window(50,700,anchor="nw",window=button9)

                root.mainloop()

            def cleanlinessincharge():
                
                #voting for cleanlinessincharge
                buttona['state']='disabled'
                buttonb['state']='disabled'
                buttonc['state']='disabled'
                buttond['state']='disabled'
                buttone['state']='disabled'
                buttonf['state']='disabled'
                buttong['state']='disabled'

                #creating table and adding data in database

                #mycursor.execute("Create table cleanlinessincharge(ID int(3),Name varchar(40),Class varchar(30),Age int(3),Votes int(8));")

                #mycursor.execute("insert into cleanlinessincharge values(1,'Nandani Soni','XI COMM',15,0);")
                #mycursor.execute("insert into cleanlinessincharge values(2,'Richa Patel','XI COMM',15,0);")
                #mycursor.execute("insert into cleanlinessincharge values(3,'Praakshit Biswas','XII COMM',16,0);")
                #mycursor.execute("insert into cleanlinessincharge values(4,'Param Savla','XII COMM',16,0);")
                #mydb.commit()

                root1 = Tk()
                root1.title('Cleanliness Incharge')
                root1.geometry('1856x1161')

                my_canvas=Canvas(root1,width=1856,height=1161)
                my_canvas.pack(fill="both",expand=True)

                bg=PhotoImage(file="4.png",master=my_canvas)

                my_canvas.create_image(0,0,image=bg,anchor="nw")

                my_canvas.create_text(700,50,text="Cleanliness Incharge",font=("Castellar",80),fill="purple")

                def vote1():

                    #adding votes to database and disabling other buttons with a sound
                    mycursor.execute("update cleanlinessincharge set votes = votes + 1 where Name = 'Nandani Soni';")
                    mydb.commit()
                    button1['state']='disabled'
                    button2['state']='disabled'
                    button3['state']='disabled'
                    button4['state']='disabled'
                    playsound('sound.mp3')

                # adding image and details
                a=PhotoImage(file="nandani.png",master=my_canvas)
                my_canvas.create_image(150,220,image=a)
                my_canvas.create_text(450,150,text="Name : Nandani Soni",font=("Castellar",20),fill="black")
                my_canvas.create_text(430,200,text="Class : XI COMM",font=("Castellar",20),fill="black")
                button1=Button(root1,text="Vote",font=("Castellar",20),height=1,width=10,command=vote1)
                button1_window=my_canvas.create_window(330,250,anchor="nw",window=button1)

                def vote2():

                    #adding votes to database and disabling other buttons with a sound
                    mycursor.execute("update cleanlinessincharge set votes = votes + 1 where Name = 'Richa Patel';")
                    mydb.commit()
                    button1['state']='disabled'
                    button2['state']='disabled'
                    button3['state']='disabled'
                    button4['state']='disabled'
                    playsound('sound.mp3')

                # adding image and details
                b=PhotoImage(file="richa.png",master=my_canvas)
                my_canvas.create_image(900,220,image=b)
                my_canvas.create_text(1200,150,text="Name : Richa Patel",font=("Castellar",20),fill="black")
                my_canvas.create_text(1190,200,text="Class : XI COMM",font=("Castellar",20),fill="black")
                button2=Button(root1,text="Vote",font=("Castellar",20),height=1,width=10,command=vote2)
                button2_window=my_canvas.create_window(1100,250,anchor="nw",window=button2)

                def vote3():

                    #adding votes to database and disabling other buttons with a sound
                    mycursor.execute("update cleanlinessincharge set votes = votes + 1 where Name = 'Praakshit Biswas';")
                    mydb.commit()
                    button1['state']='disabled'
                    button2['state']='disabled'
                    button3['state']='disabled'
                    button4['state']='disabled'
                    playsound('sound.mp3')

                # adding image and details
                c=PhotoImage(file="praakshit.png",master=my_canvas)
                my_canvas.create_image(150,520,image=c)
                my_canvas.create_text(500,450,text="Name : Praakshit Biswas",font=("Castellar",20),fill="black")
                my_canvas.create_text(450,500,text="Class : XII COMM",font=("Castellar",20),fill="black")
                button3=Button(root1,text="Vote",font=("Castellar",20),height=1,width=10,command=vote3)
                button3_window=my_canvas.create_window(330,550,anchor="nw",window=button3)

                def vote4():

                    #adding votes to database and disabling other buttons with a sound
                    mycursor.execute("update cleanlinessincharge set votes = votes + 1 where Name = 'Param Savla';")
                    mydb.commit()
                    button1['state']='disabled'
                    button2['state']='disabled'
                    button3['state']='disabled'
                    button4['state']='disabled'
                    playsound('sound.mp3')

                # adding image and details
                d=PhotoImage(file="param.png",master=my_canvas)
                my_canvas.create_image(900,520,image=d)
                my_canvas.create_text(1200,450,text="Name : Param Savla",font=("Castellar",20),fill="black")
                my_canvas.create_text(1190,500,text="Class : XII COMM",font=("Castellar",20),fill="black")
                button4=Button(root1,text="Vote",font=("Castellar",20),height=1,width=10,command=vote4)
                button4_window=my_canvas.create_window(1100,550,anchor="nw",window=button4)

                def result():

                    #result screen
                    root = Tk()
                    root.title('Password')
                    root.geometry('650x350')

                    my_canvas=Canvas(root,width=650,height=350)
                    my_canvas.pack(fill="both",expand=True)

                    purple=PhotoImage(file="4.png",master=my_canvas)

                    my_canvas.create_image(0,0,image=purple,anchor="nw")

                    global entry3

                    my_canvas.create_text(110,40,text="Password",font=("Castellar",20),fill="black")

                    entry3=Entry(root,font=("Castellar",20),bd=10,show="*")
                    entry3.place(x=200,y=20)

                    def enter1():

                        #password checking
                        Password=entry3.get()

                        if Password=="7890":

                            root= Tk()
                            root.title('Cleanliness Incharge')
                            root.geometry('1012x405')

                            bottomframe=Frame(root)
                            bottomframe.pack(side=BOTTOM)

                            def graph():

                                #graph

                                mycursor.execute("select votes from cleanlinessincharge;")
                                details=mycursor.fetchall()
                                x=[]
                                y=["Nandani","Richa","Praakshit","Param"]
                                for i in details:
                                    x.append(i[0])
                                pl.title("Cleanliness Incharge")
                                pl.xlabel("Candidates")
                                pl.ylabel("No. of Votes")
                                pl.bar(y,x)
                                pl.show()

                                                            
                            graph=Button(bottomframe,text="Graph",command=graph,font=("Castellar",20),height=1,width=10)
                            graph.pack()

                            def back():

                                #back to select post
                                buttona['state']='active'
                                buttonb['state']='active'
                                buttonc['state']='active'
                                buttond['state']='active'
                                buttone['state']='active'
                                buttonf['state']='active'
                                buttong['state']='active'
                                enter()
                                
                            back=Button(bottomframe,text="Back",command=back)
                            back.pack()

                            #result table

                            mycursor.execute("Select * from cleanlinessincharge order by votes desc;")
                            rows=mycursor.fetchall()

                            frn=Frame(root)
                            frn.pack(side=TOP)

                            tv=ttk.Treeview(root)
                            tv.pack()

                            tv["columns"]=("ID","Name","class","age","votes")
                            tv['show']='headings'

                            s=ttk.Style(root)
                            s.theme_use("clam")

                            s.configure(".",font=("Helvetica",15))
                            s.configure("Treeview.Heading",foreground='white',font=("Helvetica",15,"bold"))

                            tv.column("ID",anchor=tk.CENTER)
                            tv.column("Name",width=250,anchor=tk.CENTER)
                            tv.column("class",anchor=tk.CENTER)
                            tv.column("age",anchor=tk.CENTER)
                            tv.column("votes",anchor=tk.CENTER)

                            tv.heading("ID",text="ID",anchor=tk.CENTER)
                            tv.heading("Name",text="Name",anchor=tk.CENTER)
                            tv.heading("class",text="class",anchor=tk.CENTER)
                            tv.heading("age",text="age",anchor=tk.CENTER)
                            tv.heading("votes",text="votes",anchor=tk.CENTER)

                            for i in rows:
                                tv.insert('','end',values=i)

                        else:
                            messagebox.showinfo("","Incorrect username or password")

                    
                    button8=Button(root,text="enter",font=("Castellar",20),height=1,width=10,command=enter1)
                    button8_window=my_canvas.create_window(200,200,anchor="nw",window=button8)
            
                button5=Button(root1,text="Result",font=("Castellar",20),height=1,width=10,command=result)
                button5_window=my_canvas.create_window(1200,700,anchor="nw",window=button5)

                def enable():

                    #enables all voting buttons
                    button1['state']='active'
                    button2['state']='active'
                    button3['state']='active'
                    button4['state']='active'

                button11=Button(root1,text="Enable",font=("Castellar",20),height=1,width=10,command=enable)
                button11_window=my_canvas.create_window(600,700,anchor="nw",window=button11)

                def clear():

                    #clears all votes added for all candidates after checking password

                            root = Tk()
                            root.title('Password')
                            root.geometry('650x350')

                            my_canvas=Canvas(root,width=650,height=350)
                            my_canvas.pack(fill="both",expand=True)

                            k1=PhotoImage(file="4.png",master=my_canvas)

                            my_canvas.create_image(0,0,image=k1,anchor="nw")

                            global entry4

                            my_canvas.create_text(110,40,text="Password",font=("Castellar",20),fill="black")

                            entry4=Entry(root,font=("Castellar",20),bd=10,show="*")
                            entry4.place(x=200,y=20)

                            def enter2():
                                Password=entry4.get()

                                if Password=="7890":
                                    mycursor.execute("update cleanlinessincharge set votes = 0;")
                                    mydb.commit()
                                    messagebox.showinfo("","votes cleared")

                            button10=Button(root,text="enter",font=("Castellar",20),height=1,width=10,command=enter2)
                            button10_window=my_canvas.create_window(200,200,anchor="nw",window=button10)

               
                button9=Button(root1,text="clear votes",font=("Castellar",20),height=1,width=10,command=clear)
                button9_window=my_canvas.create_window(50,700,anchor="nw",window=button9)

                root.mainloop()

            def disciplineincharge():
                
                #voting for disciplineincharge
                buttona['state']='disabled'
                buttonb['state']='disabled'
                buttonc['state']='disabled'
                buttond['state']='disabled'
                buttone['state']='disabled'
                buttonf['state']='disabled'
                buttong['state']='disabled'

                #creating table and adding data in database

                #mycursor.execute("Create table disciplineincharge(ID int(3),Name varchar(40),Class varchar(30),Age int(3),Votes int(8));")

                #mycursor.execute("insert into disciplineincharge values(1,'Aditya Vinayak Singh','XI SCI',15,0);")
                #mycursor.execute("insert into disciplineincharge values(2,'Lisha Tiwari','XI COMM',17,0);")
                #mycursor.execute("insert into disciplineincharge values(3,'Sneha Mishra','XII COMM',17,0);")
                #mycursor.execute("insert into disciplineincharge values(4,'Prachay Thaker','XII COMM',16,0);")
                #mydb.commit()
                
                root1 = Tk()
                root1.title('Discipline Incharge')
                root1.geometry('1856x1161')

                my_canvas=Canvas(root1,width=1856,height=1161)
                my_canvas.pack(fill="both",expand=True)

                bg=PhotoImage(file="4.png",master=my_canvas)

                my_canvas.create_image(0,0,image=bg,anchor="nw")

                my_canvas.create_text(700,50,text="Discipline Incharge",font=("Castellar",80),fill="purple")

                def vote1():

                    #adding votes to database and disabling other buttons with a sound
                    mycursor.execute("update disciplineincharge set votes = votes + 1 where Name = 'Aditya Vinayak Singh';")
                    mydb.commit()
                    button1['state']='disabled'
                    button2['state']='disabled'
                    button3['state']='disabled'
                    button4['state']='disabled'
                    playsound('sound.mp3')

                # adding image and details
                a=PhotoImage(file="aditya.png",master=my_canvas)
                my_canvas.create_image(150,220,image=a)
                my_canvas.create_text(520,150,text="Name : Aditya Vinayak Singh",font=("Castellar",20),fill="black")
                my_canvas.create_text(410,200,text="Class : XI SCI",font=("Castellar",20),fill="black")
                button1=Button(root1,text="Vote",font=("Castellar",20),height=1,width=10,command=vote1)
                button1_window=my_canvas.create_window(330,250,anchor="nw",window=button1)

                def vote2():

                    #adding votes to database and disabling other buttons with a sound
                    mycursor.execute("update disciplineincharge set votes = votes + 1 where Name = 'Lisha Tiwari';")
                    mydb.commit()
                    button1['state']='disabled'
                    button2['state']='disabled'
                    button3['state']='disabled'
                    button4['state']='disabled'
                    playsound('sound.mp3')

                # adding image and details
                b=PhotoImage(file="lisha.png",master=my_canvas)
                my_canvas.create_image(950,220,image=b)
                my_canvas.create_text(1250,150,text="Name : Lisha Tiwari",font=("Castellar",20),fill="black")
                my_canvas.create_text(1200,200,text="Class : XI COMM",font=("Castellar",20),fill="black")
                button2=Button(root1,text="Vote",font=("Castellar",20),height=1,width=10,command=vote2)
                button2_window=my_canvas.create_window(1100,250,anchor="nw",window=button2)

                def vote3():

                    #adding votes to database and disabling other buttons with a sound
                    mycursor.execute("update disciplineincharge set votes = votes + 1 where Name = 'Sneha Mishra';")
                    mydb.commit()
                    button1['state']='disabled'
                    button2['state']='disabled'
                    button3['state']='disabled'
                    button4['state']='disabled'
                    playsound('sound.mp3')

                # adding image and details
                c=PhotoImage(file="sneha.png",master=my_canvas)
                my_canvas.create_image(150,520,image=c)
                my_canvas.create_text(480,450,text="Name : Sneha Mishra",font=("Castellar",20),fill="black")
                my_canvas.create_text(410,500,text="Class : XII COMM",font=("Castellar",20),fill="black")
                button3=Button(root1,text="Vote",font=("Castellar",20),height=1,width=10,command=vote3)
                button3_window=my_canvas.create_window(330,550,anchor="nw",window=button3)

                def vote4():

                    #adding votes to database and disabling other buttons with a sound
                    mycursor.execute("update disciplineincharge set votes = votes + 1 where Name = 'Prachay Thaker';")
                    mydb.commit()
                    button1['state']='disabled'
                    button2['state']='disabled'
                    button3['state']='disabled'
                    button4['state']='disabled'
                    playsound('sound.mp3')

                # adding image and details
                d=PhotoImage(file="prachay.png",master=my_canvas)
                my_canvas.create_image(950,520,image=d)
                my_canvas.create_text(1270,450,text="Name : Prachay Thaker",font=("Castellar",20),fill="black")
                my_canvas.create_text(1210,500,text="Class : XII COMM",font=("Castellar",20),fill="black")
                button4=Button(root1,text="Vote",font=("Castellar",20),height=1,width=10,command=vote4)
                button4_window=my_canvas.create_window(1100,550,anchor="nw",window=button4)

                def result():

                    #result screen
                    root = Tk()
                    root.title('Password')
                    root.geometry('650x350')

                    my_canvas=Canvas(root,width=650,height=350)
                    my_canvas.pack(fill="both",expand=True)

                    purple=PhotoImage(file="4.png",master=my_canvas)

                    my_canvas.create_image(0,0,image=purple,anchor="nw")

                    global entry3

                    my_canvas.create_text(110,40,text="Password",font=("Castellar",20),fill="black")

                    entry3=Entry(root,font=("Castellar",20),bd=10,show="*")
                    entry3.place(x=200,y=20)

                    def enter1():

                        #password checking
                        Password=entry3.get()

                        if Password=="7890":

                            root= Tk()
                            root.title('Discipline Incharge')
                            root.geometry('1012x405')

                            bottomframe=Frame(root)
                            bottomframe.pack(side=BOTTOM)

                            def graph():
                                
                                #graph
                                
                                mycursor.execute("select votes from disciplineincharge;")
                                details=mycursor.fetchall()
                                x=[]
                                y=["Aditya","Lisha","Sneha","Prachay"]
                                for i in details:
                                    x.append(i[0])
                                pl.title("Discipline Incharge")
                                pl.xlabel("Candidates")
                                pl.ylabel("No. of Votes")
                                pl.bar(y,x)
                                pl.show()

                                                            
                            graph=Button(bottomframe,text="Graph",command=graph)
                            graph.pack()

                            def back():

                                #back to select post
                                buttona['state']='active'
                                buttonb['state']='active'
                                buttonc['state']='active'
                                buttond['state']='active'
                                buttone['state']='active'
                                buttonf['state']='active'
                                buttong['state']='active'
                                enter()
                                
                            back=Button(bottomframe,text="Back",command=back)
                            back.pack()

                            #result table

                            mycursor.execute("Select * from disciplineincharge order by votes desc;")
                            rows=mycursor.fetchall()

                            frn=Frame(root)
                            frn.pack(side=TOP)

                            tv=ttk.Treeview(root)
                            tv.pack()

                            tv["columns"]=("ID","Name","class","age","votes")
                            tv['show']='headings'

                            s=ttk.Style(root)
                            s.theme_use("clam")

                            s.configure(".",font=("Helvetica",15))
                            s.configure("Treeview.Heading",foreground='white',font=("Helvetica",15,"bold"))

                            tv.column("ID",anchor=tk.CENTER)
                            tv.column("Name",width=250,anchor=tk.CENTER)
                            tv.column("class",anchor=tk.CENTER)
                            tv.column("age",anchor=tk.CENTER)
                            tv.column("votes",anchor=tk.CENTER)

                            tv.heading("ID",text="ID",anchor=tk.CENTER)
                            tv.heading("Name",text="Name",anchor=tk.CENTER)
                            tv.heading("class",text="class",anchor=tk.CENTER)
                            tv.heading("age",text="age",anchor=tk.CENTER)
                            tv.heading("votes",text="votes",anchor=tk.CENTER)

                            for i in rows:
                                tv.insert('','end',values=i)

                        else:
                            messagebox.showinfo("","Incorrect username or password")

                    
                    button8=Button(root,text="enter",font=("Castellar",20),height=1,width=10,command=enter1)
                    button8_window=my_canvas.create_window(200,200,anchor="nw",window=button8)
            
                button5=Button(root1,text="Result",font=("Castellar",20),height=1,width=10,command=result)
                button5_window=my_canvas.create_window(1200,700,anchor="nw",window=button5)

                def enable():

                    #enables all voting buttons
                    button1['state']='active'
                    button2['state']='active'
                    button3['state']='active'
                    button4['state']='active'

                button11=Button(root1,text="Enable",font=("Castellar",20),height=1,width=10,command=enable)
                button11_window=my_canvas.create_window(600,700,anchor="nw",window=button11)

                def clear():

                    #clears all votes added for all candidates after checking password

                            root = Tk()
                            root.title('Password')
                            root.geometry('650x350')

                            my_canvas=Canvas(root,width=650,height=350)
                            my_canvas.pack(fill="both",expand=True)

                            k1=PhotoImage(file="4.png",master=my_canvas)

                            my_canvas.create_image(0,0,image=k1,anchor="nw")

                            global entry4

                            my_canvas.create_text(110,40,text="Password",font=("Castellar",20),fill="black")

                            entry4=Entry(root,font=("Castellar",20),bd=10,show="*")
                            entry4.place(x=200,y=20)

                            def enter2():
                                Password=entry4.get()

                                if Password=="7890":
                                    mycursor.execute("update disciplineincharge set votes = 0;")
                                    mydb.commit()
                                    messagebox.showinfo("","votes cleared")

                            button10=Button(root,text="enter",font=("Castellar",20),height=1,width=10,command=enter2)
                            button10_window=my_canvas.create_window(200,200,anchor="nw",window=button10)

               
                button9=Button(root1,text="clear votes",font=("Castellar",20),height=1,width=10,command=clear)
                button9_window=my_canvas.create_window(50,700,anchor="nw",window=button9)

                root.mainloop()

            #select post screen 

            buttona=Button(root,text="Head Girl",font=("Castellar",20),height=1,width=30,command=headgirl)
            buttona.pack()
            buttona.place(x=450,y=150)

            buttonb=Button(root,text="Head Boy",font=("Castellar",20),height=1,width=30,command=headboy)
            buttonb.pack()
            buttonb.place(x=450,y=240)

            buttonc=Button(root,text="Deputy Head Girl",font=("Castellar",20),height=1,width=30,command=deputyheadgirl)
            buttonc.pack()
            buttonc.place(x=450,y=330)
 
            buttond=Button(root,text="Deputy Head Boy",font=("Castellar",20),height=1,width=30,command=deputyheadboy)
            buttond.pack()
            buttond.place(x=450,y=420)

            buttone=Button(root,text="Sports Captain",font=("Castellar",20),height=1,width=30,command=sportscaptain)
            buttone.pack()
            buttone.place(x=450,y=510)

            buttonf=Button(root,text="Cleanliness Incharge",font=("Castellar",20),height=1,width=30,command=cleanlinessincharge)
            buttonf.pack()
            buttonf.place(x=450,y=600)

            buttong=Button(root,text="Discipline Incharge",font=("Castellar",20),height=1,width=30,command=disciplineincharge)
            buttong.pack()
            buttong.place(x=450,y=690)


            root.mainloop()

        else:
            messagebox.showinfo("","Incorrect username or password")

            
    button6=Button(root,text="Enter",command=enter,font=("Castellar",20),height=1,width=10)
    button6_window=my_canvas.create_window(150,180,anchor="nw",window=button6)

    root.mainloop()

#welcome screen

bg=PhotoImage(file="4.png")

my_canvas=Canvas(root,width=800,height=500)
my_canvas.pack(fill="both",expand=True)

my_canvas.create_image(0,0,image=bg,anchor="nw")

my_canvas.create_text(750,150,text="welcome",font=("Castellar",100))
my_canvas.create_text(700,300,text="to",font=("Castellar",70))
my_canvas.create_text(750,450,text="welspun election",font=("Castellar",100))

button1=Button(root,text="Login",font=("Castellar",30),command=login,height=1,width=10)
button1_window=my_canvas.create_window(550,600,anchor="nw",window=button1)

root.mainloop()
