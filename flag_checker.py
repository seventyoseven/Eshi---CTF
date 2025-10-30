try:
    from secret.verify_flag import check_flag
except ImportError:
    print("Error: verification module missing.")
    exit()

result = input("Enter your flag: ").strip()

if check_flag(result):
    print("✅ Correct flag! Well done.")
else:
    print("❌ Incorrect flag. Try again.")
