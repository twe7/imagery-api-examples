# This example shows, how to download an image from the catalog
import requests

# set your API key here
apiKey = ''

# retrieve a list of all images and download the first one
r = requests.get('https://api.tailwindimaging.com/image', headers={'x-api-key': apiKey})
image = r.json()['results'][0]

print('Downloading {} ...'.format(image['fileName']))

downloadResponse = requests.get('https://api.tailwindimaging.com/image/{}/download'.format(image['id']), headers={'x-api-key': apiKey})
downloadedImage = requests.get(downloadResponse.json()['downloadUrl'], headers={'x-api-key': apiKey})
open(image['fileName'], 'wb').write(downloadedImage.content)

print('Done')

