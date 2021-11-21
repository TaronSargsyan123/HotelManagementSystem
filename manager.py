from person import *


class Manager(Person):
    def __init__(self, name, id, gender, phone, location):
        super().__init__(name, id,gender)
        self.__phone = phone
        self.__location = location

    def get_phone(self):
        return self.__phone

    def set_phone(self, phone):
        self.__phone = phone

    def get_location(self):
        return self.__location

    def set_location(self, location):
        self.__location = location

    def showInfo(self):
        print(self.name, self.id, self.phone, self.location)


    phone = property(get_phone, set_phone)
    location = property(get_location, set_location)