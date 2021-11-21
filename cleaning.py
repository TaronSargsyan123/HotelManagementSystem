from person import *

class Cleaning(Person):
    def __init__(self, name, id, location):
        super().__init__(name, id)
        self.__location = location

    def cleanRoom(self):
        print("Clean Room")


    def get_location(self):
        return self.__location

    def set_location(self, location):
        self.__location = location

    location = property(get_location, set_location)