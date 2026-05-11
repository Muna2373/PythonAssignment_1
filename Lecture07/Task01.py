class Car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

car1 = Car("ABC-123", 142)

print("Registration number is:", car1.registration_number)
print("Maximum speed is:", car1.maximum_speed)
print("Current speed is :", car1.current_speed)
print("Travelled distance is:", car1.travelled_distance)