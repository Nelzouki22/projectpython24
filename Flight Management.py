class Passenger:
    def __init__(self, name, age, seat_number):
        self.name = name
        self.age = age
        self.seat_number = seat_number

class Flight:
    def __init__(self, flight_number, capacity):
        self.flight_number = flight_number
        self.capacity = capacity
        self.passengers = []

    def add_passenger(self, passenger):
        if len(self.passengers) < self.capacity:
            self.passengers.append(passenger)
            print(f"Passenger {passenger.name} added to flight {self.flight_number}")
        else:
            print("Flight is at full capacity. Cannot add passenger.")

    def list_passengers(self):
        print(f"Passengers on flight {self.flight_number}:")
        for passenger in self.passengers:
            print(f"Seat {passenger.seat_number}: {passenger.name}, {passenger.age} years old")

def main():
    flight = Flight("ABC123", 50)

    passenger1 = Passenger("Alice", 30, "A1")
    passenger2 = Passenger("Bob", 25, "B3")
    passenger3 = Passenger("Charlie", 40, "C2")

    flight.add_passenger(passenger1)
    flight.add_passenger(passenger2)
    flight.add_passenger(passenger3)

    flight.list_passengers()

if __name__ == "__main__":
    main()
