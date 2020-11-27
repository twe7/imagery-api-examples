import requests
import json

# set your API key here
apiKey = ''

# retrieve a list of all images
r = requests.get('https://api.tailwindimaging.com/image', headers={'x-api-key': apiKey})

# pretty-print JSON output
json_formatted_str = json.dumps(r.json(), indent=2)
print(json_formatted_str)
