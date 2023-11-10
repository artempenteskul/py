import asyncio

from time import time


async def kill_time(num: int) -> None:
    print(f'Running: {num}')
    await asyncio.sleep(1)
    print(f'Finished: {num}')


async def main() -> None:
    print('Started the process')

    list_of_tasks = []

    for n in range(10_000):
        list_of_tasks.append(kill_time(n))

    start_time = time()

    await asyncio.gather(*list_of_tasks)

    print(f'All operations have taken {time() - start_time} seconds')

    print('DONE!')

if __name__ == '__main__':
    asyncio.run(main())
