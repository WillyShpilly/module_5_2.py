class House:
    def __init__(self, name, number_of_floor):
        self.name = name
        self.number_of_floor = number_of_floor

    def __str__(self):
        return (f'Название: {self.name}, кол-во этажей: {self.number_of_floor}')
    def __len__(self):
        return self.number_of_floor


n1 = House('ЖК Эльбрус', 10)
n2 = House('ЖК Акация', 20)
print(n1)
print(n2)
print(len(n1))
print(len(n2))