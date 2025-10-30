# flag_checker.py

# The correct flag stored secretly
correct_flag = "flag{shifted_message}"

# Take input from the user
result = input("Enter your flag: ").strip()

# Check if it matches
if result == correct_flag:
    print("Correct flag! Well done.")
else:
    print("Incorrect flag. Try again.")
