import requests

# set up API credentials
access_key = 'yBmgjsN6dvAUlGBPiqeVoFa7RBfrI6u3WKlOLNaJOJk'

# set up API endpoint and query parameters
endpoint = 'https://api.unsplash.com/search/photos'
query_params = {
    'query': 'Mexican platter',
    'orientation': 'landscape',
    'per_page': 1,
    'client_id': access_key,
     'license': 'commercial',
}

# make API request and parse response
response = requests.get(endpoint, params=query_params)
response_data = response.json()

# extract image URL from response
image_url = response_data['results'][0]['urls']['regular']

# download and save image to file
response = requests.get(image_url)
with open('indian_food.jpg', 'wb') as f:
    f.write(response.content)
