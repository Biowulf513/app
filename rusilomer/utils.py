# -*- coding: utf-8 -*-
import requests


def location_geoconing(city='', venue=''):
    api_key = 'AIzaSyBEyU7CLrolAMH0Ou8oi_FXxbQ1TVLpKPI'
    url = 'https://maps.googleapis.com/maps/api/geocode/json?&address=%s+%s&key=%s&language=ru' %(city, venue, api_key)

    json_data = requests.get(url)
    print_data = json_data.json()
    coordinates = print_data['results'][0]['geometry']['location']
    lat = coordinates['lat']
    lng = coordinates['lng']
    geocoding={'lat':lat, 'lng':lng}
    return geocoding