class Vehicles:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year=year
    def start(self):
        print("Vehicle is starting")
    def stop(self):
        print("Vehicle is stopping")

class Car(Vehicles):
    def __init__(self,make,model,year,number_of_doors,number_of_wheels):
        super().__init__(make,model,year)
        self.number_of_doors=number_of_doors
        self.number_of_wheels=number_of_wheels
    def start(self):
        print("Car is starting")
    def stop(self):
        print("Car is stopping")
class Bike(Vehicles):
    def __init__(self,make,model,year,number_of_wheels,mielage):
        super().__init__(make,model,year)
        self.number_of_wheels=number_of_wheels
        self.mielage=mielage
    def start(self):
        print("Bike is starting")
    def stop(self):
        print("Bike is stopping")
vehicles=[Car("bmw","q4",2010,4,4),
          Bike("bmw","a4",2000,2,19),]
for vehicle in vehicles:
    if isinstance(vehicle,Vehicles):
        print(f"Your {vehicle.make} is made in the {vehicle.year} and it is working fine")
        vehicle.start()
        vehicle.stop()
    else:
        print("Your vehicle is not in the list")




# car1=Car("Audi","Q4",2010,4,4)
# car1.__dict__
# print(car1.__dict__)
# bike1=Bike("Ninja","rrr",2010,2,19)
# bike1.__dict__
# print(bike1.__dict__)