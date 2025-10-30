# Secret validation module (keep private)
def check_flag(user_flag: str) -> bool:
    correct_flag = "flag{shifted_message}"  # hidden here
    return user_flag == correct_flag
