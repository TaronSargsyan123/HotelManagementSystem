class Inventory:
    def __init__(self, type, status):
        self.__type = type
        self.__status = status

    def printStatus(self):
        print(self.status)

    def get_type(self):
        return self.type

    def set_type(self, type):
        self.type = type

    def get_status(self):
        return self.status

    def set_status(self, status):
        self.type = status

    type = property(get_type, set_type)
    type = property(get_type, set_type)