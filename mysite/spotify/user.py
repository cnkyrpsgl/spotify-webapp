import requests

def getUser(access_token):
    headers = {
        'Authorization': "Bearer " + access_token,
        }
    r = requests.get("https://api.spotify.com/v1/me", headers = headers).json()
    return r["display_name"], r["images"][0]["url"]