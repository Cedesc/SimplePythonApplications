import requests


def get_top_songs(access_token: str, time_range: str = 'short_term', limit: int = 50):
    """https://developer.spotify.com/console/get-current-user-top-artists-and-tracks/
    The 'top songs' aren't the favored songs, but the top songs of this website:
    https://www.statsforspotify.com/track/top?timeRange=short_term
    Possible time_ranges are 'short_term', 'medium_term' and 'long_term'."""
    response = requests.get(
        f"https://api.spotify.com/v1/me/top/tracks?time_range={time_range}&limit={limit}",
        headers={
            "Authorization": f"Bearer {access_token}"
        }
    )

    return response.json()


def get_liked_songs(access_token: str, limit: int = 50, offset: int = 0):
    """https://developer.spotify.com/console/get-current-user-saved-tracks/
    The 'liked songs' or 'saved songs' are the favored songs."""
    response = requests.get(
        f"https://api.spotify.com/v1/me/tracks?limit={limit}&offset={offset}",
        headers={
            "Authorization": f"Bearer {access_token}"
        }
    )

    return response.json()


def get_playlist_items(access_token: str, playlist_id: str, limit: int = 25):
    """https://developer.spotify.com/console/get-playlist-tracks/"""
    response = requests.get(
        f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks?fields=items(track(id))&limit={limit}",
        headers={
            "Authorization": f"Bearer {access_token}"
        }
    )

    return response.json()


def create_playlist(access_token: str, name: str, public: bool = True, description: str = ""):
    """https://developer.spotify.com/console/post-playlists/"""
    response = requests.post(
        'https://api.spotify.com/v1/users/cedesc3/playlists',
        headers={
            "Authorization": f"Bearer {access_token}"
        },
        json={
            "name": name,
            "public": public,
            "description": description
        }
    )

    return response.json()


def add_items_to_playlist(access_token: str, playlist_id: str, uris: list[str]):
    """https://developer.spotify.com/console/post-playlist-tracks/"""
    response = requests.post(
        f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks",
        headers={
            "Authorization": f"Bearer {access_token}"
        },
        json={
            "uris": uris
        }
    )

    return response.json()


def extract_ids_get_playlist_items(response: dict) -> list[str]:

    result: list[str] = []

    list_of_songs: list = response['items']

    for i in range(len(list_of_songs)):
        result.append(list_of_songs[i]['track']['id'])

    return result


def extract_ids_get_top_tracks(response: dict) -> list[str]:

    result: list[str] = []

    list_of_songs: list = response['items']

    for i in range(len(list_of_songs)):
        result.append(list_of_songs[i]['id'])

    return result


def convert_song_ids_to_uris(ids: list[str]) -> list[str]:
    return [f"spotify:track:{song_id}" for song_id in ids]


def get_total_track_amount_of_liked_tracks(response: dict) -> int:
    """Currently the result is lower than the actual amount since I have liked songs that aren't in Spotify,
    like 'Motiva' by 'Bladesa'."""
    return response['total']
