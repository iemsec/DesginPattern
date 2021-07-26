import string
import random

class VehicleInfo:
    brand: str
    catalogue_price: int
    electric: bool    

    def __init__(self, brand, electric, catalogue_price) -> None:
        self.brand = brand
        self.catalogue_price = catalogue_price
        self.electric = electric

    def compute_tax(self):
        tax_percentage = 0.05
        if self.electric:
            tax_percentage = 0.02
        return tax_percentage * self.catalogue_price

    def print(self):
        print(f"Brand: {self.brand}")
        print(f"Payable tax: {self.compute_tax()}")

class Vehicle:
    id: str
    license_plate: str
    info: VehicleInfo

    def __init__(self, id, license_plate, info) -> None:
        self.id = id
        self.license_plate = license_plate
        self.info = info

    def print(self):
        print("Registration Complete. Vehicle information:")
        print(f"Id: {self.id}")
        print(f"Licence plate: {self.license_plate}")
        self.info.print()

class VehicleRegistry:

    vehicle_info = { }

    def __init__(self) -> None:
        self.add_vehicle_info("Tesla Model 3", True, 60000)
        self.add_vehicle_info("VW ID3", True, 35000)
        self.add_vehicle_info("BMW 5", False, 45000)

    def add_vehicle_info(self, brand, electric, catalogue_price):
        self.vehicle_info[brand] = VehicleInfo(brand, electric, catalogue_price)

    def generate_vehicle_id(self, length):
        return ''.join(random.choices(string.ascii_uppercase, k=length))

    def generate_vehicle_license(self, id):
        return f"{id[:2]}-{''.join(random.choices(string.digits, k=2))}-{''.join(random.choices(string.ascii_uppercase, k=2))}"

    def create_vehicle(self,brand):

        # generate a vehicle id of length 12
        vehicle_id = self.generate_vehicle_id(12)

        # now generate a license plate for the vehicle
        # using the first two characters of the vehicle id
        license_plate = self.generate_vehicle_license(vehicle_id)
        return Vehicle(vehicle_id, license_plate, self.vehicle_info[brand])



class Application:

    def register_vehicle(self, brand: string):
        # create a registry instance
        registry = VehicleRegistry()

        # Create the vehicle
        vehicle = registry.create_vehicle(brand)

        vehicle.print()

app = Application()
vehicle = app.register_vehicle("BMW 5")