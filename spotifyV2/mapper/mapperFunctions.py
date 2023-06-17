

def ids_of_tracks(tracks: dict) -> list[str]:
    """
    """
    return list(map(lambda track: track['track']['id'], tracks['items']))


def ids_of_top_tracks(tracks: dict) -> list[str]:  # todo really needed ?
    """
    """
    return list(map(lambda track: track['id'], tracks['items']))


def convert_track_ids_to_uris(ids: list[str]) -> list[str]:
    """
    """
    return [f"spotify:track:{song_id}" for song_id in ids]


def get_total_amount_of_tracks_in_liked_tracks(response: dict) -> int:
    """
    Currently the result is lower than the actual amount since I have
    liked songs that aren't in Spotify, like 'Motiva' by 'Bladesa'.
    """
    return response['total']
