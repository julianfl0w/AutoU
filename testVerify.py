import requests
import json

# The URL where your Flask app is running
flask_app_url = "http://127.0.0.1:5000/verify"

# List of Coursera certificate URLs to verify
coursera_cert_urls = [
    "https://www.coursera.org/account/accomplishments/professional-cert/UNA42T665N9U",
    "https://www.coursera.org/account/accomplishments/verify/37H9RNNQMSFV"
    # Add more certificate URLs as needed
]

# Send a POST request to the Flask app with the list of Coursera URLs
response = requests.post(flask_app_url, json={'urls': coursera_cert_urls})

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()
    print(f"Names on the certificates: {json.dumps(data,indent=2)}")
else:
    print(f"Error: Received status code {response.status_code}")
