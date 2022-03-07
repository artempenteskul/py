a_counter = 2
b_counter = 3
c_counter = 4

pi_number = 3

for i in range(1, 16):
    if i % 2 == 0:
        pi_number -= 4 / (a_counter * b_counter * c_counter)
    else:
        pi_number += 4 / (a_counter * b_counter * c_counter)
    print(f'Pi number {i} - {pi_number}')
    a_counter += 1
    b_counter += 1
    c_counter += 1
