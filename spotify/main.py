from random import shuffle
from datetime import date
import requests
import config



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


def merge_playlist_parts(get_playlist_items_token: str, create_playlist_token: str, add_items_to_playlist_token: str,
                         playlist_part_1: str, playlist_part_2: str, number_of_songs: int = 25):

    # get songs of the playlists
    songs_part_1 = get_playlist_items(get_playlist_items_token, playlist_part_1, limit=number_of_songs)
    print(f"Get songs - part 1: {songs_part_1}")
    songs_part_2 = get_playlist_items(get_playlist_items_token, playlist_part_2, limit=number_of_songs)
    print(f"Get songs - part 2: {songs_part_1}")

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
    print(f"Create playlist: {playlist}")
    # save playlist id
    playlist_id = playlist['id']

    # fill playlist with songs
    added_elements = add_items_to_playlist(add_items_to_playlist_token, playlist_id, song_uris)
    print(f"Added elements: {added_elements}")

    return added_elements


def refresh_tokens():
    pass


def main():

    merge_playlist_parts(config.GET_PLAYLIST_ITEMS_TOKEN,
                         config.CREATE_PLAYLIST_TOKEN,
                         config.ADD_ITEMS_TO_PLAYLIST_TOKEN,
                         config.PLAYLIST_1,
                         config.PLAYLIST_2,
                         number_of_songs=config.NUMBER_OF_SONGS)


if __name__ == '__main__':
    main()
