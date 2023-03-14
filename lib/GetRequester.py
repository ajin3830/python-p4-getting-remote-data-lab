import requests
import json

class GetRequester:
# GetRequester class retrieves JSON from any provided URL
    
    # the url gets passed in on initialization  
    def __init__(self, url):
        self.url = url

    # instance method to get the response body from the requested URL
    def get_response_body(self):
        response = requests.get(self.url)
        return response.content

    def load_json(self):
        # we use the JSON library to parse the API response into nicely formatted JSON
        # meaning with the data we got back from the API we can collect and present it
        # here we're just returning it
        json_content = json.loads(self.get_response_body())
        return json_content