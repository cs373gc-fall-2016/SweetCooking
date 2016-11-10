from urllib2 import Request, urlopen, URLError

print('artsnob.me api scraper')
print()


URL = 'http://artsnob.me/'


request = Request(URL + 'Artist')
try:
    response = urlopen(request)
    data = response.read()
    print(data)
except URLError, e:
    print('#### Error in Artist: ', e)

request = Request(URL + 'Artwork')
try:
    response = urlopen(request)
    data = response.read()
    print(data)
except URLError, e:
    print('#### Error in Artwork: ', e)



request = Request(URL + 'Style')
try:
    response = urlopen(request)
    data = response.read()
    print(data)
except URLError, e:
    print('#### Error in Style: ', e)


collection_id = 1
request = Request(URL + 'Collection/' + str(collection_id))
try:
    response = urlopen(request)
    data = response.read()
    print(data)
except URLError, e:
    print('#### Error in Collection: ', e)








