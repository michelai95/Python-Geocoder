import geocoder
import requests


destinations = [
    "Space Needle",
    "Crater Lake",
    "Golden Gate Bridge",
    "Yosemite National Park",
    "Las Vegas, Nevada",
    "Grand Canyon National Park",
    "Aspen, Colorado",
    "Mount Rushmore",
    "Yellowstone National Park",
    "Sandpoint, Idaho",
    "Banff National Park",
    "Capilano Suspension Bridge"
]

for point in Destinations
    loc = geocoder.arcgis(point)

    print("{0} is located at ({1:.4f}, {2: .4f})".format(point, loc.latlng[0], loc.latlng[1]))