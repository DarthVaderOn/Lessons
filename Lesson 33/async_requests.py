import asyncio
from time import time
import aiohttp
from all.sites import sites


user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) ' \
                     'Chrome/81.0.4044.138 Safari/537.36'


async def send_request(url):
    start_time = time()

    async with aiohttp.request('GET', url, headers={'User-Agent': user_agent}) as response:
        await response.text()
        print(f'[{url}] Time elapsed: {time() - start_time:.2f}s ({response.status})')



async def main():
    start_time = time()
    tasks = [send_request(site) for site in sites]
    await asyncio.gather(*tasks)

    print(f'Total time elapsed: {time() - start_time:.2f}s')


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())