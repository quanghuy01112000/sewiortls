class Coordinates:
    __posX = ''
    __posY = ''
    __atTime = ''

    def __int__(self):
        self.__posX = ''
        self.__posY = ''
        self.__atTime = ''

    # def __int__(self, posX, posY, atTime):
    #     self.__posX = posX
    #     self.__posY = posY
    #     self.__atTime = atTime

    def getPosX(self):
        return self.__posX

    def setPosX(self,posX):
        self.__posX = posX

    def getPosY(self):
        return self.__posY

    def setPosY(self,posY):
        self.__posY = posY

    def getAtTime(self):
        return self.__atTime

    def setAtTime(self, atTime):
        self.__atTime = atTime