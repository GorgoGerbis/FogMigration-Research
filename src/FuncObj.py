from enum import Enum
import random


class enumproperty(object):

    def __init__(self, fget):
        self.fget = fget

    def __get__(self, instance, ownerclass=None):
        if ownerclass is None:
            ownerclass = instance.__class__
        return self.fget(ownerclass)

    def __set__(self, instance, value):
        raise AttributeError("can't set pseudo-member %r" % self.name)

    def __delete__(self, instance):
        raise AttributeError("can't delete pseudo-member %r" % self.name)


class FuncObj(Enum):
    """
    Enum functions [x, y, z]
    x = CPU usage
    y = RAM usage
    z = Bandwidth taken
    """
    F1 = [1, 1, 1]
    F2 = [2, 2, 2]
    F3 = [3, 3, 3]
    F4 = [4, 4, 4]
    F5 = [5, 5, 5]
    F6 = [6, 6, 6]

    @enumproperty
    def RANDOM(cls):
        return random.choice(list(cls.__members__.values()))

    #######################################################################

    @staticmethod
    def retrieve_function_value(c):
        if c == 'F1' or c == "F1":
            return FuncObj.F1
        elif c == 'F2' or c == "F2":
            return FuncObj.F2
        elif c == 'F3' or c == "F3":
            return FuncObj.F3
        elif c == 'F4' or c == "F4":
            return FuncObj.F4
        elif c == 'F5' or c == "F5":
            return FuncObj.F5
        elif c == 'F6' or c == "F6":
            return FuncObj.F6
        else:
            raise AttributeError("Function {} does not exist!".format(c))

    def __str__(self):
        return "Function {} | CPU Usage: {} | RAM Usage: {} | BW Usage: {}".format(self.name, self.value[0], self.value[1], self.value[2])

    #######################################################################
