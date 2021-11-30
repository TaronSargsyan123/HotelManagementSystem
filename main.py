from control import *
from inputClass import *
import tkinter
from tkinter import ttk
from tkinter import *
import tkinter as tk
from datetime import datetime


hostname = 'localhost'
username = 'root'
password = ''
database = 'hoteldb'

myConnection = mysql.connector.connect(host=hostname, user=username, password=password, db=database)

#input1 = Input()
#
#
#
#controlPanel = Control()
#controlPanel.controlInput(input1,input1.userInput("enter 1-search, 2-show table, 3-input --> "))




LIST = []

def selectByName(table):
    sql_select_Query = "select * from %s" % (table)
    cursor = myConnection.cursor(dictionary=True)
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()

    # print("#" * 100)
    for row in records:
        id = row["id"]
        name = row["name"]
        # LIST.append((str(id),name))

        LIST.append(name)

def viewSelection(table):
    cursor = myConnection.cursor(dictionary=True)
    selection = list.curselection()
    if [list.get(i) for i in selection] != []:
        print([list.get(i) for i in selection])
        viewWindow = tk.Toplevel(window)
        viewWindow["bg"] = "#38393D"

        print([list.get(i) for i in selection][0])
        cursor.execute("SELECT * FROM %s WHERE name = '%s'" % (table, [list.get(i) for i in selection][0]))
        rows = cursor.fetchone()

        def okCommand():
            viewWindow.destroy()

        lable = Label(viewWindow, relief=tk.FLAT, bg="#38393D", fg="#4D7992", font="Dosis", text=rows)
        btnOK = Button(viewWindow, relief=tk.FLAT, bg="#38393D", fg="#4D7992", font="Dosis", text="OK",command = okCommand)
        lable.pack()
        btnOK.pack()



def enterList():
    global LIST
    list.delete(0, END)
    LIST.clear()


    if comboList.get()=="Manager":

        selectByName("manager")
        #print("manager")
        #print(LIST)

    elif comboList.get()=="Guest":

        selectByName("guest")
        #print("manager")
        #print(LIST)

    elif comboList.get()=="Chef":

        selectByName("chef")
        #print("manager")
        #print(LIST)

    elif comboList.get()=="Room":

        selectByName("room")
        #print("manager")
        #print(LIST)

    elif comboList.get()=="Receptionist":

        selectByName("receptionist")
        #print("manager")
        #print(LIST)

    list.delete(0, END)
    list.insert(0, *LIST)



def viewSelectionBTN():
    if comboList.get()=="Manager":
        viewSelection("manager")



    elif comboList.get()=="Guest":
        viewSelection("guest")



    elif comboList.get()=="Chef":
        viewSelection("chef")

    elif comboList.get()=="Room":
        viewSelection("room")

    elif comboList.get()=="Receptionist":
        viewSelection("receptionist")



def deleteLogic(table):
    cursor = myConnection.cursor()
    selection = list.curselection()
    if [list.get(i) for i in selection] != []:
        cursor.execute("DELETE FROM %s WHERE name = '%s'" % (table, [list.get(i) for i in selection][0]))
        myConnection.commit()




def deleteSelection():
    if comboList.get()=="Manager":
        deleteLogic('manager')



    elif comboList.get()=="Guest":
        deleteLogic('guest')



    elif comboList.get()=="Chef":
        deleteLogic('chef')

    elif comboList.get()=="Room":
        deleteLogic('room')

    elif comboList.get()=="Receptionist":
        deleteLogic('receptionist')


