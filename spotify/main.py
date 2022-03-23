from random import shuffle
from datetime import date
import requests



def create_playlist(access_token: str, name: str, public: bool = True, description: str = ""):
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


def get_playlist_items(access_token: str, playlist_id: str, limit: int = 25):
    response = requests.get(
        f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks?fields=items(track(id))&limit={limit}",
        headers={
            "Authorization": f"Bearer {access_token}"
        }
    )

    return response.json()


def add_items_to_playlist(access_token: str, playlist_id: str, uris: list[str]):
    response = requests.post(
        f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks",
        headers={
            "Authorization": f"Bearer {access_token}"
        },
        json={
            # "uris": ["spotify:track:4pbTElMDaHrkLOfOv8nUdC",
            #          "spotify:track:1301WleyT98MSxVHPZCA6M"]
            "uris": uris
        }
    )

    return response.json()


def extract_ids(response: dict) -> list[str]:

    result: list[str] = []

    list_of_songs: list = response['items']

    for i in range(len(list_of_songs)):
        result.append(list_of_songs[i]['track']['id'])

    return result


def arrange_elements(first_list: list[str], second_list: list[str]) -> list[str]:

    length: int = len(first_list)

    # check if the length of the lists is equal
    if length != len(second_list):
        raise Exception("lists are not the same length")

    return [first_list[i // 2] if i % 2 == 0 else second_list[i // 2] for i in range(length * 2)]


def convert_song_ids_to_uris(ids: list[str]) -> list[str]:
    return [f"spotify:track:{song_id}" for song_id in ids]


def merge_dohmaen_parts(get_playlist_items_token: str, create_playlist_token: str, add_items_to_playlist_token: str):

    my_dohmaen_part_id = "308VV4yDDA065rhU9EgrGf"  # todo
    robins_dohmaen_part_id = "3So0E5adOPpsBzcnBWe1zu"  # todo

    # get songs of the playlists
    songs_part_1 = get_playlist_items(get_playlist_items_token, my_dohmaen_part_id, limit=25)
    print(songs_part_1)  # todo
    songs_part_2 = get_playlist_items(get_playlist_items_token, robins_dohmaen_part_id, limit=25)
    print(songs_part_2)  # todo
    # todo can I get the songs of robins playlist???

    # convert to the ids
    ids_part_1: list[str] = extract_ids(songs_part_1)
    ids_part_2: list[str] = extract_ids(songs_part_2)

    # shuffle lists
    shuffle(ids_part_1)
    shuffle(ids_part_2)

    # merge lists and convert ids to uris
    merged_list: list[str] = arrange_elements(ids_part_1, ids_part_2)
    song_uris: list[str] = convert_song_ids_to_uris(merged_list)

    # create new playlist
    playlist_name: str = f"Dohmän {date.today().strftime('%d.%m.')}"
    playlist = create_playlist(create_playlist_token, playlist_name, public=True, description="")
    print(playlist)  # todo
    # save playlist id
    playlist_id = playlist['id']

    # fill playlist with songs
    added_elements = add_items_to_playlist(add_items_to_playlist_token, playlist_id, song_uris)
    print(added_elements)  # todo

    return added_elements


def main():
    # playlist = create_playlist_on_spotify(
    #     name="My Private Playlist 4",
    #     public=True,
    #     description=""
    # )
    #
    # print(f"Playlist: {playlist}")


    # me = get_me()
    # print(me)

    # songs = add_items_to_playlist()
    # print(songs)

    # songs = get_playlist_items()
    # print(songs)

    # token = "BQCrr7DwuBx7FGnjoUSIEPgvPSVUaOsSv_6oQ8IIsN6jJ-REr9_HC5QRT_-SBTvEkLeqVw3whpTUYk_GcljmWMSba_6ZfwEXFiqKDsMx5_qkK3zoFd2frQV2syTuK2iqnNWJ66CsbMnpQYIViwzXyQ9-wZ8yixwduNqy0fCpYXQQOtLweHAHYc5Xw9mOUp83u-ZW2fLfkuvNAZduhyU"
    # playlist = create_playlist(token, "Test 1", True, "Joa geht wohl")
    # print(playlist['id'])

    # https://developer.spotify.com/console/post-playlist-tracks/
    get_playlist_items_token: str = "BQDMb3MrgMqiOMFbXb4jtmoxoo9cuwtFhGP6XLMd-_swm63Fuqqu5M73aIRz10Im60Bnv3Tj6kOlOF1vcLtqKKGsVBUk9AtZ1mviX3QIsBXd_G2x_fXX1Aok6kVCqMSOeS_NgU8-26pNEJrk-f23H5N0hEBrI0mcJTL341yL1qChG0fy0yChKiBejZTOvvzjwa6ZWnvvKAse_qvIahU"

    # https://developer.spotify.com/console/post-playlists/
    create_playlist_token: str = "BQDMb3MrgMqiOMFbXb4jtmoxoo9cuwtFhGP6XLMd-_swm63Fuqqu5M73aIRz10Im60Bnv3Tj6kOlOF1vcLtqKKGsVBUk9AtZ1mviX3QIsBXd_G2x_fXX1Aok6kVCqMSOeS_NgU8-26pNEJrk-f23H5N0hEBrI0mcJTL341yL1qChG0fy0yChKiBejZTOvvzjwa6ZWnvvKAse_qvIahU"

    # https://developer.spotify.com/console/post-playlist-tracks/
    add_items_to_playlist_token: str = "BQAt-i_TEfAVUXjtwmvm1Oid7VAk6K2LdjSOGL0wHxrtYLEgiyjTW23pr9TH02p32WVjv9EBWAekiwhHKnVslGAfmofu3OnX_lnZdjT2SPvYrfc3gIlXbL_JUa4SXzJNYM3fXbCo-fpk91ZYTz4ClV_vGl2AFGRWsme5FUUKciHbQLWexEBcBr55yeeSx3ckJcS2xZUZ_OBq4z8Efw8"

    merge_dohmaen_parts(get_playlist_items_token, create_playlist_token, add_items_to_playlist_token)


if __name__ == '__main__':
    main()


# https://open.spotify.com/playlist/308VV4yDDA065rhU9EgrGf?si=f2534c275fa849d4


""" songs:  https://open.spotify.com/track/4pbTElMDaHrkLOfOv8nUdC?si=e645e1100a8e4ecb
            https://open.spotify.com/track/598B9RU1jZhObFSQJhisIa?si=20a59f76f8484ad4
            https://open.spotify.com/track/1lnbl9uZjCdiyBUHRzS7ef?si=3ac848188a8d4e65
"""
# source 1:  308VV4yDDA065rhU9EgrGf
# source 2:  3So0E5adOPpsBzcnBWe1zu
# target:  14BD51yINR0Z6mmpJsauB7









def get_artist():
    response = requests.get(
        f"https://api.spotify.com/v1/artists/cedesc3",
        headers={
            "Authorization": f"Bearer BQAgsju5CAnenrAPQmYUbbM-aDyfDAGYDlH1Gonq2AvzpbD40DLEsfV8lkw6MnKJdO4mFpcHMKiFlZetj-Jk8cinu6xnFfKBCP5mlcGNVfHtkju06AyNAT_Qrbeq9oDOSRizmQAm-8-GG3EL3ris-k9CB2XAzy1vYT2p8MiM83HD_nLkHIVIAAZF_e6Mw0UtKudrY0f3"
        }
    )
    json_resp = response.json()

    return json_resp


def get_me():
    response = requests.get(
        "https://api.spotify.com/v1/me",
        headers={
            "Authorization": f"Bearer BQAgsju5CAnenrAPQmYUbbM-aDyfDAGYDlH1Gonq2AvzpbD40DLEsfV8lkw6MnKJdO4mFpcHMKiFlZetj-Jk8cinu6xnFfKBCP5mlcGNVfHtkju06AyNAT_Qrbeq9oDOSRizmQAm-8-GG3EL3ris-k9CB2XAzy1vYT2p8MiM83HD_nLkHIVIAAZF_e6Mw0UtKudrY0f3"
        }
    )

    json_resp = response.json()

    return json_resp
