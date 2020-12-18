import requests


def retrieve_ip_adress():
    """Return IP address of our computer."""
    response = requests.get('https://api.ipify.org')

    return response.text


def get_geolocation(ip_address):
    """Return gelociaton of an IP address."""
    response = requests.get(f'https://ipinfo.io/{ip_address}')
    data = response.json()
    coords = [float(coord) for coord in data['loc'].split(',')]

    return coords


def get_weather(coords):
    """Return weather data for a given set of coordinates."""
    url = 'https://api.met.no/weatherapi/locationforecast/2.0/compact'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
           (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}
    params = {'lat': coords[0], 'lon': coords[1]}

    response = requests.get(url, params=params, headers=headers)

    return response.json()['properties']['timeseries'][0]['data']['instant']['details']['air_temperature']


def greet():
    ip_address = retrieve_ip_adress()
    coords = get_geolocation(ip_address)
    temp = get_weather(coords)

    return f'Hello the temperature is {temp} deg C'


if __name__ == '__main__':
    print(greet())
