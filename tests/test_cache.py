import pytest
from unittest.mock import patch, Mock
from src.model.api_client import APIClient


@pytest.fixture
def api_client():
    return APIClient(cache_size=2)


def test_api_cache_hit(api_client):
    mock_response = {"userId": 1, "id": 1, "title": "Test Post", "body": "This is a test"}
    with patch("requests.get", return_value=Mock(json=lambda: mock_response)):
        # Primera vez: Cache miss
        response_1 = api_client.fetch_post(1)
        assert response_1 == mock_response

        # Segunda vez: Cache hit
        response_2 = api_client.fetch_post(1)
        assert response_2 == mock_response


def test_api_cache_eviction(api_client):
    mock_post1 = {"userId": 1, "id": 1, "title": "Post 1", "body": "Body 1"}
    mock_post2 = {"userId": 1, "id": 2, "title": "Post 2", "body": "Body 2"}
    mock_post3 = {"userId": 1, "id": 3, "title": "Post 3", "body": "Body 3"}

    with patch("requests.get", side_effect=[
        Mock(json=lambda: mock_post1),
        Mock(json=lambda: mock_post2),
        Mock(json=lambda: mock_post1),  # Acceder a Post 1 una vez más
        Mock(json=lambda: mock_post3),
        Mock(json=lambda: mock_post2)  # Si Post 2 fue eliminado, se vuelve a obtener desde la API
    ]):
        api_client.fetch_post(1)  # Cache miss
        api_client.fetch_post(2)  # Cache miss (se llena la caché)
        api_client.fetch_post(1)  # Acceder a Post 1 (su frecuencia aumenta)
        api_client.fetch_post(3)  # Cache miss (Post 2 debería eliminarse, ya que es el menos usado)

        # Verificar si Post 2 ha sido eliminado
        response = api_client.fetch_post(2)
        assert response == mock_post2  # Post 2 debe haberse eliminado y volver a obtenerse de la API
        assert api_client.fetch_post(1) == mock_post1  # Post 1 sigue en caché
        assert api_client.fetch_post(3) == mock_post3  # Post 3 sigue en caché


def test_api_multiple_requests(api_client):
    mock_response = {"userId": 2, "id": 5, "title": "Another Post", "body": "More content"}
    with patch("requests.get", return_value=Mock(json=lambda: mock_response)):
        response_1 = api_client.fetch_post(5)
        response_2 = api_client.fetch_post(5)
        assert response_1 == response_2  # Ambas deben venir de la caché después de la primera llamada


def test_api_invalid_post(api_client):
    with patch("requests.get", return_value=Mock(status_code=404, json=lambda: {"error": "Not Found"})):
        response = api_client.fetch_post(9999)
        assert response == {"error": "Not Found"}