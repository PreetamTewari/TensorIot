import random
import json
import boto3
class ParkingLot:
    def __init__(self, sq_footage) -> None:
        self.sq_footage = sq_footage
        self.width, self.length = self.get_best_fit()
        # print(self.width, self.length)
        self.available_spaces = self.get_available_spaces()
        self.parking_spaces = [""] * self.available_spaces
        self.parked_cars = {}

    def get_available_spaces(self):
        return self.sq_footage // (self.width * self.length)
    
    def get_best_fit(self):
        available_widths = [8, 10, 12, 14]
        available_length = 12
        best_width = 0
        best_length = 0
        best_fit = float("inf")

        for width in available_widths:
            parking_spots = self.sq_footage // (width * available_length)
            if parking_spots > 0:
                remaining_space = self.sq_footage - (width * available_length * parking_spots)
                if remaining_space < best_fit:
                    best_fit = remaining_space
                    best_width = width
                    best_length = available_length
            
        return [best_width, best_length]
    
    def park(self, license, spotNo):
        if spotNo < 0 or spotNo >= len(self.parking_spaces):
            return "Invalid input for spot number"
        
        if self.parking_spaces[spotNo] != "":
            return f'Spot {spotNo} is already taken. Car with license {license} cannot be parked'
        else:
            self.parking_spaces[spotNo] = license
            self.parked_cars[license] = spotNo
            return f'Car with license plate {license} parked successfully in spot {spotNo}'
    
    def get_cars_parked(self):
        return self.parked_cars
    
class Car:
    def __init__(self, license) -> None:
        self.license = license

    def park(self, parking_lot):
        spotNo = random.randint(0, parking_lot.available_spaces - 1)
        return parking_lot.park(self.license, spotNo)
    
    def __str__(self) -> str:
        return str(self.license)
    
def generate_license():
    state_code = 'KA'
    city_code = random.randint(1, 99)
    category_code = random.choice(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'])
    number_code = random.randint(1000, 9999)

    return f'{state_code} {city_code} {category_code} {number_code}'
    
if __name__ == '__main__':
    parking_sq_footage = int(input("Enter the parking lot square footage: "))
    parking_lot = ParkingLot(parking_sq_footage)
    
    cars = [Car(generate_license()) for _ in range(30)]

    while cars and parking_lot.available_spaces:
        car = cars.pop()
        print(car)
        print(car.park(parking_lot))

    if parking_lot.get_cars_parked():
        json_doc = json.dumps(parking_lot.get_cars_parked())
        with open('parking_lot.json', 'w') as f:
            f.write(json_doc)

        s3 = boto3.client('s3', aws_access_key_id = 'aws_iam_user_access_key', aws_secret_access_key = 'aws_iam_user_secret_key', region_name = 'ap-south-1')
        s3.upload_file('parking_lot.json', 'tpreetam-tensoriot', 'parking_lot.json')