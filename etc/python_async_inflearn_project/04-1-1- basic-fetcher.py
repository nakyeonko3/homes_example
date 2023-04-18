import aiohttp
import asyncio
import time


async def fetcher(session, url):
    async with session.get(url) as response:
        return await response.text()


async def main():
    urls = [
        "https://naver.com",
        "https://www.youtube.com",
        "https://google.com",
    ] * 10

    async with aiohttp.ClientSession() as session:
        result = await asyncio.gather(*[fetcher(session, url) for url in urls])
        print(result)


if __name__ == "__main__":
    start = time.time()
    asyncio.run(main())
    end = time.time()
    print(end - start)
