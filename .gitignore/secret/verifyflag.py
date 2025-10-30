# Secret validation module (keep private)
def check_flag(user_flag: str) -> bool:
    correct_flag = "FLAG{this_is_the_real_one}"  # hidden here
    return user_flag == correct_flag
