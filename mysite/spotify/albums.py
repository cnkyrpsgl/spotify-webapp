import requests
import time
def getAlbums(access_token, id):
    try:
        payload = {"include_groups" :"album", "limit": 1}
        headers = {
        'Authorization': "Bearer " + access_token,
        }
        r = requests.get("https://api.spotify.com/v1/artists/{}/albums".format(id), headers = headers, params = payload).json()
        if r["items"]:
            return r["items"][0]["artists"][0]["name"], r["items"][0]["name"], r["items"][0]["release_date"], r["items"][0]["images"][1]["url"], r["items"][0]["external_urls"]["spotify"]
        return None
        # artist, album, date, img, href
    except:
        time.sleep(5)
        return getAlbums(access_token, id)