def showList():
    if comboList.get() == "Manager":
        sql_select_Query = "select * from manager"
        cursor = myConnection.cursor(dictionary=True)
        cursor.execute(sql_select_Query)
        records = cursor.fetchall()
        lise1 = []
        for row in records:
            id = row["id"]
            name = row["name"]
            phone = row["phone"]
            gender = row["gender"]
            room = row["room"]
            if gender == 1:
                gender = "male"
            elif gender == 2:
                gender = "female"
            lise1.append("\n"+' , '.join((str(id), str(name), str(phone), str(gender), str(room))))


    elif comboList.get() == "Guest":
        sql_select_Query = "select * from guest"
        cursor = myConnection.cursor(dictionary=True)
        cursor.execute(sql_select_Query)
        records = cursor.fetchall()
        lise1 = []
        for row in records:
            id = row["id"]
            name = row["name"]
            sname = row["sname"]
            phone = row["phone"]
            gender = row["gender"]
            room = row["room"]
            city = row["city"]
            country = row["country"]
            date1 = row["date1"]
            date2 = row["dare2"]
            email = row["email"]
            if gender == 1:
                gender = "male"
            elif gender == 2:
                gender = "female"
            lise1.append("\n"+' , '.join( (str(id), str(name), str(sname), str(phone), str(gender),str(room), str(city), str(country), str(date1), str(date2), str(email),)))

    elif comboList.get() == "Chef":
        sql_select_Query = "select * from chef"
        cursor = myConnection.cursor(dictionary=True)
        cursor.execute(sql_select_Query)
        records = cursor.fetchall()
        lise1 = []
        for row in records:
            id = row["id"]
            name = row["name"]
            gender = row["gender"]
            room = row["room"]
            if gender == 1:
                gender = "male"
            elif gender == 2:
                gender = "female"
            lise1.append("\n"+' , '.join((str(id), str(name), str(gender), str(room))))

    elif comboList.get() == "Room":
        sql_select_Query = "select * from room"
        cursor = myConnection.cursor(dictionary=True)
        cursor.execute(sql_select_Query)
        records = cursor.fetchall()
        lise1 = []
        for row in records:

            id = row["id"]
            location = row["location"]
            type = row["type"]
            name = row["name"]


            lise1.append("\n"+' , '.join((str(id), str(location), str(type), str(name))))

    elif comboList.get() == "Receptionist":
        sql_select_Query = "select * from receptionist"
        cursor = myConnection.cursor(dictionary=True)
        cursor.execute(sql_select_Query)
        records = cursor.fetchall()
        lise1 = []
        for row in records:
            id = row["id"]
            name = row["name"]
            phone = row["phone"]
            gender = row["gender"]
            room = row["room"]
            if gender == 1:
                gender = "male"
            elif gender == 2:
                gender = "female"
            lise1.append("\n"+' , '.join((str(id), str(name), str(phone), str(gender), str(room))))



    viewWindow = tk.Toplevel(window)
    viewWindow["bg"] = "#38393D"



    def okCommand():
        viewWindow.destroy()

    lable = Label(viewWindow, relief=tk.FLAT, bg="#38393D", fg="#4D7992", font="Dosis",text=lise1)
    btnOK = Button(viewWindow, relief=tk.FLAT, bg="#38393D", fg="#4D7992", font="Dosis", text="OK",command=okCommand)

    lable.pack()
    btnOK.pack()


