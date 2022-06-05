from random import shuffle
from datetime import date
import spotifyAPIFunctions as sAPI


def arrange_elements(first_list: list[str], second_list: list[str]) -> list[str]:

    length: int = len(first_list)

    # check if the length of the lists is equal
    if length != len(second_list):
        raise Exception("lists are not the same length")

    return [first_list[i // 2] if i % 2 == 0 else second_list[i // 2] for i in range(length * 2)]


def merge_playlist_parts(access_token: str,
                         playlist_part_1: str, playlist_part_2: str, number_of_songs: int = 25):

    # get songs of the playlists
    songs_part_1 = sAPI.get_playlist_items(access_token, playlist_part_1, limit=number_of_songs)
    print(f"Get songs - part 1: {songs_part_1}")
    songs_part_2 = sAPI.get_playlist_items(access_token, playlist_part_2, limit=number_of_songs)
    print(f"Get songs - part 2: {songs_part_1}")

    # convert to the ids
    ids_part_1: list[str] = sAPI.extract_ids_get_playlist_items(songs_part_1)
    ids_part_2: list[str] = sAPI.extract_ids_get_playlist_items(songs_part_2)

    # shuffle lists
    shuffle(ids_part_1)
    shuffle(ids_part_2)

    # merge lists and convert ids to uris
    merged_list: list[str] = arrange_elements(ids_part_1, ids_part_2)
    song_uris: list[str] = sAPI.convert_song_ids_to_uris(merged_list)

    # create new playlist
    playlist_name: str = f"Dohmän {date.today().strftime('%d.%m.')}"
    playlist = sAPI.create_playlist(access_token, playlist_name, public=True, description="")
    print(f"Create playlist: {playlist}")
    # save playlist id
    playlist_id = playlist['id']

    # fill playlist with songs
    added_elements = sAPI.add_items_to_playlist(access_token, playlist_id, song_uris)
    print(f"Added elements: {added_elements}")

    return added_elements
