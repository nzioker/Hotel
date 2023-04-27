import operations

if __name__ == '__main__':
    operations.Rooms().all_booked_rooms()
    user_input = input("Which tier do you want?")
    operations.Rooms().book_a_room(user_input)
