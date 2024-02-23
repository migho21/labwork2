'''
 Program purpose: To designing a hotel reservation system where guests can book rooms online.
 Developer: Muhammad Amirul Aiman Bin Muhamad Azani
 Date: 23 February 2024
'''

print("\nWelcome to DiNara Hotel Reservation System\n")

# Display Room Types
print("DiNara Hotel Room Types:")
print("1. Single: RM100 per night")
print("2. Double: RM150 per night")
print("3. Suite: RM250 per night\n")

# Get user inputs
typeroom = int(input("Enter your room (Choose number): "))
pernight = int(input("Enter your per night: "))
numroom = int(input("Enter your number of room: "))

# Define room prices
single_room = 100
double_room = 150
suite_room = 250

# Error handling for invalid inputs
if typeroom not in [1, 2, 3] or pernight <= 0 or numroom <= 0:
    print("Error: No room selected. Please try again from room (1-3).")
else:
    # Calculate total price
    if typeroom == 1:  # Single Room
        total = single_room * pernight * numroom
        print(f"\nTotal price (RM): {total:.2f}")
        if pernight > 7:
            print("Awesome! You get a free breakfast voucher.")
    elif typeroom == 2:  # Double Room
        total = double_room * pernight * numroom
        print(f"\nTotal price (RM): {total:.2f}")
    elif typeroom == 3:  # Suite Room
        total = suite_room * pernight * numroom
        print(f"\nTotal price (RM): {total:.2f}")
        if pernight < 3:
            print("Minimum just 3 nights only for Suite Room.")

    # Check for discount
    if numroom > 5:
        total_discount = total * 0.1
        print(f"Discount: RM{total_discount:.2f}")

    # Display reservation info
    print("\nYour Reservation Info:")
    print(f"Room Type: {typeroom}")
    print(f"Per Night: {pernight}")
    print(f"Number of Room: {numroom}")
