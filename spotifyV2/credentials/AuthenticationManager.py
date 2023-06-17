import requests
import os


class AuthenticationManager:

    def __init__(self):
        self.clientId: str = os.getenv("CLIENT_ID")
        self.clientSecret: str = os.getenv("CLIENT_SECRET")
        self.accessToken: str = self._requestAccessToken()

    def _requestAccessToken(self) -> str:
        """
        POST \n
        Create access token that is valid for 1h
        :return: access token
        """
        url = "https://accounts.spotify.com/api/token"
        headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }
        data = {
            "grant_type": "client_credentials",
            "client_id": self.clientId,
            "client_secret": self.clientSecret
        }
        return requests.post(url=url, headers=headers, data=data).json()['access_token']
