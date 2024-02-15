import random
import sys
import time

file_path = "commonPassword.txt"
gen_file_path = "generatedPassword․txt"
count = 0

def generate_password(length):
    chars = list("!$%&()*+-=/?@abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
    password = ""
    for i in range(length):
        password = password + random.choice(chars)
    with open("generatedPassword․txt", "a") as file:
        file.write(password + "\n")
    return


'''
def timer(function):
    def wrapper(*args,**kwargs):
        start_time = time.perf_counter()
        result = function(*args,**kwargs)
        end_time = time.perf_counter() - start_time
        print(f"It takes {end_time} seconds")
        return result
    return wrapper
'''

#@timer
def is_common(password, file_path):
    start_time = time.perf_counter()
    count = 0
    with open (gen_file_path, "r") as file1, open(file_path, "r") as file2:
        for line1 in file1:
            for line2 in file2:
                if line1 == line2:
                    count += 1
                    end_time = time.perf_counter() - start_time
                    print(f"It takes {end_time} seconds")
                    return True
    end_time = time.perf_counter() - start_time
    print(f"It takes {end_time} seconds")
    return False


def delete_file_content(file):
    with open(file, "w"):
        file.write("")

for i in range(30):
    generate_password(random.randint(12,16))

for i in range(30):
    with open(gen_file_path, "r") as file:
        for password in file:
            if is_common(password, file_path):
                print(f"Password was found, it takes {count} tries ")
                delete_file_content(gen_file_path)
                sys.exit()
            else:
                print(f"Password was not found ")
delete_file_content(gen_file_path)

