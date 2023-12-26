# pcpp1 practice: abstract classes lab
# abstract classes, abstract methods, multiple inheritance

import abc

class Scanner(abc.ABC):
    def scan_document(self):
        return f'The document has been scanned'

    @abc.abstractmethod
    def get_scanner_status(self):
        pass


class Printer(abc.ABC):
    def print_document(self):
        return 'The document has been printed'

    @abc.abstractmethod
    def get_printer_status(self):
        pass


class MFD1(Scanner, Printer):
    serial_no = '001'
    def get_scanner_status(self):
        return f'Max Resolution: 480p. The serial number is S{MFD1.serial_no}'
    
    def get_printer_status(self):
        return f'Max Resolution: 480p. The serial number is P{MFD1.serial_no}'

class MFD2(Scanner, Printer):
    serial_no = '002'
    def get_scanner_status(self):
        return f'Max Resolution: 720p. The serial number is S{MFD2.serial_no}'
    
    def get_printer_status(self):
        return f'Max Resolution: 720p. The serial number is P{MFD2.serial_no}'

    def operation_history(self):
        return 'Displaying history'

class MFD3(Scanner, Printer):
    serial_no = '003'
    def get_scanner_status(self):
        return f'Max Resolution: 1080p. The serial number is S{MFD3.serial_no}'
    
    def get_printer_status(self):
        return f'Max Resolution: 1080p. The serial number is P{MFD3.serial_no}'
    
    def operation_history(self):
        return 'Displaying history'
    
    def fax(self):
        return 'Sending fax'
    

# testing
mfd1 = MFD1()
mfd2 = MFD2()
mfd3 = MFD3()

print(mfd1.print_document())
print(mfd2.scan_document())
print(mfd1.get_printer_status())
print(mfd2.get_scanner_status())
print(mfd3.get_printer_status())
print(mfd2.operation_history())
print(mfd3.fax())