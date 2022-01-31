def eratosthenes_algo(limit: int):
    nums = list(range(0, limit + 1))
    nums[1] = 0

    p = 2

    while p < limit:
        for i in range(p * 2, limit + 1, p):
            nums[i] = 0
        p += 1

    prime_nums = [x for x in nums if x != 0]

    return prime_nums


if __name__ == '__main__':
    limit = int(input('Enter the limit for the prime nums: '))
    print(f'List for prime nums with {limit} limit: {eratosthenes_algo(limit=limit)}')