def insertToTable():
    if comboList.get() == "Manager":
        insertManagerWindow = tk.Tk()
        insertManagerWindow.geometry("300x470")
        insertManagerWindow.title("insert manager")
        insertManagerWindow.resizable(False,False)
        insertManagerWindow["bg"] = "#27292D"




        def submitBtn():
            cursor = myConnection.cursor()
            sql = "INSERT INTO manager (id, name, gender,phone,room) VALUES (%s, %s, %s, %s, %s)"
            print(int(idTxt.get()), str(nameTxt.get()), int(phoneTxt.get()), int(genderTxt.get()), int(roomTxt.get()) )
            print(int(idTxt.get()))
            val = (int(idTxt.get()), str(nameTxt.get()),  int(genderTxt.get()),int(phoneTxt.get()), int(roomTxt.get()) )
            #val = (1, "nameqwerty", 1, 1, 1)
            cursor.execute(sql, val)
            myConnection.commit()



        idTxt = Entry(insertManagerWindow, relief=tk.FLAT, bg="#38393D", fg="#4D7992", font="Dosis")
        nameTxt = Entry(insertManagerWindow, relief=tk.FLAT, bg="#38393D", fg="#4D7992", font="Dosis")
        phoneTxt = Entry(insertManagerWindow, relief=tk.FLAT, bg="#38393D", fg="#4D7992", font="Dosis")
        genderTxt = Entry(insertManagerWindow, relief=tk.FLAT, bg="#38393D", fg="#4D7992", font="Dosis")
        roomTxt = Entry(insertManagerWindow, relief=tk.FLAT, bg="#38393D", fg="#4D7992", font="Dosis")

        idLabel = Label(insertManagerWindow, relief=tk.FLAT, bg="#38393D", fg="#4D7992", font="Dosis",text="id (int)")
        nameLabel = Label(insertManagerWindow, relief=tk.FLAT, bg="#38393D", fg="#4D7992", font="Dosis",text="name (str)")
        phoneLabel = Label(insertManagerWindow, relief=tk.FLAT, bg="#38393D", fg="#4D7992", font="Dosis",text="phone (int)")
        genderLabel = Label(insertManagerWindow, relief=tk.FLAT, bg="#38393D", fg="#4D7992", font="Dosis",text="gender (1-male/2-female)")
        roomLabel = Label(insertManagerWindow, relief=tk.FLAT, bg="#38393D", fg="#4D7992", font="Dosis",text="room (room number)")

        submit = Button(insertManagerWindow, relief=tk.FLAT, bg="#38393D", fg="#4D7992", font="Dosis",text="submit",command=submitBtn)

        margin = 10
        lbl = 30
        txt= 30

        idLabel.place(x=5,y=margin,width=290,height=lbl)
        idTxt.place(x=5,y=lbl+margin*2,width=290,height=txt)
        nameLabel.place(x=5, y=txt+lbl+margin*3, width=290, height=lbl)
        nameTxt.place(x=5, y=txt+lbl*2+margin*4, width=290, height=txt)
        phoneLabel.place(x=5, y=txt*2+lbl*2+margin*5, width=290, height=lbl)
        phoneTxt.place(x=5, y=txt*2+lbl*3+margin*6, width=290, height=txt)
        genderLabel.place(x=5, y=txt*3+lbl*3+margin*7, width=290, height=lbl)
        genderTxt.place(x=5, y=txt*3+lbl*4+margin*8, width=290, height=txt)
        roomLabel.place(x=5, y=txt*4+lbl*4+margin*9, width=290, height=lbl)
        roomTxt.place(x=5, y=txt*4+lbl*5+margin*10, width=290, height=txt)
        submit.place(x=5, y=txt*5+lbl*5+margin*11, width=290, height=50)

    elif comboList.get() == 'Chef':
        insertManagerWindow = tk.Tk()
        insertManagerWindow.geometry("300x470")
        insertManagerWindow.title("insert chef")
        insertManagerWindow.resizable(False, False)
        insertManagerWindow["bg"] = "#27292D"

        def submitBtn():
            cursor = myConnection.cursor()
            sql = "INSERT INTO chef (id, name, gender,room) VALUES (%s, %s, %s, %s)"
            print(int(idTxt.get()), str(nameTxt.get()), int(genderTxt.get()), int(roomTxt.get()))
            val = (int(idTxt.get()), str(nameTxt.get()), int(genderTxt.get()), int(roomTxt.get()))
            # val = (1, "nameqwerty", 1, 1, 1)
            cursor.execute(sql, val)
            myConnection.commit()

        idTxt = Entry(insertManagerWindow, relief=tk.FLAT, bg="#38393D", fg="#4D7992", font="Dosis")
        nameTxt = Entry(insertManagerWindow, relief=tk.FLAT, bg="#38393D", fg="#4D7992", font="Dosis")

        genderTxt = Entry(insertManagerWindow, relief=tk.FLAT, bg="#38393D", fg="#4D7992", font="Dosis")
        roomTxt = Entry(insertManagerWindow, relief=tk.FLAT, bg="#38393D", fg="#4D7992", font="Dosis")

        idLabel = Label(insertManagerWindow, relief=tk.FLAT, bg="#38393D", fg="#4D7992", font="Dosis", text="id (int)")
        nameLabel = Label(insertManagerWindow, relief=tk.FLAT, bg="#38393D", fg="#4D7992", font="Dosis",
                          text="name (str)")

        genderLabel = Label(insertManagerWindow, relief=tk.FLAT, bg="#38393D", fg="#4D7992", font="Dosis",
                            text="gender (1-male/2-female)")
        roomLabel = Label(insertManagerWindow, relief=tk.FLAT, bg="#38393D", fg="#4D7992", font="Dosis",
                          text="room (room number)")

        submit = Button(insertManagerWindow, relief=tk.FLAT, bg="#38393D", fg="#4D7992", font="Dosis", text="submit",
                        command=submitBtn)

        margin = 10
        lbl = 30
        txt = 30

        idLabel.place(x=5, y=margin, width=290, height=lbl)
        idTxt.place(x=5, y=lbl + margin * 2, width=290, height=txt)
        nameLabel.place(x=5, y=txt + lbl + margin * 3, width=290, height=lbl)
        nameTxt.place(x=5, y=txt + lbl * 2 + margin * 4, width=290, height=txt)
        genderLabel.place(x=5, y=txt * 3 + lbl * 3 + margin * 7, width=290, height=lbl)
        genderTxt.place(x=5, y=txt * 3 + lbl * 4 + margin * 8, width=290, height=txt)
        roomLabel.place(x=5, y=txt * 4 + lbl * 4 + margin * 9, width=290, height=lbl)
        roomTxt.place(x=5, y=txt * 4 + lbl * 5 + margin * 10, width=290, height=txt)
        submit.place(x=5, y=txt * 5 + lbl * 5 + margin * 11, width=290, height=50)

    elif comboList.get() == 'Receptionist':
        insertManagerWindow = tk.Tk()
        insertManagerWindow.geometry("300x470")
        insertManagerWindow.title("insert receptionist")
        insertManagerWindow.resizable(False, False)
        insertManagerWindow["bg"] = "#27292D"

        def submitBtn():
            cursor = myConnection.cursor()
            sql = "INSERT INTO receptionist (id, name, gender,phone,room) VALUES (%s, %s, %s, %s, %s)"
            print(int(idTxt.get()), str(nameTxt.get()), int(phoneTxt.get()), int(genderTxt.get()), int(roomTxt.get()))
            print(int(idTxt.get()))
            val = (int(idTxt.get()), str(nameTxt.get()), int(genderTxt.get()), int(phoneTxt.get()), int(roomTxt.get()))
            # val = (1, "nameqwerty", 1, 1, 1)
            cursor.execute(sql, val)
            myConnection.commit()

        idTxt = Entry(insertManagerWindow, relief=tk.FLAT, bg="#38393D", fg="#4D7992", font="Dosis")
        nameTxt = Entry(insertManagerWindow, relief=tk.FLAT, bg="#38393D", fg="#4D7992", font="Dosis")
        phoneTxt = Entry(insertManagerWindow, relief=tk.FLAT, bg="#38393D", fg="#4D7992", font="Dosis")
        genderTxt = Entry(insertManagerWindow, relief=tk.FLAT, bg="#38393D", fg="#4D7992", font="Dosis")
        roomTxt = Entry(insertManagerWindow, relief=tk.FLAT, bg="#38393D", fg="#4D7992", font="Dosis")

        idLabel = Label(insertManagerWindow, relief=tk.FLAT, bg="#38393D", fg="#4D7992", font="Dosis", text="id (int)")
        nameLabel = Label(insertManagerWindow, relief=tk.FLAT, bg="#38393D", fg="#4D7992", font="Dosis",
                          text="name (str)")
        phoneLabel = Label(insertManagerWindow, relief=tk.FLAT, bg="#38393D", fg="#4D7992", font="Dosis",
                           text="phone (int)")
        genderLabel = Label(insertManagerWindow, relief=tk.FLAT, bg="#38393D", fg="#4D7992", font="Dosis",
                            text="gender (1-male/2-female)")
        roomLabel = Label(insertManagerWindow, relief=tk.FLAT, bg="#38393D", fg="#4D7992", font="Dosis",
                          text="room (room number)")

        submit = Button(insertManagerWindow, relief=tk.FLAT, bg="#38393D", fg="#4D7992", font="Dosis", text="submit",
                        command=submitBtn)

        margin = 10
        lbl = 30
        txt = 30

        idLabel.place(x=5, y=margin, width=290, height=lbl)
        idTxt.place(x=5, y=lbl + margin * 2, width=290, height=txt)
        nameLabel.place(x=5, y=txt + lbl + margin * 3, width=290, height=lbl)
        nameTxt.place(x=5, y=txt + lbl * 2 + margin * 4, width=290, height=txt)
        phoneLabel.place(x=5, y=txt * 2 + lbl * 2 + margin * 5, width=290, height=lbl)
        phoneTxt.place(x=5, y=txt * 2 + lbl * 3 + margin * 6, width=290, height=txt)
        genderLabel.place(x=5, y=txt * 3 + lbl * 3 + margin * 7, width=290, height=lbl)
        genderTxt.place(x=5, y=txt * 3 + lbl * 4 + margin * 8, width=290, height=txt)
        roomLabel.place(x=5, y=txt * 4 + lbl * 4 + margin * 9, width=290, height=lbl)
        roomTxt.place(x=5, y=txt * 4 + lbl * 5 + margin * 10, width=290, height=txt)
        submit.place(x=5, y=txt * 5 + lbl * 5 + margin * 11, width=290, height=50)

        #-----------------------------------------------------------------------------------------------------------------------------------------------
    elif comboList.get() == 'Guest':
        insertManagerWindow = tk.Tk()
        insertManagerWindow.geometry("300x640")
        insertManagerWindow.title("insert room")
        insertManagerWindow.resizable(False, False)
        insertManagerWindow["bg"] = "#27292D"

        def submitBtn():
            cursor = myConnection.cursor()
            sql = "INSERT INTO guest (id, name,sname,gender,phone,room,city,country,date1,date2,email) VALUES (%s, %s, %s, %s,%s, %s, %s, %s,%s, %s, %s)"
            date1D = datetime.strptime(date1Txt.get(), '%m-%d-%Y').date()
            date2D = datetime.strptime(date2Txt.get(), '%m-%d-%Y').date()
            val = (int(idTxt.get()),nameTxt.get(),snameTxt.get(),int(genderTxt.get()),int(phoneTxt.get()),int(roomTxt.get()),cityTxt.get(),countryTxt.get(),date1D,date2D,emailTxt.get())
            # val = (1, "nameqwerty", 1, 1, 1)
            cursor.execute(sql, val)
            myConnection.commit()

        idTxt      = Entry(insertManagerWindow, relief=tk.FLAT, bg="#38393D", fg="#4D7992", font="Dosis")
        nameTxt    = Entry(insertManagerWindow, relief=tk.FLAT, bg="#38393D", fg="#4D7992", font="Dosis")
        snameTxt   = Entry(insertManagerWindow, relief=tk.FLAT, bg="#38393D", fg="#4D7992", font="Dosis")
        phoneTxt   = Entry(insertManagerWindow, relief=tk.FLAT, bg="#38393D", fg="#4D7992", font="Dosis")
        genderTxt  = Entry(insertManagerWindow, relief=tk.FLAT, bg="#38393D", fg="#4D7992", font="Dosis")
        roomTxt    = Entry(insertManagerWindow, relief=tk.FLAT, bg="#38393D", fg="#4D7992", font="Dosis")
        cityTxt    = Entry(insertManagerWindow, relief=tk.FLAT, bg="#38393D", fg="#4D7992", font="Dosis")
        countryTxt = Entry(insertManagerWindow, relief=tk.FLAT, bg="#38393D", fg="#4D7992", font="Dosis")
        date1Txt   = Entry(insertManagerWindow, relief=tk.FLAT, bg="#38393D", fg="#4D7992", font="Dosis")
        date2Txt   = Entry(insertManagerWindow, relief=tk.FLAT, bg="#38393D", fg="#4D7992", font="Dosis")
        emailTxt   = Entry(insertManagerWindow, relief=tk.FLAT, bg="#38393D", fg="#4D7992", font="Dosis")


        idLabel      = Label(insertManagerWindow, relief=tk.FLAT, bg="#38393D", fg="#4D7992", font="Dosis", text="id (int)")
        nameLabel    = Label(insertManagerWindow, relief=tk.FLAT, bg="#38393D", fg="#4D7992", font="Dosis",text="name (str)")
        snameLabel   = Label(insertManagerWindow, relief=tk.FLAT, bg="#38393D", fg="#4D7992", font="Dosis",text="sname (str)")
        phoneLabel   = Label(insertManagerWindow, relief=tk.FLAT, bg="#38393D", fg="#4D7992", font="Dosis",text="phone (int)")
        genderLabel  = Label(insertManagerWindow, relief=tk.FLAT, bg="#38393D", fg="#4D7992", font="Dosis",text="gender (1-male/2-female)")
        roomLabel    = Label(insertManagerWindow, relief=tk.FLAT, bg="#38393D", fg="#4D7992", font="Dosis",text="room (room number)")
        cityLabel    = Label(insertManagerWindow, relief=tk.FLAT, bg="#38393D", fg="#4D7992", font="Dosis", text="city(str)")
        countryLabel = Label(insertManagerWindow, relief=tk.FLAT, bg="#38393D", fg="#4D7992", font="Dosis",text="country(str)")
        date1Label   = Label(insertManagerWindow, relief=tk.FLAT, bg="#38393D", fg="#4D7992", font="Dosis",text="date 1 (date)")
        date2Label   = Label(insertManagerWindow, relief=tk.FLAT, bg="#38393D", fg="#4D7992", font="Dosis",text="date 2 (date)")
        emailLabel   = Label(insertManagerWindow, relief=tk.FLAT, bg="#38393D", fg="#4D7992", font="Dosis",text="email (email)")

        submit = Button(insertManagerWindow, relief=tk.FLAT, bg="#38393D", fg="#4D7992", font="Dosis", text="submit",command=submitBtn)


        margin = 10
        lbl = 30
        txt = 30













        idLabel.pack()
        idTxt.pack()
        nameLabel.pack()
        nameTxt.pack()
        snameLabel.pack()
        snameTxt.pack()
        phoneLabel.pack()
        phoneTxt.pack()
        genderLabel.pack()
        genderTxt.pack()
        roomLabel.pack()
        roomTxt.pack()
        cityLabel.pack()
        cityTxt.pack()
        countryLabel.pack()
        countryTxt.pack()
        date1Label.pack()
        date1Txt.pack()
        date2Label.pack()
        date2Txt.pack()
        emailLabel.pack()
        emailTxt.pack()
        submit.pack()



    elif comboList.get() == 'Room':
        insertManagerWindow = tk.Tk()
        insertManagerWindow.geometry("300x470")
        insertManagerWindow.title("insert room")
        insertManagerWindow.resizable(False, False)
        insertManagerWindow["bg"] = "#27292D"

        def submitBtn():
            cursor = myConnection.cursor()
            sql = "INSERT INTO room (id, location,type,name) VALUES (%s, %s, %s, %s)"
            #print(int(idTxt.get()), str(nameTxt.get()), int(phoneTxt.get()), int(genderTxt.get()), int(roomTxt.get()))
            #print(int(idTxt.get()))
            val = (int(idTxt.get()), str(locationTxt.get()), str(typeTxt.get()), str(nameTxt.get()))
            # val = (1, "nameqwerty", 1, 1, 1)
            cursor.execute(sql, val)
            myConnection.commit()

        idTxt = Entry(insertManagerWindow, relief=tk.FLAT, bg="#38393D", fg="#4D7992", font="Dosis")
        nameTxt = Entry(insertManagerWindow, relief=tk.FLAT, bg="#38393D", fg="#4D7992", font="Dosis")
        locationTxt = Entry(insertManagerWindow, relief=tk.FLAT, bg="#38393D", fg="#4D7992", font="Dosis")
        typeTxt = Entry(insertManagerWindow, relief=tk.FLAT, bg="#38393D", fg="#4D7992", font="Dosis")
        idLabel = Label(insertManagerWindow, relief=tk.FLAT, bg="#38393D", fg="#4D7992", font="Dosis", text="id (int)")
        nameLabel = Label(insertManagerWindow, relief=tk.FLAT, bg="#38393D", fg="#4D7992", font="Dosis",text="name (str)")
        locationLabel = Label(insertManagerWindow, relief=tk.FLAT, bg="#38393D", fg="#4D7992", font="Dosis",text="location(str)")
        typeLabel = Label(insertManagerWindow, relief=tk.FLAT, bg="#38393D", fg="#4D7992", font="Dosis",text="room (type(str)")
        submit = Button(insertManagerWindow, relief=tk.FLAT, bg="#38393D", fg="#4D7992", font="Dosis", text="submit",command=submitBtn)

        margin = 10
        lbl = 30
        txt = 30

        idLabel.place(x=5, y=margin, width=290, height=lbl)
        idTxt.place(x=5, y=lbl + margin * 2, width=290, height=txt)
        nameLabel.place(x=5, y=txt + lbl + margin * 3, width=290, height=lbl)
        nameTxt.place(x=5, y=txt + lbl * 2 + margin * 4, width=290, height=txt)
        locationLabel.place(x=5, y=txt * 3 + lbl * 3 + margin * 7, width=290, height=lbl)
        locationTxt.place(x=5, y=txt * 3 + lbl * 4 + margin * 8, width=290, height=txt)
        typeLabel.place(x=5, y=txt * 4 + lbl * 4 + margin * 9, width=290, height=lbl)
        typeTxt.place(x=5, y=txt * 4 + lbl * 5 + margin * 10, width=290, height=txt)
        submit.place(x=5, y=txt * 5 + lbl * 5 + margin * 11, width=290, height=50)


