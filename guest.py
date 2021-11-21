from person import *




class Guest(Person):
    def __init__(self, name, id, gender, phone, room, address, city, country, passport, sName, checkInDate, checkOutDate, email):
        super().__init__(name, id, gender)
        self.__phone = phone
        self.__room = room
        self.__address = address
        self.__city = city
        self.__country = country
        self.__passport = passport
        self.__sName = sName
        self.__checkInDate = checkInDate
        self.__checkOutDate = checkOutDate
        self.__email = email



    def get_phone(self):
        return self.__phone

    def set_phone(self, phone):
        if type(phone) == int:
            self.__phone = phone
        else:print("invalid volue")

    def get_room(self):
        return self.__room

    def set_room(self, room):
        self.__room = room

    def get_address(self):
        return self.__address

    def set_address(self, address):
        self.__room = address


    def get_city(self):
        return self.__city

    def set_city(self, city):
        self.__city = city

    def get_country(self):
        return self.__country

    def set_country(self, country):
        self.__country = country

    def get_passport(self):
        return self.__passport

    def set_passport(self, passport):
        self.__passport = passport

    def get_sName(self):
        return self.__sName

    def set_sName(self, sName):
        self.__sName = sName

    def get_checkInDate(self):
        return self.__checkInDate

    def set_checkInDate(self, checkInDate):
        self.__checkInDate = checkInDate

    def get_checkOutDate(self):
        return self.__checkOutDate

    def set_checkOutDate(self, checkOutDate):
        self.__checkOutDate = checkOutDate

    def get_email(self):
        return self.__email

    def set_email(self, email):
        self.__email = email

    def CheckIn(self):
        pass

    def CheckOut(self):
        pass

    def PayBill(self):
        pass

    def OrderFood(self):
        pass

    def SubmitFeedback(self):
        pass

    def showInfo(self):
        print(self.name, self.id, self.gender, self.phone, self.room, self.address, self.city, self.country, self.passport, self.sName, self.checkInDate, self.checkOutDate, self.email)

    phone = property(get_phone, set_phone)
    room = property(get_room, set_room)
    address = property(get_address, set_address)
    city = property(get_city, set_city)
    country = property(get_country, set_country)
    passport = property(get_passport, set_passport)
    sName = property(get_sName, set_sName)
    checkInDate = property(get_checkInDate, set_checkInDate)
    checkOutDate = property(get_checkOutDate, set_checkOutDate)
    email = property(get_email, set_email)
