from demo.exception.InvalidIndexException import InvalidIndexException
from demo.exception.InvalidWeatherException import InvalidWeatherException
from .weather import Weather

class WeatherFactory:
    __weather = []

    __instance = None

    def __init__(self):
        raise RuntimeError("Call getInstance() instead")

    @classmethod
    def __dummydata(cls):
        cls.__weather.append(Weather(10, 23.5, 85.0))
        cls.__weather.append(Weather(1, 17.2, 73.0))
        cls.__weather.append(Weather(7, 32.9, 90.2))

    @classmethod
    def getInstance(cls):
        if (cls.__instance is None):
            cls.__instance = cls.__new__(cls)
        cls.__dummydata()
        return cls.__instance    


    def getAll(self):
        return self.__weather[:]

    def find(self, index):
        if (isinstance(index, int) and (index >= 0 and index < len(self.__weather))):
            return self.__weather[index]
        else:
            raise InvalidIndexException(index) 


    def add(self, newWeather):
        if (isinstance(newWeather, Weather)):
            self.__weather.append(newWeather)
        else :
            raise InvalidIndexException(newWeather)


    def edit(self, index, editWeather):
        if (isinstance(index, int) and (index >= 0 and index < len(self.__weather))):
            if (isinstance(editWeather, Weather)):
                self.__weather[index] = editWeather
            else :
                raise InvalidWeatherException(editWeather)  
        else :
            raise InvalidIndexException(index) 


    def removeByIndex(self, index):
        if (isinstance(index, int) and (index >= 0 and index < len(self.__weather))):
            del self.__weather[index]
        else:
            raise InvalidIndexException(index)



    def clear(self):
        self.__weather.clear()