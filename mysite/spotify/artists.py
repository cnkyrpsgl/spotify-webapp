import requests

def getArtists(access_token):
    payload = {"type":"artist","limit":"50"}
    headers = {
    'Authorization': "Bearer " + access_token
    }
    ids = []
    r = requests.get("https://api.spotify.com/v1/me/following", headers = headers, params = payload).json()["artists"]
    ids += [artist["id"] for artist in r["items"]]
    while r["cursors"]["after"]:
        payload["after"] = r["cursors"]["after"]
        r = requests.get("https://api.spotify.com/v1/me/following", headers = headers, params = payload).json()["artists"]
        ids += [artist["id"] for artist in r["items"]]
    return ids
