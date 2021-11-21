from person import *

class Chef(Person):
    def __init__(self, name, id, gender, location):
        super().__init__(name, id, gender)
        self.__location = location

    def TakeOrders(self):
        pass

    def get_location(self):
        return self.__location

    def set_location(self, location):
        self.__location = location

    def showInfo(self):
        print(self.name, self.id, self.gender, self.location)

    location = property(get_location, set_location)