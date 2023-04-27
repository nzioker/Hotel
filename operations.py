import random


class Rooms:
    def __init__(self):
        self.rooms = {"Presidential": 25, "Platinum": 30, "Gold": 50, "Ivory": 50}
        self.cost = {"Presidential": 2000, "Platinum": 1200, "Gold": 800, "Ivory": 400}
        self.total_available_rooms = (
            self.rooms["Presidential"]
            + self.rooms["Platinum"]
            + self.rooms["Gold"]
            + self.rooms["Ivory"]
        )
        self.booked_rooms = []

    def available_rooms(self):
        print(self.total_available_rooms)

    def generate_room_numbers(self, tier):
        if tier == "Presidential":
            room = random.randint(1, 25)
            if room in self.booked_rooms:
                new_room = random.randint(1, 25)
                return new_room
            return room

        if tier == "Platinum":
            room = random.randint(26, 55)
            if room in self.booked_rooms:
                new_room = random.randint(26, 55)
                return new_room
            return room

        if tier == "Gold":
            room = random.randint(56, 105)
            if room in self.booked_rooms:
                new_room = random.randint(56, 105)
                return new_room
            return room

        if tier == "Ivory":
            room = random.randint(106, 155)
            if room in self.booked_rooms:
                new_room = random.randint(106, 155)
                return new_room
            return room

    def all_booked_rooms(self):
        return self.booked_rooms

    @staticmethod
    def process_receipt(status):
        name = input("What is your name? ")
        phone_number = input("Enter your phone number ")
        print(f"Name: {name}")
        print(f"Phone Number: {phone_number}")
        print(f"Status: {status}")
        print("Thank you for Choosing Red Rock Hotels. Enjoy your stay")

    def process_payments(self, payment, user_input):
        if payment == self.total_cost:
            self.rooms[user_input] -= self.number_of_rooms
            status = "booked"
            self.process_receipt(status)
            print(f"Proceed to room {self.room_number}. Here are your keys ")

        if payment < self.total_cost:
            new_selection = input(
                f"Unfortunately, Your payment is insufficient. Select one of these other tiers {self.remaining_tiers}"
            )
            self.book_a_room(new_selection)

    def book_a_room(self, user_input):
        # check availability of that tier
        self.remaining_tiers = list(self.rooms.keys())
        self.remaining_tiers.remove(user_input)
        if self.rooms[user_input] > 0:
            self.number_of_rooms = int(
                input(f"How many rooms do you want to pay for? ")
            )

            if self.number_of_rooms < self.rooms[user_input]:
                number_of_nights = int(
                    input(
                        f"Room is available. How many nights do you want to pay for? It costs USD {self.cost[user_input]} per night. "
                    )
                )
                self.total_cost = (
                    number_of_nights * self.cost[user_input] * self.number_of_rooms
                )
                payment = int(input(f"Kindly make payment of USD {self.total_cost} "))
                self.room_number = self.generate_room_numbers(user_input)
                self.booked_rooms.append(self.room_number)
                self.process_payments(payment, user_input)
            else:
                new_selection = input(
                    f"We're sorry. The cannot book this number of rooms for this tier. Select one of these other tiers {self.remaining_tiers}"
                )
        else:
            new_selection = input(
                f"Unfortunately, all our rooms for that tier are booked. Select one of these other tiers {self.remaining_tiers}"
            )
            self.book_a_room(new_selection)
