class Car:
    def __init__(self ):
        self.__currentVelocity = 0
        self.__model = ""
        self.__lights = False
        self.__direction = 0
        self.__fuel = 0
        self.__on = False
    def increaseVelocity(self):
        self.__currentVelocity += 5
    def decreaseVelociy(self):
        self.__currentVelocity -= 5
    def setCurrentVelocity(self , velocity):
        self.__currentVelocity = velocity
    def getCurrentVelocity(self):
        return self.__currentVelocity
    def setModel(self , model):
        self.__model = model
    def setLights(self , b):
        self.__lights = b
    def brake(self):
        self.__currentVelocity = 0
    def turnOn(self):
        self.__on = True
    def getModel(self):
        return self.__model
    def setModel(self , model):
        self.__model = model

