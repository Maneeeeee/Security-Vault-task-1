import random
import sys
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
    with open("generatedPassword.txt", "a") as file:
        file.write(password + "\n")
    return


def is_common(password, file_path):
    count = 0
    with open(file_path, "r") as file:
        for line in file:
            count += 1
            if password == line:
                return True
    return False


def delete_file_content(file_path) as file:
    with open(file_path, "w"):
        file.seek(0)
        file.write("")

for i in range(30):
    generate_password(random.randint(12,16))

start_time = time.perf_counter()
for i in range(30):
    with open("generatedPassword.txt", "r") as file:
        for password in file:
            is_common_password = is_common(password, "commonPassword.txt")
            if is_common_password:
                print(f"Password was found, it takes {count} tries ")
                delete_file_content("generatedPassword.txt")
                sys.exit()
            else:
                print(f"Password was not found ")
time = time.perf_counter() - start_time
print(f"It takes {time} seconds")
delete_file_content("generatedPassword.txt")
