import mysql.connector

hostname = 'localhost'
username = 'root'
password = ''
database = 'hoteldb'





class Input:
    try:
        myConnection = mysql.connector.connect(host=hostname, user=username, password=password, db=database)
        print("succsesfuly connected...")

        def showMenu(self):
           print("From database shows tables")
           print("enter 1-ManagerList, 2-GuestList, 3-ChefList, 4-RoomsList, 5-ReceptionistList --> ")

        def userInput(self,text):
           return(input(text))


        def forItem(self,objectList):
           for item in objectList:
               item.showInfo()


        def showList(self,listNumber):
            if listNumber == "1":
                self.myConnection = mysql.connector.connect(host=hostname, user=username, password=password, db=database)
                print("Manager atributes --> name, id, gender, phone number, room")
                print("the manager list content...")
                #self.forItem(ManagerList)
                try:
                    with self.myConnection.cursor() as cursor:
                        sql_select_Query = "select * from manager"
                        cursor = self.myConnection.cursor(dictionary=True)
                        cursor.execute(sql_select_Query)
                        records = cursor.fetchall()

                        print("#"*100)
                        for row in records:
                            self.id = row["id"]
                            self.name = row["name"]
                            self.phone = row["phone"]
                            self.gender_date = row["gender"]
                            self.room_date = row["room"]
                            if self.gender_date == 1:
                                self.gender_date = "male"
                            elif self.gender_date == 2:
                                self.gender_date = "female"
                            print(self.id, self.name, self.phone, self.gender_date, self.room_date)
                        print("#" * 100)
                finally:
                    self.myConnection.close()



            if listNumber == "2":
                self.myConnection = mysql.connector.connect(host=hostname, user=username, password=password,
                                                            db=database)
                print("Guest atributs --> name, id, gender, phone number, room, address, city, country, passport, sname, date 1, date 2, email")
                print("the guest list content...")




                try:
                    with self.myConnection.cursor() as cursor:
                        sql_select_Query = "select * from guest"
                        # MySQLCursorDict creates a cursor that returns rows as dictionaries
                        cursor = self.myConnection.cursor(dictionary=True)
                        cursor.execute(sql_select_Query)
                        records = cursor.fetchall()

                        print("#"*100)
                        for row in records:
                            self.id = row["id"]
                            self.name = row["name"]
                            self.sname = row["sname"]
                            self.phone = row["phone"]
                            self.gender_date = row["gender"]
                            self.room_date = row["room"]
                            self.city = row["city"]
                            self.country = row["country"]
                            self.date1 = row["date1"]
                            self.dare2 = row["dare2"]
                            self.email = row["email"]
                            if self.gender_date == 1:
                                self.gender_date = "male"
                            elif self.gender_date == 2:
                                self.gender_date = "female"
                                # id	name	sname	gender	phone	room	address	city	country	date1	dare2	email
                            print(self.id, self.name, self.sname, self.gender_date,self.phone, self.room_date,self.city,self.country,self.date1,self.dare2,self.email)
                        print("#" * 100)
                finally:
                    print("FINAL")

            if listNumber == "3":
                self.myConnection = mysql.connector.connect(host=hostname, user=username, password=password,db=database)
                print("Chef atributes --> name, id, gender, room")
                print("the chef list content...")

                try:
                    with self.myConnection.cursor() as cursor:
                        sql_select_Query = "select * from chef"
                        cursor = self.myConnection.cursor(dictionary=True)
                        cursor.execute(sql_select_Query)
                        records = cursor.fetchall()

                        print("#" * 100)
                        for row in records:
                            self.id = row["id"]
                            self.name = row["name"]
                            self.gender_date = row["gender"]
                            self.room_date = row["room"]
                            if self.gender_date == 1:
                                self.gender_date = "male"
                            elif self.gender_date == 2:
                                self.gender_date = "female"
                            print(self.id, self.name, self.gender_date, self.room_date)
                        print("#" * 100)
                finally:
                    print("FINAL")

            if listNumber == "4":
                self.myConnection = mysql.connector.connect(host=hostname, user=username, password=password,
                                                            db=database)
                print("Room atributes --> id, location, room type, name")
                print("the rooms list content...")
                try:
                    with self.myConnection.cursor() as cursor:
                        sql_select_Query = "select * from room"

                        cursor = self.myConnection.cursor(dictionary=True)
                        cursor.execute(sql_select_Query)
                        records = cursor.fetchall()

                        print("#" * 100)
                        for row in records:
                            self.id = row["id"]
                            self.location = row["location"]
                            self.type = row["type"]
                            self.name = row["name"]
                            print(self.id, self.location, self.type, self.name)
                        print("#" * 100)
                finally:
                    print("FINAL")

            if listNumber == "5":
                self.myConnection = mysql.connector.connect(host=hostname, user=username, password=password,
                                                            db=database)
                print("Recetpionist atributes --> name, id, gender, phone number, room type")
                print("the receptionist list content...")
                try:
                    with self.myConnection.cursor() as self.cursor:
                        sql_select_Query = "select * from receptionist"

                        cursor = self.myConnection.cursor(dictionary=True)
                        cursor.execute(sql_select_Query)
                        records = cursor.fetchall()

                        print("#" * 100)
                        for row in records:
                            self.id = row["id"]
                            self.name = row["name"]
                            self.phone = row["phone"]
                            self.gender_date = row["gender"]
                            self.room_date = row["room"]
                            if self.gender_date == 1:
                                self.gender_date = "male"
                            elif self.gender_date == 2:
                                self.gender_date = "female"
                            print(self.id, self.name, self.phone, self.gender_date, self.room_date)
                        print("#" * 100)
                finally:
                    print("FINAL")





        def SearchInList(self,List,key):


            self.cursor = self.myConnection.cursor()
            self.cursor.execute("SELECT * FROM %s WHERE id = '%s'" % (List,key))
            self.rows = self.cursor.fetchone()
            print(self.rows)



        def searchObj(self,searchListNumber,key):
            if searchListNumber == "1":
                print("Manager atributes --> name, id, gender, phone number, room")
                self.SearchInList('manager', key)


            if searchListNumber == "2":
                print("Guest atributs --> name, id, gender, phone number, room, address, city, country, passport, sname, date 1, date 2, email")
                self.SearchInList('guest', key)

            if searchListNumber == "3":
                print("Chef atributes --> name, id, gender, phone number, room")
                self.SearchInList('chef', key)

            if searchListNumber == "4":
                print("Room atributes --> id, location, room type, name")
                self.SearchInList('room', key)

            if searchListNumber == "5":
                print("Recetpionist atributes --> name, id, gender, phone number, room type")
                self.SearchInList('receptionist', key)

        def Add_Manager(self):
            self.Manager_name = input("Manager name --> ")
            self.Manager_id = input("Manager id --> ")
            self.Manager_gender_info = input("Manager gender (m/f) --> ")
            self.Manager_phone = input("Manager phone --> ")
            self.Manager_room = input("Manager room --> ")
            self.response = input("Are you sure you want to add new Manager(y/n)?: ").lower()
            if(self.response != "y"):
                print("OK as You Want")
            else:
                if self.Manager_gender_info == "m":
                    self.Manager_gender = 1
                elif self.Manager_gender_info == "f":
                    self.Manager_gender = 2
                else: print("Error")

                self.cursor = self.myConnection.cursor()
                self.sql = "INSERT INTO manager (id, name, gender,phone,room) VALUES (%s, %s, %s, %s, %s)"
                self.val = (self.Manager_id,self.Manager_name,self.Manager_gender,self.Manager_phone,self.Manager_room)
                self.cursor.execute(self.sql, self.val)

                self.myConnection.commit()
                print("Adding new Manager____!!!!")

                showTable = input("press y to show Manager table --> ")
                if showTable == "y":
                    self.showList("1")
                else:
                    print("OK as You Want")


        def Add_Guest(self):
            self.Guest_name = input("Guest name --> ")
            self.Guest_id = input("Guest id --> ")
            self.Guest_gender_info = input("Guest gender (m/f) --> ")
            self.Guest_phone = input("Guest phone --> ")
            self.Guest_room = input("Guest room --> ")

            self.Guest_city = input("Guest city --> ")
            self.Guest_country = input("Guest country --> ")
            self.Guest_sname = input("Guest sname --> ")
            self.Guest_date1 = input("Guest date1 --> ")
            self.Guest_date2 = input("Guest date2 --> ")
            self.Guest_email = input("Guest email --> ")
            self.response = input("Are you sure you want to add new Guest(y/n)?: ").lower()
            if(self.response != "y"):
                print("OK as You Want")
            else:
                if self.Guest_gender_info == "m":
                    self.Guest_gender = 1
                elif self.Guest_gender_info == "f":
                    self.Guest_gender = 2
                else: print("Error")

                self.cursor = self.myConnection.cursor()
                self.sql = "INSERT INTO guest (id,name,sname,gender,phone,room,city,country,date1,dare2,email) VALUES (%s, %s, %s, %s,%s, %s, %s, %s, %s, %s, %s)"
                self.val = (self.Guest_id,self.Guest_name,self.Guest_sname,self.Guest_gender,self.Guest_phone,self.Guest_room,self.Guest_city,self.Guest_country,self.Guest_date1,self.Guest_date2,self.Guest_email)
                self.cursor.execute(self.sql, self.val)

                self.myConnection.commit()
                print("Adding new Guest____!!!!")

                showTable = input("press y to show Guest table --> ")
                if showTable == "y":
                    self.showList("2")
                else:
                    print("OK as You Want")


        def Add_Chef(self):
            self.Chef_name = input("Chef name --> ")
            self.Chef_id = input("Chef id --> ")
            self.Chef_gender_info = input("Chef gender (m/f) --> ")
            self.Chef_phone = input("Chef phone --> ")
            self.Chef_room = input("Chef room --> ")
            self.response = input("Are you sure you want to add new Chef(y/n)?: ").lower()
            if(self.response != "y"):
                print("OK as You Want")
            else:
                if self.Chef_gender_info == "m":
                    self.Chef_gender = 1
                elif self.Chef_gender_info == "f":
                    self.Chef_gender = 2
                else: print("Error")

                self.cursor = self.myConnection.cursor()
                self.sql = "INSERT INTO chef (id,name,gender,room) VALUES (%s, %s, %s, %s)"
                self.val = (self.Chef_id,self.Chef_name,self.Chef_gender,self.Chef_room)
                self.cursor.execute(self.sql, self.val)

                self.myConnection.commit()


                print("Adding new Chef____!!!!")

                showTable = input("press y to show Chef table --> ")
                if showTable == "y":
                    self.showList("3")
                else:
                    print("OK as You Want")



        def Add_Room(self):
            self.Room_id = input("Room id --> ")
            self.Room_location = input("Room location --> ")
            self.Room_type = input("Room type --> ")
            self.Room_name = input("Room name --> ")
            self.response = input("Are you sure you want to add new Room(y/n)?: ").lower()
            if(self.response != "y"):
                print("OK as You Want")
            else:

                self.cursor = self.myConnection.cursor()
                self.sql = "INSERT INTO room (id,location,type,name) VALUES (%s, %s, %s, %s)"
                self.val = (self.Room_id,self.Room_location,self.Room_type,self.Room_name)
                self.cursor.execute(self.sql, self.val)

                self.myConnection.commit()
                print("Adding new Room____!!!!")

                showTable = input("press y to show Room table --> ")
                if showTable == "y":
                    self.showList("4")
                else:
                    print("OK as You Want")

        def Add_Receptionist(self):
            self.Receptionist_name = input("Receptionist name --> ")
            self.Receptionist_id = input("Receptionist id --> ")
            self.Receptionist_gender_info = input("Receptionist gender (m/f) --> ")
            self.Receptionist_phone = input("Receptionist phone --> ")
            self.Receptionist_room = input("Receptionist room --> ")
            self.response = input("Are you sure you want to add new Receptionist(y/n)?: ").lower()
            if(self.response != "y"):
                print("OK as You Want")
            else:
                if self.Receptionist_gender_info == "m":
                    self.Receptionist_gender = 1
                elif self.Receptionist_gender_info == "f":
                    self.Receptionist_gender = 2
                else: print("Error")

                self.cursor = self.myConnection.cursor()
                self.sql = "INSERT INTO receptionist (id,name,gender,phone,room) VALUES (%s, %s, %s, %s,%s)"
                self.val = (self.Receptionist_id,self.Receptionist_name,self.Receptionist_gender,self.Receptionist_phone,self.Receptionist_room)
                self.cursor.execute(self.sql, self.val)

                self.myConnection.commit()
                print("Adding new Receptionist____!!!!")

                showTable = input("press y to show Receptionist table --> ")
                if showTable == "y":
                    self.showList("5")
                else:
                    print("OK as You Want")
    except:
        print("connection error...")