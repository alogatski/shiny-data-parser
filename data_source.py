import requests


def nasa_data_source():
    api_key = "DEMO_KEY"
    url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print(f"Success request: {data}")
        return data
    else:
        print(f"Failed to fetch data from {url}")


def dog_data_source():
    url = "https://dog.ceo/api/breeds/list/all"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print(f"Success request: {data}")
        return data
    else:
        print(f"Failed to fetch data from {url}")


def meteo_data_source():
    latitude = 35.6895  # Tokyo
    longitude = 139.6917
    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print(f"Success request: {data}")
        return data
    else:
        print(f"Failed to fetch data from {url}")
