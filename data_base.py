import sqlite3


def create_table():
    with sqlite3.connect('neighbors.db') as db_connect:
        cursor = db_connect.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS users
                            (id INTEGER PRIMARY KEY,
                            name text,
                            x real,
                            y real)''')
        db_connect.commit()


def add_user_to_db(name, x, y):
    with sqlite3.connect('neighbors.db') as db_connect:
        cursor = db_connect.cursor()
        entities = (name, x, y)
        cursor.execute("INSERT INTO users(name, x, y) VALUES(?, ?, ?)", entities)
        db_connect.commit()


def get_users_from_db(id, count, radius):
    with sqlite3.connect('neighbors.db') as db_connect:
        cursor = db_connect.cursor()
        user_cords = list(cursor.execute(f'SELECT x as x1, y as y1 FROM users where id={id}'))
        x1, y1 = [i for i in user_cords[0]]
        result = cursor.execute(f'''SELECT name, sqrt(ABS(pow({x1}-x, 2)) + ABS(pow({y1}-y, 2))) as hypotenuse
                                    FROM users
                                    WHERE hypotenuse <={radius} and hypotenuse > 0
                                    LIMIT {count}''')
        # db_connect.commit()
        return make_beautiful(result.fetchall())


def make_beautiful(sql_request):
    my_dict = (dict(sql_request))
    for key in my_dict.keys():
        my_dict[key] = round(my_dict[key], 1)
    return my_dict
