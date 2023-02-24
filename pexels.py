import requests

# set up API credentials
access_key = 'bnloqyAWYps3hrvL1wg1YpwxlnfF0ytZI6FgqgZmUTmCaGanxtOpahqc'

# set up API endpoint and query parameters
endpoint = 'https://api.pexels.com/v1/search'
query_params = {
    'query': 'Mexican foods',
    'orientation': 'landscape',
    'per_page': 1,
    'page': 1,
    'exclude': 'people, person, girls, ladies, men, gents',
}
headers = {
    'Authorization': access_key,
}

# make API request and parse response
response = requests.get(endpoint, params=query_params, headers=headers)
response_data = response.json()

# extract image URL from response
image_url = response_data['photos'][0]['src']['large']

# download and save image to file
response = requests.get(image_url)
with open('indian_food.jpg', 'wb') as f:
    f.write(response.content)
