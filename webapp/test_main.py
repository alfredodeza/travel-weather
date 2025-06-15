from main import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200


def test_countries():
    response = client.get("/countries")
    assert response.status_code == 200
    assert sorted(response.json()) == ["England", "France", "Germany", "Italy", "Peru", "Portugal", "Spain"]


def test_get_country_cities():
    response = client.get('/country/Portugal')
    assert response.status_code == 200
    data = response.json()
    assert 'cities' in data
    assert 'Lisbon' in data['cities']
    assert 'Porto' in data['cities']


def test_get_country_cities_peru():
    response = client.get('/country/Peru')
    assert response.status_code == 200
    data = response.json()
    assert data['country'] == 'Peru'
    assert 'cities' in data
    assert 'Lima' in data['cities']

# def test_monthly_average():
#     response = client.get("/countries/Portugal/Lisbon/January")
#     assert response.status_code == 200
#     assert isinstance(response.json(), (int, float, dict, list, str))

# def test_monthly_average_invalid_country():
#     response = client.get("/countries/Narnia/Lisbon/January")
#     assert response.status_code == 422 or response.status_code == 500

def test_monthly_average_invalid_city():
    response = client.get("/countries/Portugal/Atlantis/January")
    assert response.status_code == 404

# def test_monthly_average_invalid_month():
#     response = client.get("/countries/Portugal/Lisbon/FakeMonth")
#     assert response.status_code == 404 
#     #or response.status_code == 500
