# pcpp1 practice: advanced exceptions
# exception chaining, implicit and explicit exceptions

class RocketNotReadyError(Exception):
    pass


def personnel_check():
    try:
        print(f"The captain's name is {crew[0]}")
        print(f"The pilot's name is {crew[1]}")
        print(f"The mechanic's name is {crew[2]}")
        print(f"The navigator's name is {crew[3]}")
    except IndexError as e:
        raise RocketNotReadyError('One or more crew members are missing') from e
    

def fuel_check():
    if fuel == 100:
        print('Fuel tank is full')
    elif fuel < 100:
        raise RocketNotReadyError('Need to fill up fuel tank')
    else:
        raise RocketNotReadyError('Other fuel issue')

def batteries_check():
    if batteries == 'charged':
        print('Batteries are fully charged')
    else:
        raise RocketNotReadyError('Batteries are not charged')

def circuits_check():
    try:
        1/circuits
        print(f'Circuits are connected properly')
    except ZeroDivisionError as e:
        raise RocketNotReadyError('Circuits are not connected properly') from e

crew = ['Kelli', 'Cassidy', 'Taylor']
fuel = 100
batteries = 'charged'
circuits = 0
check_list = [personnel_check, fuel_check, batteries_check, circuits_check]

print('Final check procedure...')

for check in check_list:
    try:
        check()
    except RocketNotReadyError as e:
        print(f'ROCKET NOT READY. Error: {e}, caused by {e.__cause__}')