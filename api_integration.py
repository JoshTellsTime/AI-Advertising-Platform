# api_integration.py

import requests
from config import GOOGLE_API_KEY, FACEBOOK_API_KEY, INSTAGRAM_API_KEY, MICROSOFT_API_KEY, TWITTER_API_KEY

class APIIntegration:
    @staticmethod
    def google_api_request(endpoint, params):
        headers = {'Authorization': 'Bearer ' + GOOGLE_API_KEY}
        response = requests.get(endpoint, headers=headers, params=params)
        return response.json()

    @staticmethod
    def facebook_api_request(endpoint, params):
        headers = {'Authorization': 'Bearer ' + FACEBOOK_API_KEY}
        response = requests.get(endpoint, headers=headers, params=params)
        return response.json()

    @staticmethod
    def instagram_api_request(endpoint, params):
        headers = {'Authorization': 'Bearer ' + INSTAGRAM_API_KEY}
        response = requests.get(endpoint, headers=headers, params=params)
        return response.json()

    @staticmethod
    def microsoft_api_request(endpoint, params):
        headers = {'Authorization': 'Bearer ' + MICROSOFT_API_KEY}
        response = requests.get(endpoint, headers=headers, params=params)
        return response.json()

    @staticmethod
    def twitter_api_request(endpoint, params):
        headers = {'Authorization': 'Bearer ' + TWITTER_API_KEY}
        response = requests.get(endpoint, headers=headers, params=params)
        return response.json()