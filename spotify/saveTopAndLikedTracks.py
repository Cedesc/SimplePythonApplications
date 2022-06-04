from datetime import date
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


def createTopTracksSave(get_playlist_items_token: str, create_playlist_token: str, add_items_to_playlist_token: str,
                        time_range: str = 'short_term', number_of_songs: int = 50):
    """Saves the top tracks of the last 4 weeks."""

    # get songs of favorites
    tracks = sAPI.get_top_songs(get_playlist_items_token, time_range=time_range, limit=number_of_songs)
    # print(f"Get top tracks: {tracks}")
    print(f"Get top tracks")

    # convert to the ids
    ids: list[str] = sAPI.extract_ids_get_top_tracks(tracks)

    # convert ids to uris
    uris: list[str] = sAPI.convert_song_ids_to_uris(ids)

    # create new playlist (moving it to the right folder isn't possible so far)
    playlist_name: str = f"Top Tracks {getMonthInGerman(date.today().strftime('%m'))} {date.today().strftime('%y')}"
    playlist = sAPI.create_playlist(create_playlist_token, playlist_name, public=True, description="")
    # print(f"Create playlist: {playlist}")
    print(f"Create playlist")
    # save playlist id
    playlist_id = playlist['id']

    # fill playlist with songs
    added_elements = sAPI.add_items_to_playlist(add_items_to_playlist_token, playlist_id, uris)
    # print(f"Added elements: {added_elements}")
    print(f"Added elements")

    return added_elements
