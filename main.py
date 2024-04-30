from API.geocoder import get_ll_span
from API.business import find_businesses
from API.mapapi_PG import show_map

ll, spn = get_ll_span(input('Введите адрес: '))
drugstores = find_businesses(ll, spn, 'аптека')

points = []

for store in drugstores:
    lon, lat = store['geometry']['coordinates']
    time_data = store['properties']['CompanyMetaData']['Hours']['Availabilities'][0]

    if time_data.get('TwentyFourHours'):
        color = 'gn'
    elif time_data.get('Intervals'):
        color = 'bl'
    else:
        color = 'gr'

    points.append(f'{lon},{lat},pm2{color}m')

ll_spn = f'll={ll}'
show_map(ll_spn, 'map', f'pt={"~".join(points)}')