def searchLogic(List,key):
    cursor =myConnection.cursor()
    cursor.execute("SELECT * FROM %s WHERE name = '%s'" % (List,  key))
    rows =cursor.fetchone()
    print(rows)
    windowSearch = Tk()
    windowSearch["bg"] = "#38393D"
    windowSearch.geometry("300x30")
    if rows != None:
        lableS = Label(windowSearch,text=rows,relief=tk.FLAT, bg="#38393D", fg="#4D7992",font="Dosis")
        lableS.pack()
    else:
        lableS = Label(windowSearch, text="object not found", relief=tk.FLAT, bg="#38393D", fg="#4D7992", font="Dosis")
        lableS.pack()




def search():

    if comboList.get() == "Manager":
        searchLogic("manager",txtE.get())
        #print(txtE.get())


    elif comboList.get() == "Guest":
        searchLogic("guest",txtE.get())




    elif comboList.get() == "Chef":
        searchLogic("chef",txtE.get())

    elif comboList.get() == "Room":
        searchLogic("room",txtE.get())

    elif comboList.get() == "Receptionist":
        searchLogic("receptionist",txtE.get())



window = tk.Tk()
window.geometry("500x300")
window.title("title")
window.resizable(False,False)
window["bg"] = "#38393D"

canvas = tk.Canvas(window,bg="#27292D",relief=tk.FLAT, highlightthickness=0)
canvas.place(x=1,y=52,width=300,height=200)

