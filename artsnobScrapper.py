from urllib2 import Request, urlopen, URLError
import json


URL = 'http://artsnob.me:5000/api/'


request = Request(URL + 'artist')

f = open('jsonstuff.json', 'w')
'''
try:
    response = urlopen(request)
    data = response.read()
    f.write(data)
    # print(data)
except URLError, e:
    print('#### Error in Artist: ', e)


request = Request(URL + 'artwork')
try:
    response = urlopen(request)
    data = response.read()
    f.write(data)
    # print(data)
except URLError, e:
    print('#### Error in Artwork: ', e)



request = Request(URL + 'style')
try:
    response = urlopen(request)
    data = response.read()
    f.write(data)
    # print(data)
except URLError, e:
    print('#### Error in Style: ', e)


request = Request(URL + 'collection')
try:
    response = urlopen(request)
    data = response.read()
    f.write(data)
    # print(data)
except URLError, e:
    print('#### Error in Collection: ', e)
'''

response = urlopen(request)
data = json.loads(response.read())
jsonstuffs = {'name': 'Artists', 'children': []}
for artist in data['objects']:
    artistinfo = {'name': artist['name'], 'children':[]}
    for artwork in artist['artworks']:
        artistinfo['children'].append({'name': artwork['title'], 'size': 1000})
    jsonstuffs['children'].append(artistinfo)
f.write(json.dumps(jsonstuffs))
f.close()







