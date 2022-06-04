from datetime import date
import spotifyAPIFunctions as sAPI


def getMonthInGerman(month_string: str) -> str:
    """Solved with a dictionary since I haven't python3.10 with pattern matching."""
    switch = {
        '01': 'Januar',
        '02': 'Februar',
        '03': 'März',
        '04': 'April',
        '05': 'Mai',
        '06': 'Juni',
        '07': 'Juli',
        '08': 'August',
        '09': 'September',
        '10': 'Oktober',
        '11': 'November',
        '12': 'Dezember',
    }
    result = switch.get(month_string)
    if result is None:
        raise IndexError
    return switch.get(month_string)


def createFavoritesSave(get_playlist_items_token: str, create_playlist_token: str, add_items_to_playlist_token: str):

    # get songs of favorites
    tracks = sAPI.get_favorite_songs(get_playlist_items_token)
    print(f"Get favorite tracks: {tracks}")

    # convert to the ids
    pass  # todo
    ids: list[str] = sAPI.extract_ids(tracks)

    # convert ids to uris
    uris: list[str] = sAPI.convert_song_ids_to_uris(ids)

    # create new playlist (moving it to the right folder isn't possible so far)
    playlist_name: str = f"{getMonthInGerman(date.today().strftime('%m'))} {date.today().strftime('%y')}"
    playlist = sAPI.create_playlist(create_playlist_token, playlist_name, public=True, description="")
    print(f"Create playlist: {playlist}")
    # save playlist id
    playlist_id = playlist['id']

    # fill playlist with songs
    added_elements = sAPI.add_items_to_playlist(add_items_to_playlist_token, playlist_id, uris)
    print(f"Added elements: {added_elements}")

    return added_elements




def main(token):
    songs_part_1 = sAPI.get_favorite_songs(token)
    print(f"Get songs - part 1: {songs_part_1}")
    print("Ende")


if __name__ == '__main__':
    # t = "BQBql9Gapnjly5lasQVLtJOMVFWd4hngKOxYfr-ROGuEi2DBTu68XP76-FNGasnr6Wi8j6Itoz5OV9wdbHLEnlBBCQt1gAO6xGJtfmNZTAaYy2-3iq6l_79vWO3LfZBYO93954GcZZuEFEDOF-LkdIMTbaPr0J9XArVdU0rOtS4mQYfmtmczWqLpvJgYOsCjwB-OPqz8jL33t_N_y2RReN2y"
    # main(t)
    # print(date.today().strftime('%m'))
    # print(getMonthInGerman(date.today().strftime('%m')))
    # print(f"{getMonthInGerman(date.today().strftime('%m'))} {date.today().strftime('%y')}")

    # from https://developer.spotify.com/console/get-playlist-tracks/
    # from https://developer.spotify.com/console/post-playlists/
    # from https://developer.spotify.com/console/post-playlist-tracks/

    t1 = 'BQCz5Pqj85a4j-KaAyRXtO3UdlEQ8zBQ8SWOrrWFgkdLYSAhYt-0KAXEoPcPJn_yebjBMkJoz8o4rPukzSTPWfy4ZLiyK6bbpY41SGOuzLdBJcLp5UC2yIDONMv-zHiQy98gkqP3t2lUZaJ7Q2AKeAthOUTxTZohO-PujMlJqHby2TrXop14a-1_9OiW4medFEhLwczKMqtiwFbWO79evIoR'
    t2 = 'BQBp8GRDHXVJYDzCG4WGpaMB0AL1TTq5i639h7BaTBho_pNy7A6P85p9bV0iIxxfdGf5t9Jr5_o8uHdYW_0uhtSXIx8WMxBNUEF6RgUJ09LglLTYLThfcaWSCknUO1oXnpr3V8YUVNRATcFVGkBHRwYePzSf2wBTTPHRdJMzQB9F81LTs3kFfeKEwjSev0Agm3-Mjqr3_D9EHWwEHTTgmdqJ'
    t3 = 'BQChZy8_lLmzB53yRBAIj4YoTr3nsfqB_ibL3ad9AG4qGng0vOwKdRGWYGrhS9P9prQcLr9aaKxhq_E3JG_ScbBm_yEIFkGYSximDO9Q2XL-g5PYW9uRtyGXXCbdnmRga015-psnvwcenIiUox464QEtMq5r4eCNVzneCsbmoHEC783kBNDVoSi4ErHXUWAVMazBIILkkiJRb32T6JzbUdFb'
    createFavoritesSave(t1, t2, t3)
