# pcpp1 practice: shallow and deep copy #2
# creating classes, copy module and its methods

import copy

# part 2 work
class Delicacy():
    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight

    def __str__(self):
        return f'name: {self.name}, price: {self.price}, weight: {self.weight}'


warehouse = []
warehouse.append(Delicacy('Lolly Pop', 0.4, 133))
warehouse.append(Delicacy('Licorice', 0.1, 251))
warehouse.append(Delicacy('Chocolate', 1, 601))
warehouse.append(Delicacy('Sours', 0.01, 513))
warehouse.append(Delicacy('Hard candies', 0.3, 433))

print('Source list of candies:')
for item in warehouse:
    print(item)

print('*' * 20)
print('Price proposal:')

deepcopied_warehouse = copy.deepcopy(warehouse)
for item in deepcopied_warehouse:
    if item.weight > 300:
        item.price *= 0.8
    print(item)

print('*' * 20)

shallowcopied_warehouse = copy.copy(warehouse)
for item in shallowcopied_warehouse:
    if item.weight > 300:
        item.price *= 0.8
    print(item)