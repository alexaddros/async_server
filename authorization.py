import sqlite3

users = sqlite3.connect("users.db")
cursor = users.cursor()


def create_new(nickname, password_hash):
    names = cursor.execute("""SELECT nickname FROM main""").fetchall()
    if nickname not in [name[0] for name in names]:
        cursor.execute(f"""INSERT INTO main VALUES('{nickname}', '{password_hash}')""")
        users.commit()
        return True
    else:
        return False


def get_nicknames():
    return [name[0] for name in cursor.execute("""SELECT nickname FROM main""").fetchall()]


def authorize(nickname, password_hash):
    names_and_hashes = cursor.execute("""SELECT * FROM main""").fetchall()
    for info in names_and_hashes:
        if nickname == info[0]:
            if password_hash == info[1]:
                return True
            else:
                return False

    return False
