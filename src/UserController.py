import pickle

USERS_PATH = "users.bin"


def encrypt(line: str):
    crypto = []
    for char in line:
        crypto.append(ord(char) ^ 0b11111111)
    return crypto


def decrypt(line: list):
    crypto = ""
    for char in line:
        crypto += chr(char ^ 0b11111111)
    return crypto


def load_users(users):
    try:
        with open(USERS_PATH, "rb") as file:
            encrypt_users = pickle.load(file)
        users = []
        for encrypt_user in encrypt_users:
            users.append(
                {
                    "name": decrypt(encrypt_user["name"]),
                    "password": decrypt(encrypt_user["password"]),
                    "traders": [
                        {"name": decrypt(encrypt_trader["name"]), "password": decrypt(encrypt_trader["password"])}
                        for encrypt_trader in encrypt_user["traders"]
                    ],
                }
            )
        return users
    except FileNotFoundError:
        save_users(users)
    except Exception as err:
        print(f"Exception on loading users from path = {USERS_PATH}. {err}")


def save_users(users):
    try:
        encrypt_users = []
        for user in users:
            encrypt_users.append(
                {
                    "name": encrypt(user["name"]),
                    "password": encrypt(user["password"]),
                    "traders": [
                        {"name": encrypt(trader["name"]), "password": encrypt(trader["password"])}
                        for trader in user["traders"]
                    ],
                }
            )
        with open(USERS_PATH, "wb") as file:
            pickle.dump(encrypt_users, file)
    except Exception as err:
        print(f"Exception on saving users to path = {USERS_PATH}. {err}")
