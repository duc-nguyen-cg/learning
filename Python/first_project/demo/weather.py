class Weather: 
    def __init__(self, month=None, temp=None, precipitation=None):
        self.__month = month
        self.__temp = temp
        self.__precipitation = precipitation

    def __str__(self) -> str:
        name = "Weather: month = {}, temperature = {}, precipitation = {}"
        return (name.format(self.__month, self.__temp, self.__precipitation))

    def getMonth(self):
        return self.__month

    def getTemp(self):
        return self.__temp

    def getPrecipitation(self):
        return self.__precipitation

    def setMonth(self, month):
        self.__month = month

    def setTemp(self, temp):
        self.__temp = temp

    def setPrecipitation(self, prep):
        self.__precipitation = prep


