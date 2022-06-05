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


def createLikedTracksSave(get_playlist_items_token: str, create_playlist_token: str, add_items_to_playlist_token: str):
    """Saves the currently liked tracks.
    The maximum value for the 'limit' of 'get_liked_songs()' is 50, but since I have more than 50 liked songs, the
    function has to be called multiple times."""

    # get songs of favorites
    # (saved in the list 'track_packages' instead of 'tracks' because of the maximum limit of 50)
    track_packages = [sAPI.get_liked_songs(get_playlist_items_token, limit=50, offset=0)]
    # get amount of liked songs
    total_track_amount: int = sAPI.get_total_track_amount_of_liked_tracks(track_packages[0])
    # necessary additional calls of get_like_songs()
    for i in range((total_track_amount-1) // 50):
        track_packages.append(sAPI.get_liked_songs(get_playlist_items_token, limit=50, offset=(i+1)*50))
    print(f"Get liked tracks")

    # convert to the ids
    # (multiple calls of extract_ids_get_playlist_items() are necessary because the tracks aren't all in one variable)
    ids: list[str] = []
    for package in track_packages:
        ids += sAPI.extract_ids_get_playlist_items(package)

    # convert ids to uris
    uris: list[str] = sAPI.convert_song_ids_to_uris(ids)

    # create new playlist (moving it to the right folder isn't possible so far)
    playlist_name: str = f"Liked Tracks {getMonthInGerman(date.today().strftime('%m'))} {date.today().strftime('%y')}"
    playlist = sAPI.create_playlist(create_playlist_token, playlist_name, public=True, description="")
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
            sAPI.add_items_to_playlist(add_items_to_playlist_token, playlist_id, uris[lower_bound:upper_bound]))
    print(f"Added elements")

    return added_elements_package


if __name__ == '__main__':

    t1 = 'BQBvIhWbsi3RybMyyFkZKY3cbZBHrUqN19As1pDqxkZclf5Sh8CSpcj9oqQQhN967p5i1gu1vGFZ-6lPKciOo68anTYnFk9Y3l2t3GfV1xbPGrj4Ye7mxgFep9pN1vS_GP6J__CyVw8ft00E2LD61IYmJs9VJK18StSeNPTuaYr6N9bIKdDSLIbBdWC8Mz9zlLxJY3kfboUpRBS-cKZTD7Hx'
    t2 = 'BQACiUU0o8H4X_sJ6ilgm-55nCFgbDTkSFk4iBf_13cKOLvBxYt9vIsFfgPK6-PClSxQsJaO5PBhWeNGTbllUjFFAjkfR2wxZsoyaH-Y0sKbv3evQNYPwjX3vdCLyUOOc0GTu1AAr2lesE7CylQDDL_24pTgfNBsOBJng55SkP_QzuCrEHYifU1FXA0B0Ys-chzlGCqr0fFKFoBbpsiCQyX7'
    t3 = 'BQDImxaRXAAEVEqnSTEld4WkKcTNBJDj5kea7JfkuQZ5ZZKf3ApGHZZvBdu5Fd1W2sBOaiNiK96J9kO6dJzHScPl4MUIzbSmCribSsrtiG1NUfIzEu3TC9psXgJKbudv80u8DcHZN-aeuJWvE3PjZ-1nXhWeS_Ujn2GSm47JFicQd-wv_99a1EVtCivPbmSJ8ENZJkqDcNWGevAY5boNi8QT'
    createLikedTracksSave(t1, t2, t3)
