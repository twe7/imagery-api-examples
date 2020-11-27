# This example shows, how to purchase an image from the catalog
import requests

# set your API key here
apiKey = ''

# retrieve a list of all images and purchase the first one
r = requests.get('https://api.tailwindimaging.com/image', headers={'x-api-key': apiKey})
firstImage = r.json()['results'][0]

# purchase the image by performing a POST request with a JSON body
data = {
    'images': [{'id': firstImage['id']}]
}
r = requests.post('https://api.tailwindimaging.com/store/purchase', json=data, headers={'x-api-key': apiKey})

if r.status_code == 200:
    print('Image purchased successfully')
else:
    print('Error: {}'.format(r.text))

