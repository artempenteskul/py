from random import randrange

coin_value_list = []

for i in range(10):
    while True:
        coin_value = randrange(0, 2)
        print(0, end=' ') if coin_value == 0 else print(1, end=' ')
        coin_value_list.append(coin_value)
        if len(coin_value_list) < 3:
            pass
        else:
            if coin_value == coin_value_list[-2] == coin_value_list[-3]:
                print(f'(attempts: {len(coin_value_list)})')
                coin_value_list = []
                break
