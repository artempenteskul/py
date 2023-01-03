from datetime import datetime


if __name__ == '__main__':
    d = datetime(2023, 1, 3, 12, 19, 45, 745177)
    timestamp = datetime.timestamp(d)
    print(timestamp)
