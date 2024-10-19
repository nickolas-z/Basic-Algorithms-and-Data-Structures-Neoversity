import requests
from timeit import timeit
from functools import lru_cache


cache = dict()

dict = {
    "word": "meaning"
}

def get_article_from_server(url):
    print("OWN Fetching article from server...")
    response = requests.get(url)
    return response.text

def get_article(url):
    print("OWN Getting article...")
    if url not in cache:
        cache[url] = get_article_from_server(url)

    return cache[url]

def measure_time(arg):
    execution_time = timeit(lambda: get_article(arg), number=1)
    print("OWN Execution time:", execution_time, "seconds")

measure_time("https://google.com")
measure_time("https://youtube.com")
measure_time("https://youtube.com")
measure_time("https://google.com")
measure_time("https://youtube.com")





@lru_cache(maxsize=1)  # Decorate the function with @lru_cache
def get_article_from_server(url):
    print("LRU Fetching article from server...")
    response = requests.get(url)
    return response.text

def get_article(url):
    print("LRU Getting article...")
    return get_article_from_server(url)

def measure_time(arg):
    execution_time = timeit(lambda: get_article(arg), number=1)
    print("LRU Execution time:", execution_time, "seconds")

measure_time("https://google.com")
measure_time("https://google.com")
measure_time("https://youtube.com")
measure_time("https://youtube.com")
measure_time("https://youtube.com")