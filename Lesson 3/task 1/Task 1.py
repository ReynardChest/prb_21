import re
import operator
from functools import reduce
from collections import namedtuple
import math as m


def decimal_conversion(coord_list):
    dec_coord_list = []
    for coord in coord_list:

        try:
            x = float(coord)
        except ValueError:
            print('Ошибка, {} в заданом массиве не число'.format(coord))
            return

        deg = int(x // 100)
        mins = int(x % 100)
        secs = x % 1 * 60
        dec = deg + mins/60 + secs/3600
        dec_coord_list.append(dec)
    return dec_coord_list


def nmea_processing(line):

    def check_checksum(nmea_str, checksum):
        nmea_10 = reduce(operator.xor, map(ord, nmea_str), 0)
        checksum_10 = int(checksum, 16)
        return nmea_10 == checksum_10

    match = re.match(r'''[\s\$]?(?P<nmea_str>(?P<sentence_type>\w+),(?P<data>[^*]*))\*(?P<checksum>..)''', line)

    if match:
        nmea_str = match.group('nmea_str')
        checksum = match.group('checksum')

        if check_checksum(nmea_str, checksum):
            return match.group('data')


def form_dec_array(data):

    try:
        data = data.split(sep=',')
    except (AttributeError) as e:
        print(e)
        return

    dec_coord = decimal_conversion([float(data[1]), float(data[3])])

    if data[2] == "S":
        lat = -dec_coord[0]
    else:
        lat = dec_coord[0]

    if data[4] == "W":
        lon = -dec_coord[1]
    else:
        lon = dec_coord[1]

    coordinates = namedtuple('coordinates', 'lat lon')
    coord = coordinates(lat, lon)

    return coord


def calc_meters(lat0, lon0, lat1, lon1, mode = 'euclid'):
    lat0 = m.radians(lat0)
    lon0 = m.radians(lon0)
    lat1 = m.radians(lat1)
    lon1 = m.radians(lon1)

    delta_lat = lat1 - lat0
    delta_lon = lon1 - lon0

    R = 6371007  # Радиус Земли в метрах
    if mode == 'sphere':
        # Теорема сферических косинусов, использовать при расстоянии более 1 км
        # https://en.wikipedia.org/wiki/Great-circle_distance
        sphere_meters = R * m.acos(m.sin(lat0)*m.sin(lat1) + m.cos(lat0)*m.cos(lat1)*m.cos(delta_lon))
        return sphere_meters

    if mode == 'euclid':
        # Эвклидова метрика, использовать при расстоянии менее 1 км
        # https://en.wikipedia.org/wiki/Equirectangular_projection
        lat_norm = m.cos((lat1 + lat0)/2)
        euclid_meters = R * m.hypot(delta_lon * lat_norm, delta_lat)
        return euclid_meters

    if mode == 'haversine':
        # Формула гаверсина, использовать при любом расстоянии
        # https://en.wikipedia.org/wiki/Great-circle_distance
        a = m.sin(delta_lat/2) * m.sin(delta_lat/2) + m.cos(lat0) * m.cos(lat1) * m.sin(delta_lon/2) * m.sin(delta_lon/2)
        haversin_meters = 2 * R * m.atan2(m.sqrt(a), m.sqrt(1-a))
        return haversin_meters


def sec2hms(secs):
    s = secs % 60
    m = secs // 60
    h = secs // 3600
    return h, m, s


def get_data():
    file_name = input('Название файла: ')
    freq = 0.2
    distance = 25
    target = {'lat': 60.051584, 'lon': 30.300509}
    return file_name, freq, distance, target


def main():
    file_name, freq, distance, target = get_data()
    time = 0
    with open(file_name, "r") as f:
        for line in f:
            if nmea_processing(line) is None:
                continue
            else:
                dec_coord = form_dec_array(nmea_processing(line))
                meters = calc_meters(target['lat'], target['lon'], dec_coord.lat, dec_coord.lon)
                if meters <= distance:
                    time += freq
    h, m, s = sec2hms(time)
    return print(f"Время на дистанции менее {distance} м: \n{h:.0f}:{m:02.0f}:{s:02.0f}")


if __name__ == '__main__':
    main()
