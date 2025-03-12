import requests
from src.model.cache import LFUCache
class APIClient:
    def __init__(self, cache_size=5):
        self.cache = LFUCache(cache_size)

    def fetch_post(self, post_id):
        url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"
        if self.cache.get(url) != -1:
            print("Cache hit")
            return self.cache.get(url)
        print("Cache miss, fetching from API...")
        response = requests.get(url)
        data = response.json()
        self.cache.put(url, data)
        return data
