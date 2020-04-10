"""This is not preferred, because even though the instance is the same, the init method is being called every time"""


class Database:
    initialized = False

    def __init__(self):
        print('database init')

    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Database, cls)\
                .__new__(cls, *args, **kwargs)

        return cls._instance


database = Database()

if __name__ == '__main__':
    d1 = Database()
    d2 = Database()
    print(d1 == d2)
    print(database == d1)