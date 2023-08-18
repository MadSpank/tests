from tkinter.filedialog import LoadFileDialog
from typing import List


class Car():
    def __init__(self, year, production, model, mileage):
        self.year = year
        self.model = model
        self.mileage = mileage
        self.production = production

    def drive(self, mileage, speed):
        print(f'Car goes for {mileage} with {speed} mph speed')
        self.mileage += mileage


    def brake(self):
        print('Cat got broken')

    def get_mileage(self):
        print(f'Car mileage is {self.mileage}')

    def get_car_info(self, additional_info:List=None):
        print(
            f'{self.__class__.__name__} is {self.production} {self.model} {self.year} production year and {self.mileage} miles were driven {(str(additional_info[0]) + " tons to lift " + str(additional_info[1]) + " tons to pull ") if additional_info else None}')



class Truck(Car):
    def __init__(self, year, production, model, mileage, weight_lifting, weight_pulling, loaded=0, pulling=0):
        Car.__init__(self, year, production, model, mileage)
        self.weight_lifting = weight_lifting
        self.weight_pulling = weight_pulling
        self.loaded = loaded
        self.pulling = pulling

    def get_car_info(self):
        super().get_car_info(additional_info=[self.weight_lifting, self.weight_pulling])
        print(f'Also, the cat lifting {self.loaded} kilograms and pulling {self.pulling} kilograms')

    def load_stuff(self, stuff_weight):
        self.loaded += stuff_weight
        print(f'{stuff_weight} were added to a car bed')

    def add_pullling_weight(self, weight_to_pull):
        self.pulling += weight_to_pull
        print(f'now car pulling {weight_to_pull} more kilograms')




# nissan = Car(1998, 'Nissan', 'Sunny', 100000)
truck = Truck(1960, 'Toyota', 'Zalupa', 150000, 2, 5)

# nissan.drive(20, 80)
# nissan.get_car_info()
truck.load_stuff(500)
truck.add_pullling_weight(100)
truck.get_car_info()


