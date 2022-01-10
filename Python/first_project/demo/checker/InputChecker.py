import sys

class InputChecker:
    __ALERT_MESSAGE = """
                Invalid input. Please enter again."""
    
    @classmethod
    def checkInt(cls, message = None, min = None, max = None):
        flag = True
        result = None

        if (min == None):
            min = -sys.maxsize
        if (max == None):
            max = sys.maxsize       

        while (((result is not None) and ((result < min) or (result > max))) or flag):
            flag = False
            try:
                result = int(input(message))
                if ((result < min) or (result > max)):
                    print(cls.__ALERT_MESSAGE)
                else:
                    return result     
            except ValueError:
                flag = True
                print(cls.__ALERT_MESSAGE)

    
    @classmethod
    def checkFloat(cls, message = None, min = None, max = None):
        flag = True
        result = None

        if (min == None):
            min = sys.float_info.min
        if (max == None):
            max = sys.float_info.max      

        while (((result is not None) and ((result < min) or (result > max))) or flag):
            flag = False
            try:
                result = float(input(message))
                if ((result < min) or (result > max)):
                    print(cls.__ALERT_MESSAGE)
                else:
                    return result     
            except ValueError:
                flag = True
                print(cls.__ALERT_MESSAGE)






