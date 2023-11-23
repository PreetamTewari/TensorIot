# TensorIoT Assignment

Create a parking lot class that takes in a square footage size as input and creates an array of empty values based on the input square footage size. Assume every parking spot is 8x12 (96 ft2) for this program, but have the algorithm that calculates the array size be able to account for different parking spot sizes. For example, a parking lot of size 2000ft2 can fit 20 cars, but if the parking spots were 10x12 (120 ft2), it could only fit 16 cars. The size of the array will determine how many cars can fit in the parking lot.

Create a car class that takes in a 7 digit license plate and sets it as a property. The car will have 2 methods:

1.        A magic method to output the license plate when converting the class instance to a string.

2.        A "park" method that will take a parking lot and spot # as input and fill in the selected spot in the parking lot. If another car is parked in that spot, return a status indicating the car was not parked successfully. If no car is parked in that spot, return a status indicating the car was successfully parked.

Have a main method take an array of cars with random license plates and have them park in a random spot in the parking lot array until the input array is empty or the parking lot is full. If a car tries to park in an occupied spot, have it try to park in a different spot instead until it successfully parks. Once the parking lot is full, exit the program.

Output when a car does or does not park successfully to the terminal (Ex. "Car with license plate [LICENSE_PLATE] parked successfully in spot [SPOT #]").

OPTIONAL/BONUS - Create a method for the parking lot class that maps vehicles to parked spots in a JSON object. Call this method at the end of the program, save the object to a file, and upload the file to an input S3 bucket.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Thanks](#thanks)

## Installation

I am using random, json and boto3 modules. Please install using pip/pip3 command if not available 

## How it Works
There are two classes ParkingLot and Car. In the ParkingLot class, a parking lot square footage is passed. This class has four methods *get_available_spaces*, *get_best_fit*, *park* and *get_cars_parked*.

1. **get_available_spaces**
This method computes the total available parking spots.

2. **get_best_fit**
This method takes a array of widths and a constant length and finds the best width and length to minimize wastage of the parking space.

3. **park**
This method first checks for any invalid input and then parks the car in the valid assigned parking spot. If successfull, returns a success message otherwise, return a unsuccessfull message.

4. **get_cars_parked**
This method returns a dictionary of car licenses mapped to the parking spot number.

In the Car class, a license plate number is passed. This class has one method.

1. **park**
This method takes in a ParkingLot object and calls the park method in the ParkingLot class.

2. **__str__**
This is a method override for converting the class instance to a string.

### Main Method
It takes an input from the user to enter the parking lot square footage and then creates a ParkingLot object. Using the *generate_license* function, an array of Car objects are created. If there are cars available and parking spots available, the car is taken off from the array of cars and then parked in the designated parking spot. Finally a json file of the car to spot mapping in created and uploaded to AWS S3 bucket. Can be found [here](https://tpreetam-tensoriot.s3.ap-south-1.amazonaws.com/parking_lot.json?response-content-disposition=inline&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCmFwLXNvdXRoLTEiRzBFAiEAuJ1eV9qAMzNm97W1isrdFq1kmA39HidZ3TpXGvdeKlUCIGeq3PnBRzFcgxTkpwJnsLKMUMYnv6DMktyPh2x4zX9kKuQCCEsQBRoMMjA3NTU1NzQ5NzY3IgzBwGEjdvUnXb%2Fn6WIqwQKe6lbuqO5%2BLjauMJzUZ00ezKrywDwIYmxAZ8s%2BN8g0CdCHJV0zcfA7gW0t2JrxPExSLX%2BKPmhG9a%2BvshlAU0I%2B23dx%2FRH5fHNHZ2CiHVhXB4TjB0eaU3IC88Ow6OU5ah%2Ftw3QwSZwxgD4PhVCjZbi0Zelq7BW2kIGCJUdOhkVUtH2j7v%2F1hv7yVs8OKTm6ZBQI%2B7fhxwM27p%2BygJmUZDiue1xpunF48SdC%2FkUNACiORuqSikZdDqMcASCSRKfrzY%2BRchu%2FnBKbfGfUdVXuKfTuGIg86BIZFiOCKZO0tnNkphZtq03YU2eIO73nvU1VOWzoCi%2BwjzZU1PzV3J1TSwNQPDDOgfH8eYJ4nCHKW%2BoO6ot03Zl%2B21j9xEmnvGz4G%2FR6QRf23CBPbfoXpDJtLNco6AAmYBja4Xt7PSKg2GM%2F5msw3qj%2BqgY6swLDoPnXxYqMiC9DWL%2F%2FmEIm6Vg%2FIHNSRi3Jv4DXZTqD%2F3BFDVhxqQ%2FqhMrQhiBRgg6COK0lmDuniQ1B0GJ1%2BbQLC4qi%2FEJ9zy2Py7fdX3%2Fdxn33bOK0auhEvlyGqbrIUIpCqrnN9jM4wTPAeDIYBjnLK80WbrXQVrmD7MJcYuBT9bTv%2B%2BdZjbDCgQj70yIaUGP996HGwEZly1P0wMKtnwyO7CVJZNb%2Bnmyui4HSJCNfGUwVIvI1Ea8LDq%2FKe8zTyg0dMXTE6RoHlwa3BNXqIjiJe38LSR9jn%2BZnHpZvUWRAw3EVfPNrYrQmmku54dn%2FrjEbmOuSNn85kOdzDslNzp8ifVRWalYa%2Fg1c7tI342VgCIQZjpIsK4xLAHxeCbzJLWL5xJJBT%2FsGxRzdmZdIykhppNWa&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20231123T182146Z&X-Amz-SignedHeaders=host&X-Amz-Expires=43200&X-Amz-Credential=ASIATAU2JM6DSSXF2SIV%2F20231123%2Fap-south-1%2Fs3%2Faws4_request&X-Amz-Signature=15bd1c12a8b4522aa429fa4e1b9dade37c44329cf54a6da00d11a48561776032).

It is only availble for the next 12 hours, please reach back if you want me to regenerate the link.

## Thanks
Thank you for the opportunity.

