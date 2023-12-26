# pcpp1 practice: python core syntax lab #2
# special methods, isinstance() method

def convert_time(num):
        hours = num // 3600
        mins = (num % 3600) // 60
        secs = num % 60
        return TimeInterval(h=hours, m=mins, s=secs)

class TimeInterval():
    def __init__(self, h=0, m=0, s=0):
        self.hours = h
        self.mins = m
        self.secs = s

    def __add__(self, other):
        num1 = self.hours * 3600 + self.mins * 60 + self.secs
        if isinstance(other, TimeInterval):
            num2 = other.hours * 3600 + other.mins * 60 + other.secs
        elif isinstance(other, int):
             num2 = other
        else:
             return 'Number must be a TimeInterval object or an integer'
        end_num = num1 + num2
        return convert_time(end_num)

    def __sub__(self, other):
        num1 = self.hours * 3600 + self.mins * 60 + self.secs
        if isinstance(other, TimeInterval):
            num2 = other.hours * 3600 + other.mins * 60 + other.secs
        elif isinstance(other, int):
             num2 = other
        else:
             return 'Number must be a TimeInterval object or an integer'
        end_num = num1 - num2
        return convert_time(end_num)

    def __mul__(self, other):
        num1 = self.hours * 3600 + self.mins * 60 + self.secs
        if isinstance(other, (int, float, str)):
            num2 = int(other)
        else:
             return 'Number must be in the form of an integer, float, or string'
        end_num = num1 * num2
        return convert_time(end_num)

    def __str__(self):
        return f'{str(self.hours).zfill(2)}:{str(self.mins).zfill(2)}:{str(self.secs).zfill(2)}'

fti = TimeInterval(21, 58, 50)
sti = TimeInterval(1, 45, 22)
tti = TimeInterval(h=21, m=58, s=50)

# testing 
print(tti + 62)
print(tti - 62)