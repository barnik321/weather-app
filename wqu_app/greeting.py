import requests


def get_geolocation(ip_address):
    """Return gelociaton of an IP address."""
    response = requests.get(f'https://ipinfo.io/{ip_address}')
    data = response.json()
    return data


def location_details(location_data):
    coords = location_data['loc'].split(',')
    place = location_data['city'] + ', ' + location_data['country']
    org = location_data['org']

    return coords, place, org


def get_weather(coords):
    """Return weather data for a given set of coordinates."""
    url = 'https://api.met.no/weatherapi/locationforecast/2.0/compact'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
           (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}
    params = {'lat': coords[0], 'lon': coords[1]}

    response = requests.get(url, params=params, headers=headers)

    return response.json()['properties']['timeseries'][0]['data']['instant']['details']['air_temperature']


def greet(ip_address):
    l_data = get_geolocation(ip_address)
    coords, place, org = location_details(l_data)
    temp = get_weather(coords)

    return place, temp, org


# if __name__ == '__main__':
#     print(greet())
