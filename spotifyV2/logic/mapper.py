
# todo unused because file cant be imported. Why??


def idsOfTracks(tracks: dict) -> list[str]:
    """
    """
    return list(map(lambda track: track['track']['id'], tracks['items']))


def idsOfTopTracks(tracks: dict) -> list[str]:  # todo really needed ?
    """
    """
    return list(map(lambda track: track['id'], tracks['items']))


def convertTrackIdToUri(ids: list[str]) -> list[str]:
    """
    """
    return [f"spotify (legacy):track:{song_id}" for song_id in ids]


def getTotalAmountOfTracksInLikedTracks(response: dict) -> int:
    """
    Currently the result is lower than the actual amount since I have
    liked songs that aren't in Spotify, like 'Motiva' by 'Bladesa'.
    """
    return response['total']
