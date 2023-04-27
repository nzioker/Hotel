try:
    val = int(input("Enter a number "))
    print(val)
except ValueError as e:
    val = int(input("Make sure your entry is a number "))