from datetime import datetime


DATETIME = datetime(2023, 2, 8, 11, 19, 45, 745177)

if __name__ == '__main__':
    timestamp = datetime.timestamp(DATETIME)
    print(timestamp)
