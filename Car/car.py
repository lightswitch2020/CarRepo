from Car.Exeptions import CarTurnedOffError , MaxvelocityError , MinVelocityError

class Car:
    def __init__(self):
        self.__MAXvelocity = 100
        self.__MINVELOCITY = 0
        self.__currentVelocity = 0
        self.__model = ""
        self.__lights = False
        self.__direction = 0
        self.__fuel = 0
        self.__on = False
    def increaseVelocity(self):
        if self.__on == False:
            raise CarTurnedOffError("car is turned off")
        else:
            if self.__currentVelocity + 5 > self.__MAXvelocity:
                raise MaxvelocityError("max velocity limit")
            else:
                self.__currentVelocity += 5
    def decreaseVelociy(self):
        if self.__on == False:
            raise CarTurnedOffError("car is turned off")
        elif self.__currentVelocity - 5 < 0:
            raise MinVelocityError("min velocity error")
        else:
            self.__currentVelocity -= 5
    def setCurrentVelocity(self , velocity):
        if velocity > self.__MAXvelocity:
            raise MaxvelocityError("max velocity limit")
        elif velocity < self.__MINVELOCITY:
            raise MinVelocityError("min velocity limit")
        else:
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
    def turnOff(self):
        self.__on = False
    def getModel(self):
        return self.__model
    def setDirection(self , direction):
        self.__direction = direction

