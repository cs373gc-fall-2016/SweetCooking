from urllib2 import Request, urlopen, URLError

print('artsnob.me api scraper')
print()


URL = 'http://artsnob.me/'


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


collection_id = 1
request = Request(URL + 'collection/' + str(collection_id))
try:
    response = urlopen(request)
    data = response.read()
    print(data)
except URLError, e:
    print('#### Error in Collection: ', e)








