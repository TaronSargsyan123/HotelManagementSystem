class Room:
    def __init__(self, roomN, loc, typpe, namme):
        self.roomNumber = roomN
        self.location = loc
        self.type = typpe
        self.name = namme

    def get_roomNumber(self):
        return self.roomN

    def set_roomNumber(self, roomNumber):
        self.roomN = roomNumber

    def get_location(self):
        return self.loc

    def set_location(self, location):
        self.loc = location

    def get_type(self):
        return self.typpe

    def set_type(self, type):
        self.typpe = type

    def get_name(self):
        return self.namme

    def set_name(self, name):
        self.namme = name

    def showInfo(self):
        print(self.namme,  self.loc, self.roomN, self.typpe)


    roomNumber = property(get_roomNumber, set_roomNumber)
    location = property(get_location, set_location)
    type = property(get_type, set_type)
    name = property(get_name,set_name)