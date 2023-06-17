from datetime import date, timedelta
import spotifyAPIFunctions as sAPI


def getMonthInGerman(month_string: str) -> str:
    """Solved with a dictionary since I haven't python3.10 with pattern matching."""
    switch = {
        '01': 'Jan',
        '02': 'Feb',
        '03': 'Mär',
        '04': 'Apr',
        '05': 'Mai',
        '06': 'Jun',
        '07': 'Jul',
        '08': 'Aug',
        '09': 'Sep',
        '10': 'Okt',
        '11': 'Nov',
        '12': 'Dez',
    }
    result = switch.get(month_string)
    if result is None:
        raise IndexError
    return switch.get(month_string)


def getLastMonth() -> (str, str):
    today = date.today()
    first = today.replace(day=1)
    lastMonth = first - timedelta(days=1)
    return lastMonth.strftime("%m"), lastMonth.strftime("%y")


def generatePlaylistName(prefix: str) -> str:
    month, year = getLastMonth()
    monthWritten = getMonthInGerman(month)
    return f"{prefix} {monthWritten} {year}"


def createTopTracksSave(access_token: str,
                        time_range: str = 'short_term', number_of_songs: int = 50):
    """Saves the top tracks of the last 4 weeks."""

    # get songs of favorites
    tracks = sAPI.get_top_songs(access_token, time_range=time_range, limit=number_of_songs)
    # print(f"Get top tracks: {tracks}")
    print(f"Get top tracks")

    # convert to the ids
    ids: list[str] = sAPI.extract_ids_get_top_tracks(tracks)

    # convert ids to uris
    uris: list[str] = sAPI.convert_song_ids_to_uris(ids)

    # create new playlist (moving it to the right folder isn't possible so far)
    playlist_name: str = generatePlaylistName("Top Tracks")
    playlist = sAPI.create_playlist(access_token, playlist_name, public=True, description="")
    # print(f"Create playlist: {playlist}")
    print(f"Create playlist")
    # save playlist id
    playlist_id = playlist['id']

    # fill playlist with songs
    added_elements = sAPI.add_items_to_playlist(access_token, playlist_id, uris)
    # print(f"Added elements: {added_elements}")
    print(f"Added elements")

    return added_elements


def createLikedTracksSave(access_token: str):
    """Saves the currently liked tracks.
    The maximum value for the 'limit' of 'get_liked_songs()' is 50, but since I have more than 50 liked songs, the
    function has to be called multiple times."""

    # get songs of favorites
    # (saved in the list 'track_packages' instead of 'tracks' because of the maximum limit of 50)
    track_packages = [sAPI.get_liked_songs(access_token, limit=50, offset=0)]
    # get amount of liked songs
    total_track_amount: int = sAPI.get_total_track_amount_of_liked_tracks(track_packages[0])
    # necessary additional calls of get_like_songs()
    for i in range((total_track_amount-1) // 50):
        track_packages.append(sAPI.get_liked_songs(access_token, limit=50, offset=(i+1)*50))
    print(f"Get liked tracks")

    # convert to the ids
    # (multiple calls of extract_ids_get_playlist_items() are necessary because the tracks aren't all in one variable)
    ids: list[str] = []
    for package in track_packages:
        ids += sAPI.extract_ids_get_playlist_items(package)

    # convert ids to uris
    uris: list[str] = sAPI.convert_song_ids_to_uris(ids)

    # create new playlist (moving it to the right folder isn't possible so far)
    playlist_name: str = generatePlaylistName("Liked Tracks")
    playlist = sAPI.create_playlist(access_token, playlist_name, public=True, description="")
    print(f"Create playlist")
    # save playlist id
    playlist_id = playlist['id']

    # fill playlist with songs
    # (multiple calls of add_items_to_playlist() are necessary since only 100 items can be added at once)
    added_elements_package = []
    for i in range(((total_track_amount-1) // 100) + 1):
        lower_bound = 100 * i
        upper_bound = (100 * i) + 100
        added_elements_package.append(
            sAPI.add_items_to_playlist(access_token, playlist_id, uris[lower_bound:upper_bound]))
    print(f"Added elements")

    return added_elements_package
