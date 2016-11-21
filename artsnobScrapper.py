from urllib2 import Request, urlopen, URLError
import json


URL = 'http://artsnob.me:5000/api/'


request = Request(URL + 'artist')

f = open('jsonstuff.json', 'w')

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







