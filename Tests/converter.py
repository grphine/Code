import re


def splitter(coordinate_string):
    match_result = re.search("(\d{2})\..*", coordinate_string)
    return [coordinate_string[0:match_result.span()[0]], match_result.group(0)]


lat = "5222.9561"     #52° 22.9561'
long = "133.7536"     #1° 33.7536'


a = splitter(lat)
b = splitter(long)

print(a,b)