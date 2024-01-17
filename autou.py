import requests
import base64
import env_secrets

# Your client key and secret
client_key = "key"
client_secret = "secret"

# Encode the client key and secret
credentials = f"{env_secrets.client_key}:{env_secrets.client_secret}"
encoded_credentials = base64.b64encode(credentials.encode()).decode()
#encoded_credentials = credentials

# Set the headers
headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'Authorization': f'Basic {encoded_credentials}'
}

# Set the data for the body of the request
data = {
    'grant_type': 'client_credentials'
}

# The URL for the request
url = "https://api.coursera.com/oauth2/client_credentials/token"

# Make the request
response = requests.post(url, headers=headers, data=data)

# Print the response
import json
token = json.loads(response.text)

print(json.dumps(token, indent=2))

# get the businesses url
url = "https://api.coursera.com/ent/api/businesses.v1"
headers = {
    'Authorization': f'Bearer {token["access_token"]}'
}

#response = requests.get(url, headers=headers)
#print(response.text)
