from spotifyV2.mapper.mapperFunctions import *
from spotifyV2.spotipyRequests.SpotipyRequests import SpotipyRequests


def get_percentage_of_truly_new_tracks(
        sp_req: SpotipyRequests,
        new_playlist: str,
        old_playlists: list[str]
) -> float:
    number_of_truly_new_tracks = len(_get_new_tracks_without_previous_occurrences(sp_req, new_playlist, old_playlists))
    number_of_tracks_in_new_playlist = sp_req.get_number_of_tracks_in_playlist(new_playlist)

    print("number of truly new: ")
    print(number_of_truly_new_tracks)
    print("number of tracks in new playlist: ")
    print(number_of_tracks_in_new_playlist)

    return number_of_truly_new_tracks / number_of_tracks_in_new_playlist * 100


def _get_new_tracks_without_previous_occurrences(
        sp_req: SpotipyRequests,
        new_playlist: str,
        old_playlists: list[str]
) -> set[str]:
    """
    """
    # get all tracks of new_playlist
    new_tracks = sp_req.get_playlist_items(new_playlist)
    new_tracks = ids_of_tracks(new_tracks)

    truly_new_tracks: set = \
        set(filter(lambda track: not _track_is_in_one_of_many_playlists(sp_req, track, old_playlists), new_tracks))

    return truly_new_tracks


def _track_is_in_one_of_many_playlists(sp_req: SpotipyRequests, track_id: str, playlist_ids: list[str]) -> bool:
    """
    Returns:
        True, if the track is in one or more of the given playlists. Otherwise, False.
    """
    for playlist_id in playlist_ids:
        if _track_is_in_playlist(sp_req, track_id, playlist_id):
            return True
    return False


def _track_is_in_playlist(sp_req: SpotipyRequests, track_id: str, playlist_id: str) -> bool:
    """
    Returns:
        True, if the track is in the given playlist. Otherwise, False.
    """
    # create an empty set
    playlist_tracks_ids: set[str] = set()

    # get all tracks of the playlist and add them to the previously created set
    # (multiple calls of get_playlist_items() may be necessary since only 100 items can be added at once)
    total_track_amount = sp_req.get_number_of_tracks_in_playlist(playlist_id)
    for i in range(((total_track_amount - 1) // 100) + 1):
        lower_bound = 100 * i
        tracks = sp_req.get_playlist_items(playlist_id=playlist_id, offset=lower_bound)
        tracks = ids_of_tracks(tracks)
        playlist_tracks_ids.update(tracks)

    print(track_id)

    # check if track_id is in playlist_tracks_ids
    return track_id in playlist_tracks_ids
