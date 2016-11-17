from urllib2 import Request, urlopen, URLError


URL = 'http://artsnob.me:5000/api/'


request = Request(URL + 'artist')
try:
    response = urlopen(request)
    data = response.read()
    print(data)
except URLError, e:
    print('#### Error in Artist: ', e)

request = Request(URL + 'artwork')
try:
    response = urlopen(request)
    data = response.read()
    print(data)
except URLError, e:
    print('#### Error in Artwork: ', e)



request = Request(URL + 'style')
try:
    response = urlopen(request)
    data = response.read()
    print(data)
except URLError, e:
    print('#### Error in Style: ', e)


request = Request(URL + 'collection')
try:
    response = urlopen(request)
    data = response.read()
    print(data)
except URLError, e:
    print('#### Error in Collection: ', e)