canvasButtons = tk.Canvas(window,bg="#27292D",relief=tk.FLAT, highlightthickness=0)
canvasButtons.place(x=300,y=52,width=200,height=200)

showList = tk.Button(canvasButtons, text="show list",command=showList,relief=tk.FLAT, bg="#38393D", fg="#4D7992",font="Dosis")
insertBtn = tk.Button(canvasButtons, text="insert",command=insertToTable,relief=tk.FLAT, bg="#38393D", fg="#4D7992",font="Dosis")
txtE = Entry(canvasButtons,relief=tk.FLAT, bg="#38393D", fg="#4D7992",font="Dosis")
searchBtn = tk.Button(canvasButtons, text="search",command=search,relief=tk.FLAT, bg="#38393D", fg="#4D7992",font="Dosis")

showList.place(x=5, y=5, width=190, height=35)
insertBtn.place(x=5, y=45, width=190, height=35)
txtE.place(x=5, y=125, width=190, height=35)
searchBtn.place(x=5, y=85, width=190, height=35)


canvasHeader = tk.Canvas(window,bg="#27292D",relief=tk.FLAT, highlightthickness=0)
canvasHeader.place(x=1,y=1,width=498,height=50)

style= ttk.Style()
style.theme_use('clam')
style.configure("TCombobox",relief=tk.FLAT,foreground="#4D7992",background="#38393D",fieldbackground="#27292D",darkcolor="#27292D",lightcolor="#27292D",selectbackground="#27292D",selectforeground="#27292D",bordercolor="#27292D",insertcolor="#27292D",insertwidth="#27292D",arrowsize="#27292D",arrowcolor="#4D7992",)


