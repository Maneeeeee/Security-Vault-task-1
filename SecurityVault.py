import random
import time
import string

count = 0

def generate_password(length):
    symbols = list("!$%&()*+-=/?@")
    upper_case = list(string.ascii_uppercase)
    lower_case = list(string.ascii_lowercase)
    numbers = list("0123456789")
    password = random.choice(symbols) + random.choice(upper_case) + random.choice(lower_case) + random.choice(numbers)
    for i in range(length - 4):
        password = password + random.choice(symbols + lower_case + upper_case + numbers + numbers)
    password = list(password)
    random.shuffle(password)
    password = "".join(password)
    return password

def write_in_file(length, n):
    with open("generatedPassword.txt", "w") as file:
        while n > 0:
            file.write(generate_password(length) + "\n")
            n -= 1
        return


def is_common(password, file_path):
    with open(file_path, "r") as file:
        for line in file:
            if password == line:
                return True
    return False


def delete_file_content(file_path):
    with open(file_path, "w") as file:
        file.seek(0)
        file.write("")

start_time = time.perf_counter()
with open("generatedPassword.txt", "r") as file:
    for password in file:
        if  is_common(password, "commonPassword.txt"):
            print(f"Password was found, it takes tries ")
            break
        else:
            print(f"Password was not found ")
time = time.perf_counter() - start_time
print(f"It takes {time} seconds")
# delete_file_content("generatedPassword.txt")
