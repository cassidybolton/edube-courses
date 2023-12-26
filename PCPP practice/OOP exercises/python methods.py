# pcpp1 practice: python methods
# static and class methods

class LuxuryWatch():
    __watches_created = 0
    def __init__(self):
        LuxuryWatch.__watches_created += 1

    @classmethod    
    def get_number_of_watches_created(cls):
        return cls.__watches_created
    
    @classmethod
    def engrave(cls, text):
        if LuxuryWatch.check_text(text) is True:
            watch = cls()
            watch.engraving = text
            return watch  
        else:
            raise Exception('Engraving text must be alphanumeric and <= 40 characters')
        
    @staticmethod
    def check_text(text):
        if len(text) <= 40 and text.isalnum():
             return True
        else:
            return False
        

# testing
watch1 = LuxuryWatch()
print('Total watches created: ' + str(LuxuryWatch.get_number_of_watches_created()))
watch2 = LuxuryWatch.engrave('Cassidy')
print('Total watches created: ' + str(LuxuryWatch.get_number_of_watches_created()))
watch3 = LuxuryWatch.engrave('FixedIt')
print('Total watches created: ' + str(LuxuryWatch.get_number_of_watches_created()))
