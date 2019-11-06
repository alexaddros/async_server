import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "users.db")

users = sqlite3.connect('C:/Users/skopc/Desktop/media/Lyceum_Yandex/Second_Era/Third Era/users.db')
cursor = users.cursor()

def create_new(nickname, password_hash):
    names = cursor.execute("""SELECT name FROM user""").fetchall()
    if nickname not in [name[0] for name in names]:
        cursor.execute("""INSERT INTO user VALUES(?, ?)""", (nickname, password_hash))
        users.commit()
        return True
    else:
        return False


def get_nicknames():
    return [name[0] for name in cursor.execute("""SELECT nickname FROM user""").fetchall()]


def authorize(nickname, password_hash):
    names_and_hashes = cursor.execute("""SELECT * FROM user""").fetchall()
    for info in names_and_hashes:
        if nickname == info[0]:
            if password_hash == info[1]:
                return True
            else:
                return False

    return False
