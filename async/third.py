import asyncio

import api


async def main() -> None:
    task = asyncio.create_task(api.fetch_data())  # task starts immediately

    # task.cancel()  # we can cancel just the task if it's not finished yet

    try:
        res = await task  # to get the returned data
        print(res)

        # await asyncio.wait_for(task, timeout=2)  # we can specify how long we can wait for task to finish

    except asyncio.CancelledError:
        print('Request was cancelled')
    except asyncio.TimeoutError:
        print('Timeout: Request took to long.')


if __name__ == '__main__':
    ...