comboList = ttk.Combobox(canvasHeader, style="TCombobox")
comboList['values'] = ("Manager", "Guest", "Chef", "Room","Receptionist")
comboList.current(0)
comboList.place(x=5, y=5, width=100, height=40)

okButton = tk.Button(canvasHeader, text="ok",command=enterList,relief=tk.FLAT, bg="#38393D", fg="#4D7992",font="Dosis")

okButton.place(x=110, y=5, width=50, height=40)

canvasFooter = tk.Canvas(window,bg="#27292D",relief=tk.FLAT, highlightthickness=0)
canvasFooter.place(x=1,y=251,width=498,height=50)

watermark = tk.Label(canvasFooter,relief=tk.FLAT,text="Hotel management system by Taron Sargsyan",bg="#27292D", fg="#4D7992",font="Dosis")
watermark.place(x=5,y=15)

list = tk.Listbox(canvas,relief=tk.FLAT, bg="#38393D", fg="#4D7992",font="Dosis", highlightthickness=0)
list.insert(0, *LIST)
delete_btn = tk.Button(canvas, text="delete",command=deleteSelection,relief=tk.FLAT, bg="#38393D", fg="#4D7992",font="Dosis")
view_btn = tk.Button(canvas, text="view",command=viewSelectionBTN,relief=tk.FLAT, bg="#38393D", fg="#4D7992",font="Dosis")

list.place(x=5, y=5, width=290, height=150)
delete_btn.place(x=5, y=160, width=143, height=35)
view_btn.place(x=152, y=160, width=143, height=35)

window.mainloop()

#cursor = myConnection.cursor()
#for i in range (3,100):
#                sql = "INSERT INTO manager (id, name, gender,phone,room) VALUES (%s, %s, %s, %s, %s)"
#                val = (i, "name" + str(i), 1, i*2, 2)
#                cursor.execute(sql, val)
#                myConnection.commit()

#date_str = '09-19-2018'
#
#date_object = datetime.strptime(date_str, '%m-%d-%Y').strftime('%m-%d-%Y')
#print(type(date_object))
#print(date_object)
