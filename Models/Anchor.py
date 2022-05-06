class Anchor:
    __id = ''
    __title = ''
    __current_value_posX = ''
    __current_value_posY = ''
    __isMaster = False

    def __init__(self, id, title, current_value_posX, current_value_posY, isMaster):
        self.__id = id
        self.__title = title
        self.__current_value_posX = current_value_posX
        self.__current_value_posY = current_value_posY
        self.__isMaster = isMaster

    def printData(self):
        print(self.__id, self.__title, self.__current_value_posX, self.__current_value_posY, self.__isMaster, sep='\n')
        print('-----')

    def getID(self):
        return self.__id

    def setID(self, id):
        self.__id = id

    def getTitle(self):
        return self.__title

    def setTitle(self, title):
        self.__title = title

    def getCurrentValuePosX(self):
        return self.__current_value_posX

    def setCurrentValuePosX(self, current_value_posX):
        self.__current_value_posX = current_value_posX

    def getCurrentValuePosY(self):
        return self.__current_value_posY

    def setCurrentValuePosY(self, current_value_posY):
        self.__current_value_posY = current_value_posY

    def getIsMaster(self):
        return self.__isMaster

    def setIsMaster(self, isMaster):
        self.__isMaster = isMaster
