
class Tag:
    __id = 0
    __title = ''
    __description = ''
    __color = ''
    __check_first_time = True
    __list_X_coordinates = []
    __list_Y_coordinates = []

    def __init__(self, id, title, description):
        self.__id = id
        self.__title = title
        self.__description = description
        self.__list_Y_coordinates = []
        self.__list_X_coordinates = []

    def __init__(self):
        self.__id = id
        self.__title = ''
        self.__description = ''
        self.__list_Y_coordinates = []
        self.__list_X_coordinates = []

    def printData(self):
        print(self.__id, self.__title,self.__description, sep='\n')
        print('-----')

    def addXCoordinates(self, value):
        self.__list_X_coordinates.append(value)

    def addYCoordinates(self, value):
        self.__list_Y_coordinates.append(value)

    def getID(self):
        return self.__id

    def setID(self, id):
        self.__id = id

    def getColor(self):
        return self.__color

    def setColor(self, color):
        self.__color = color

    def getCheck(self):
        return self.__check_first_time

    def setCheck(self, check):
        self.__check_first_time = check

    def getTitle(self):
        return self.__title

    def setTitle(self, title):
        self.__title = title

    def getDescription(self):
        return self.__description

    def setDescription(self, description):
        self.__description = description

    def getList_X_coordinates(self):
        return self.__list_X_coordinates

    def setList_X_coordinates(self, list_X_coordinates):
        self.__list_X_coordinates = list_X_coordinates

    def getList_Y_coordinates(self):
        return self.__list_Y_coordinates

    def setList_Y_coordinates(self, list_Y_coordinates):
        self.__list_Y_coordinates = list_Y_coordinates
