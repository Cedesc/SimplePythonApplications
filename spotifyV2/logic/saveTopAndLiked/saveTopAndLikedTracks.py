from datetime import date, timedelta
from spotifyV2.spotipyRequests.SpotipyRequests import SpotipyRequests
from spotifyV2.mapper.mapperFunctions import ids_of_tracks, ids_of_top_tracks, convert_track_ids_to_uris, get_total_amount_of_tracks_in_liked_tracks


def _get_month_in_german(month_string: str) -> str:
    """Solved with a dictionary since I haven't python3.10 with pattern matching."""
    match month_string:
        case '01': return 'Jan'
        case '02': return 'Feb'
        case '03': return 'Mär'
        case '04': return 'Apr'
        case '05': return 'Mai'
        case '06': return 'Jun'
        case '07': return 'Jul'
        case '08': return 'Aug'
        case '09': return 'Sep'
        case '10': return 'Okt'
        case '11': return 'Nov'
        case '12': return 'Dez'
        case _: raise IndexError


def _get_last_month() -> (str, str):
    today = date.today()
    first = today.replace(day=1)
    last_month = first - timedelta(days=1)
    return last_month.strftime("%m"), last_month.strftime("%y")


def _generate_playlist_name(prefix: str) -> str:
    month, year = _get_last_month()
    month_written = _get_month_in_german(month)
    return f"{prefix} {month_written} {year}"


def create_top_tracks_save(
        sp_req: SpotipyRequests,
        time_range: str = 'short_term',
        number_of_songs: int = 50
):
    """
    Saves the top tracks of the last 4 weeks.
    """
    # get songs of favorites
    tracks = sp_req.get_top_songs(time_range=time_range, limit=number_of_songs, offset=0)
    print(f"LOG (top tracks): Get top tracks: {tracks}")

    # convert to the ids
    ids: list[str] = ids_of_top_tracks(tracks)

    # convert ids to uris
    uris: list[str] = convert_track_ids_to_uris(ids)

    # create new playlist (moving it to the right folder isn't possible so far)
    playlist_name: str = _generate_playlist_name("Top Tracks")
    playlist = sp_req.create_playlist(playlist_name, public=True, description="")
    print(f"LOG (top tracks): Create playlist: {playlist}")
    # save playlist id
    playlist_id = playlist['id']

    # fill playlist with songs
    added_elements = sp_req.add_items_to_playlist(playlist_id, uris)
    print(f"LOG (top tracks): Added elements: {added_elements}")

    return added_elements


def create_liked_tracks_save(sp_req: SpotipyRequests):
    """
    Saves the currently liked tracks.
    The maximum value for the 'limit' of 'get_liked_songs()' is 50, but since I have more than 50 liked songs, the
    function has to be called multiple times.
    """
    # get songs of favorites
    # (saved in the list 'track_packages' instead of 'tracks' because of the maximum limit of 50)
    track_packages = [sp_req.get_liked_songs(limit=50, offset=0)]
    # get amount of liked songs
    total_track_amount: int = track_packages[0]['total']
    # necessary additional calls of get_like_songs()
    for i in range((total_track_amount-1) // 50):
        track_packages.append(sp_req.get_liked_songs(limit=50, offset=(i+1)*50))
    print(f"LOG (liked tracks): Get liked tracks: {track_packages}")

    # convert to the ids
    # (multiple calls of extract_ids_get_playlist_items() are necessary because the tracks aren't all in one variable)
    ids: list[str] = []
    for package in track_packages:
        ids += ids_of_tracks(package)

    # convert ids to uris
    uris: list[str] = convert_track_ids_to_uris(ids)

    # create new playlist (moving it to the right folder isn't possible so far)
    playlist_name: str = _generate_playlist_name("Liked Tracks")
    playlist = sp_req.create_playlist(playlist_name, public=True, description="")
    print(f"LOG (liked tracks): Create playlist: {playlist}")
    # save playlist id
    playlist_id = playlist['id']

    # fill playlist with songs
    # (multiple calls of add_items_to_playlist() are necessary since only 100 items can be added at once)
    added_elements_package = []
    for i in range(((total_track_amount-1) // 100) + 1):
        lower_bound = 100 * i
        upper_bound = (100 * i) + 100
        added_elements_package.append(
            sp_req.add_items_to_playlist(playlist_id, uris[lower_bound:upper_bound]))
    print(f"LOG (liked tracks): Added elements: {added_elements_package}")

    return added_elements_package
