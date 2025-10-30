from secret.verify_flag import check_flag

result = input("Enter your flag: ").strip()

if check_flag(result):
    print("✅ Correct flag! Well done.")
else:
    print("❌ Incorrect flag. Try again.")
