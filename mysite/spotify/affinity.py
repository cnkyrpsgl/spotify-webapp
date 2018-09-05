import requests

def getAffinity(access_token, get_type, time_frame):
    payload = {"time_range": time_frame,"limit":"50"}
    headers = {
        'Authorization': "Bearer " + access_token,
        }
    r = requests.get("https://api.spotify.com/v1/me/top/{}".format(get_type), headers = headers, params = payload).json()
    if get_type == "artists":
        #name, img, href
        return [[artist["name"], artist["images"][1]["url"], artist["external_urls"]["spotify"]] for artist in r["items"]]
    #title, artist, album, href
    return [[track["name"], [artist["name"] for artist in track["artists"]], track["album"]["name"], track["external_urls"]["spotify"]] for track in r["items"]]