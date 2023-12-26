# pcpp1 practice: python core syntax lab #1

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
        num2 = other.hours * 3600 + other.mins * 60 + other.secs
        end_num = num1 + num2
        return convert_time(end_num)

    def __sub__(self, other):
        num1 = self.hours * 3600 + self.mins * 60 + self.secs
        num2 = other.hours * 3600 + other.mins * 60 + other.secs
        end_num = num1 - num2
        return convert_time(end_num)

    def __mul__(self, other):
        num1 = self.hours * 3600 + self.mins * 60 + self.secs
        num2 = int(other)
        end_num = num1 * num2
        return convert_time(end_num)

    def __str__(self):
        return f'{str(self.hours).zfill(2)}:{str(self.mins).zfill(2)}:{str(self.secs).zfill(2)}'

fti = TimeInterval(21, 58, 50)
sti = TimeInterval(1, 45, 22)

# testing 
print(fti + sti)
print(fti - sti)
print(fti * 2)
print(fti)
print(sti)