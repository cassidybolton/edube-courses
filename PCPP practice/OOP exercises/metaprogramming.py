# pcpp1 practice: metaprogramming
# metaclasses, class variables and methods

from datetime import datetime


def get_instantiation_time(self):
    return self.instantiation_time


class TimeMeta(type):
    instantiation_time = None
    classes_created = []

    def __new__(mcs, name, bases, dict):
        if name not in TimeMeta.classes_created:
            TimeMeta.classes_created.append(name)

        if 'get_instantiation_time' not in dict:
            dict['get_instantiation_time'] = get_instantiation_time
        
        obj = super().__new__(mcs, name, bases, dict)
        obj.instantiation_time = datetime.now()

        return obj

class Pizza(metaclass=TimeMeta):
    def __init__(self, topping):
        self.topping = topping


class Waffle(metaclass=TimeMeta):
    def __init__(self, topping):
        self.topping = topping


pizza1 = Pizza('cheese')
pizza2 = Pizza('pep')
waffle1 = Waffle('butter')
waffle2 = Waffle('syrup')

print(pizza1.get_instantiation_time())
print(waffle2.get_instantiation_time())