from person import *


class Receptionist(Person):
    def __init__(self, name, id, gender, pphone, loc):
        super().__init__(name, id, gender)
        self.phone = pphone
        self.location = loc

    def get_phone(self):
        return self.pphone

    def set_phone(self, phone):
        self.pphone = phone

    def get_location(self):
        return self.loc

    def set_location(self, location):
        self.loc = location

    def showInfo(self):
        print(self.name, self.id, self.gender, self.pphone, self.loc)


    def CheckRoomAvailability(self):
        print("test")

    def BookRoom(self):
        pass

    def GenerateBill(self):
        pass

    def AcceptCustomFeedback(self):
        pass

    phone = property(get_phone, set_phone)
    location = property(get_location, set_location)