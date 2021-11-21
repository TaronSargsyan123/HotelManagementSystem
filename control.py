class Control:
    def controlInput(self, inputContent, info):
        if info == "1":
            while True:
                print("enter 1-ManagerList, 2-GuestList, 3-ChefList, 4-RoomsList, 5-ReceptionistList --> ")
                while True:
                    searchList = inputContent.userInput("enter list --> ")
                    searchKeyword = inputContent.userInput("enter id --> ")
                    inputContent.searchObj(searchList,searchKeyword)
                    if searchList or searchKeyword == "break":
                        break

        elif info == "2":
           while True:
               inputContent.showMenu()
               inputNumber = inputContent.userInput("enter your number")
               print(inputNumber)
               inputContent.showList(inputNumber)
               if inputNumber == "break":
                   break

        elif info == "3":
            while True:
                ListNumber = input("enter 1-ManagerList, 2-GuestList, 3-ChefList, 4-RoomsList, 5-ReceptionistList --> ")
                if ListNumber == "1":
                    inputContent.Add_Manager()
                elif ListNumber == "2":
                    inputContent.Add_Guest()
                elif ListNumber == "3":
                    inputContent.Add_Chef()
                elif ListNumber == "4":
                    inputContent.Add_Room()
                elif ListNumber == "5":
                    inputContent.Add_Receptionist()
                elif ListNumber == "break":
                   break