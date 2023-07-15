# asynchronous code
# need to run using python3.11, because there is no TaskGroup object in versions before


import time
import asyncio


async def print1(sec):
    await asyncio.sleep(sec)
    print(sec)


async def main():
    async with asyncio.TaskGroup() as tg:
        for i in range(1, 16):
            tg.create_task(print1(i))


if __name__ == '__main__':
    start_time = time.time()
    asyncio.run(main())
    print(f'Overall time for program: {time.time() - start_time} seconds.')
