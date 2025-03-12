from src.model.api_client import APIClient

def main():
    api_client = APIClient(cache_size=2)
    print(api_client.fetch_post(1))  # Primera vez: Cache miss
    print(api_client.fetch_post(1))  # Segunda vez: Cache hit
    print(api_client.fetch_post(2))  # Cache miss, se agrega otro post
    print(api_client.fetch_post(3))  # Cache miss, debería eliminar el post menos usado
    print(api_client.fetch_post(1))  # Si fue eliminado, deberá hacer una nueva petición

if __name__ == "__main__":
    main()