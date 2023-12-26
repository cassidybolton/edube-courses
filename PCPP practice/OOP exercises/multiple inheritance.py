# pcpp1 practice: multiple inheritance lab
# multiple inheritance

class Scanner():
    def scan(self):
        print('scan() method from the Scanner class')


class Printer():
    def print(self):
        print('print() method from the Printer class')


class Fax():
    def send(self):
        print('send() method from the Fax class')

    def print(self):
        print('print() method from the Fax class')


class MFD_SPF(Scanner, Printer, Fax):
    def __init__(self):
        super().__init__()


class MFD_SFP(Scanner, Fax, Printer):
    def __init__(self):
        super().__init__()


mfd1 = MFD_SPF()
mfd2 = MFD_SFP()

# testing
mfd1.scan()
mfd1.print()
mfd1.send()

mfd2.scan()
mfd2.print()
mfd2.send()