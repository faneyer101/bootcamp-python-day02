import time
from random import randint
from types import MethodType
import string
import os


def log(function):
    def function_modifed(*args, **kwargs):
        log = open("machine.log", 'a')
        before = time.time()
        user = os.environ["USER"]
        if len(args) == 1:
            ret = function(args[0])
        else:
            ret = function(args[0], args[1])
        name = function.__name__
        name.lower()
        name = name.capitalize()
        for i, c in enumerate(name):
            if c in string.punctuation:
                name = name.replace(c, ' ')
                if len(name) > i:
                    name = name.replace(name[i + 1], name[i + 1].upper())
        after = time.time()
        calcul = after - before
        if (calcul > 1):
            log.write("({})Running: {: <20} [ exec-time = {:.3f} {: <3s}]\n"
                      .format(user, str(name), calcul, "s"))
        else:
            log.write("({})Running: {: <20} [ exec-time = {:.3f} {: <3s}]\n"
                      .format(user, str(name), calcul, "ms"))
        log.close()
        return (ret)
    return function_modifed


class CoffeeMachine():
    water_level = 100

    @log
    def start_machine(self):
        if self.water_level > 20:
            return True
        else:
            print("Please add water!")
            return False

    @log
    def boil_water(self):
        return "boiling..."

    @log
    def make_coffee(self):
        if self.start_machine() is True:
            for _ in range(20):
                time.sleep(0.1)
                self.water_level -= 1
            print(self.boil_water())
            print("Coffee is ready!")

    @log
    def add_water(self, water_level):
        time.sleep(randint(1, 5))
        self.water_level += water_level
        print("Blub blub blub...")


if __name__ == "__main__":
    log_file = open("machine.log", "w")
    log_file.write("")
    log_file.close()
    machine = CoffeeMachine()
    for i in range(0, 5):
        machine.make_coffee()
    machine.make_coffee()
    machine.add_water(70)
