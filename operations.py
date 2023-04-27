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

    def room_number(self, x,y):
        room = random.randint(x, y)
        if room in self.booked_rooms:
            new_room = random.randint(x,y)
            return new_room
        return room
    
    def take_input(self, prompt):
        u = input(prompt)
        return u


    def generate_room_numbers(self, tier):
        if tier == "Presidential":
            return self.room_number(1,25)

        if tier == "Platinum":
            return self.room_number(26,55)

        if tier == "Gold":
            return self.room_number(56,105)

        if tier == "Ivory":
            return self.room_number(106,155)

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
            new_selection = self.take_input(f"Unfortunately, Your payment is insufficient. Select one of these other tiers {self.remaining_tiers}")
            self.book_a_room(new_selection)

    def select_number_of_nights(self, user_input):
        try:
            number_of_nights = int( self.take_input(f"Room is available. How many nights do you want to pay for? It costs USD {self.cost[user_input]} per night. "))
            self.total_cost = (number_of_nights * self.cost[user_input] * self.number_of_rooms)
            payment = int(self.take_input(f"Kindly make payment of USD {self.total_cost} "))
            self.room_number = self.generate_room_numbers(user_input)
            self.booked_rooms.append(self.room_number)
            self.process_payments(payment, user_input)
        except ValueError:
            print("Pass in numbers instead of letters or symbols")
            self.select_number_of_nights(user_input)

    def book_a_room(self, user_input):
        self.remaining_tiers = list(self.rooms.keys())
        self.remaining_tiers.remove(user_input)
        if self.rooms[user_input] > 0:
            try:
                self.number_of_rooms = int(self.take_input("How many rooms do you want to pay for? "))
                if self.number_of_rooms < self.rooms[user_input]:
                    self.select_number_of_nights(user_input)
                else:
                    new_selection = self.take_input(f"We're sorry. The cannot book this number of rooms for this tier. Select one of these other tiers {self.remaining_tiers}")
            except ValueError:
                print("Only numbers are accepted.")
                self.book_a_room(user_input)
        else:
            new_selection = self.take_input(f"Unfortunately, all our rooms for that tier are booked. Select one of these other tiers {self.remaining_tiers}")
            self.book_a_room(new_selection)
