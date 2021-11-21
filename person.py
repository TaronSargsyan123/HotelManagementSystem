class Person:
    def __init__(self,name,id,gender):
        self.__name = name
        self.__id = id
        self.__gender = gender


    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id

    def get_gender(self):
        return self.__gender

    def set_gender(self, gender):
        self.__gender = gender

    name = property(get_name, set_name)
    id = property(get_id, set_id)
    gender = property(get_gender, set_gender)

