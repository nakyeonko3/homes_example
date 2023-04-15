import time
import os
import threading
import requests
from concurrent.futures import ThreadPoolExecutor


def fetcher(params):
    session = params[0]
    url = params[1]
    print(f"{os.getpid()} process | {threading.get_ident()} url : {url}")
    with session.get(url) as response:
        return response.text


def main():
    urls = [
        "https://google.com",
        "https://www.youtube.com",
    ] * 50

    executor = ThreadPoolExecutor(max_workers=15)

    with requests.Session() as session:
        params = [(session, url) for url in urls]
        list(executor.map(fetcher, params))


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(end - start)  # 50
