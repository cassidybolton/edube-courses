# pcpp1 practice: inheritance vs composition
# inheritance, composition

class Tires():
    def __init__(self, size):
        self.size = size

    def get_pressure(self):
        return 'Getting tire pressure...'

    def pump(self):
        return 'Pumping tires...'


class Engine():
    def __init__(self, type):
        self.fuel_type = type
        self.status = 'off'

    def start(self):
        if self.status == 'on':
            return 'Car is already started'
        else:
            self.status = 'on'
            return 'Starting car...'

    def stop(self):
        if self.status == 'off':
            return 'Car is already stopped'
        else:
            self.status == 'off'
            return 'Stopping car...'

    def get_state(self):
        return self.status


class Vehicle():
    def __init__(self, VIN, engine, tires):
        self.VIN = VIN
        self.engine = engine
        self.tires = tires

city_tires = Tires(15)
off_road_tires = Tires(18)

electric_engine = Engine('electric')
petrol_engine = Engine('petrol')

car1 = Vehicle(123, electric_engine, city_tires)
car2 = Vehicle(456, petrol_engine, off_road_tires)

print(car1.engine.get_state())
print(car1.VIN)
print(car1.engine.start())
print(car1.tires.get_pressure())
print(car2.VIN)
print(car2.tires.size)
print(car2.tires.pump())
print(car2.engine.stop())