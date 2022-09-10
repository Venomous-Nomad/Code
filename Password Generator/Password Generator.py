import random

def generate_pass(length):
    char_list = []
    password = ""
    with open("characters_DB.txt", "r") as file:
        for f in file:
            f = f.strip()
            char_list.append(f)
    for i in range(length):
        password += random.choice(char_list)
    return password

print("|||Password Generator|||")
length = int(input("Length of password: "))
print(generate_pass(length))
