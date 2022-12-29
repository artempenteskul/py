import pickle


PICKLE_FILE = 'people-pickle'


def upload_to_db(pickle_file, db):
    db_file = open(pickle_file, 'wb')
    pickle.dump(db, file=db_file)
    db_file.close()
    print('--- upload to db is finished')
    print()


def get_db_data(pickle_file):
    db_file = open(pickle_file, 'rb')
    db = pickle.load(db_file)
    db_file.close()
    return db


def read_db_data(pickle_file):
    db = get_db_data(pickle_file)
    for key in db:
        print(f'{key} => {db[key]}')
    print()
    print('--- reading data is finished')
    print()


if __name__ == '__main__':
    bob = {'name': 'Bob Smith', 'age': 42, 'pay': 3000, 'job': 'developer'}
    sue = {'name': 'Sue Jones', 'age': 21, 'pay': 2100, 'job': 'manager'}

    database = {'bob': bob, 'sue': sue}

    upload_to_db(PICKLE_FILE, database)
    read_db_data(PICKLE_FILE)

    database = get_db_data(PICKLE_FILE)
    database['tom'] = {'name': 'Tom Tierney', 'age': 32, 'pay': 1000, 'job': 'director'}

    upload_to_db(PICKLE_FILE, database)
    read_db_data(PICKLE_FILE)
