import sys
from typing import ClassVar
from demo.checker.InputChecker import InputChecker
from demo.exception.InvalidIndexException import InvalidIndexException

from demo.weather import Weather

from .weather_factory import WeatherFactory

class WeatherController:

    show_all_btn = 1
    add_btn = 2
    edit_btn = 3
    remove_btn = 4
    clear_btn = 5
    exit_btn = 0

    __weatherFactory = WeatherFactory.getInstance()

    __instance = None

    def __init__(self):
        raise RuntimeError("Call getInstance() instead")

    @classmethod
    def getInstance(cls):
        if (cls.__instance is None):
            cls.__instance = cls.__new__(cls)
        return cls.__instance   


    def run(self):
        choice = None
        flag = True
        while ((choice is not None) or flag):
            flag = False

            choice = InputChecker.checkInt("""
                Choose an action:
                1. Show all
                2. Add
                3. Edit 
                4. Delete
                5. Clear
                0. Exit
                Enter a number: """, max = 5, min = 0)

            if (choice == self.show_all_btn):
                self.__showAll()
            elif (choice == self.add_btn):
                self.__add()
            elif (choice == self.edit_btn):
                self.__edit()
            elif (choice == self.remove_btn):
                self.__remove()
            elif (choice == self.clear_btn):
                self.__clear()
            elif (choice == self.exit_btn):
                sys.exit("System closed!")

    
    def __showAll(self):
        list = self.__weatherFactory.getAll()
        print()
        if (len(list)> 0):
            for item in list:
                print(item)
        else:
            print(list)        


    def __add(self):
        newWeather = Weather()
        month = InputChecker.checkInt("Enter month: ",1,12)
        newWeather.setMonth(month)

        temp = InputChecker.checkFloat("Enter temperature: ")
        newWeather.setTemp(temp)

        prep = InputChecker.checkFloat("Enter precipitation: ")
        newWeather.setPrecipitation(prep)

        self.__weatherFactory.add(newWeather)
        self.__showAll()


    def __edit(self):
        editIndex = InputChecker.checkInt("Enter position of element needs to edit: ",min = 0, max = len(self.__weatherFactory.getAll())-1)

        editWeather = Weather()
        month = InputChecker.checkInt("Enter new month: ", 1, 12)
        editWeather.setMonth(month)

        temp = InputChecker.checkFloat("Enter new temperature: ")
        editWeather.setTemp(temp)

        prep = InputChecker.checkFloat("Enter new precipitation: ")
        editWeather.setPrecipitation(prep)
        
        try:
            self.__weatherFactory.edit(editIndex, editWeather)
            self.__showAll()
        except Exception as e: 
            print(str(e))   
        

    def __remove(self):
        removeIndex = InputChecker.checkInt("Enter position of element needs to remove: ")
        try:
            self.__weatherFactory.removeByIndex(removeIndex)
            self.__showAll()
        except Exception as e:
            print(str(e))


    def __clear(self):
        choice = input("Are you sure (Y/N)? ")
        if (choice == "Y"):
            self.__weatherFactory.clear()
            self.__showAll()
        elif (choice == "N"):
            print("Cancelled!")    
        

