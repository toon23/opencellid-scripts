#!/usr/bin/python3
from math import cos, sqrt, pi
import argparse
import requests
import json

# Static
PREFIX = "https://opencellid.org/cell/getInArea?key="
PARAM = "&format=json"

# Class that represents a coordinate
class Coord:
    def __init__(self, lat=0.0, lon=0.0):
        self.lat = lat
        self.lon = lon

    # Constructor to parse coordinates from string in format: 'lat,lon'
    @classmethod
    def from_str(self, s):
        try:
            lat, lon = map(float, s.split(','))
            return self(lat, lon)
        except ValueError:
            print("Error: could not parse location, quitting.")
            quit()

    # Takes number of decimal numbers, default 5
    # Returns Cooridnate as str in format: lat,lon
    def to_str(self, d = 5): 
        return str(round(self.lat, d)) + ',' + str(round(self.lon, d))

    # Takes a  area size in km^2.
    # Returns coordiantes of the corners of the sqare with given area,
    # surrounding the center
    def square_from_point(self, area = 1.0):
        c = 111.3           # km/°
        a = sqrt(area) / 2  # km
    
        lat_del = a / c
        lon_del = a / (c * cos(self.lat * (pi / 180)))
    
        p_max = Coord(self.lat + lat_del, self.lon + lon_del)
        p_min = Coord(self.lat - lat_del, self.lon - lon_del)
        return (p_max, p_min)


def main():
    parser = argparse.ArgumentParser(prog='area')
    parser.add_argument('-p', '--position', type=str, required=True,
            help="Center position of the area. Format: lat,lon as floats")
    parser.add_argument('-k', '--key', type=str, required=True,
            help="Your apikey")
    parser.add_argument('-a', '--area', type=float, default=0.1,
            help="Size of the are in km²")


    args = parser.parse_args()
    loc = Coord.from_str(args.position)
    p_max, p_min = loc.square_from_point(args.area)

    # api request
    url = PREFIX + args.key + "&BBOX=" + p_min.to_str() + ',' + p_max.to_str() + PARAM
    api_result = requests.get(url)
    api_result = json.loads(api_result.text)

   #if api_result['error']:
   #    print("Error while reading opencellid API:\n{}".format(api_result['error']))
   #    quit()

    # pretty printing
    print(str(api_result['count']) + ' Stations Found')
    print("{:^10}|{:^10}, {:^10}|{:^7}|{:^5}|{:^3}| radio".format(
        "cellid", "lat", "lon", "lac", "mcc", "mnc"))
    print("{:->11}{:->23}{:->8}{:->6}{:->4}------".format( "+","+","+","+","+"))

    for cell in api_result['cells']:
        print("{cid:9d} | {lat:8f}, {lon:8f} | {lac:5d} | {mcc:3d} | {mnc:d} | {radio}".format(
            cid=cell['cellid'],
            lat=cell['lat'],
            lon=cell['lon'],
            lac=cell['lac'],
            mcc=cell['mcc'],
            mnc=cell['mnc'],
            radio=cell['radio']))

if __name__ == "__main__":
    main()
