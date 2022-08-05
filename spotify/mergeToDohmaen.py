from random import shuffle
from datetime import date
import spotifyAPIFunctions as sAPI


def arrange_elements(first_list: list[str], second_list: list[str]) -> list[str]:

    length: int = len(first_list)

    # check if the length of the lists is equal
    if length != len(second_list):
        raise Exception("Lists are not the same length.")

    return [first_list[i // 2] if i % 2 == 0 else second_list[i // 2] for i in range(length * 2)]


def arrange_elements_3_playlists(first_list: list[str], second_list: list[str], third_list: list[str]) -> list[str]:

    length: int = len(first_list)

    # check if the length of the lists is equal
    if length != len(second_list) or length != len(third_list):
        raise Exception("Lists are not the same length.")

    return [first_list[i // 3] if i % 3 == 0 else
            (second_list[i // 3] if i % 3 == 1 else third_list[i // 3])
            for i in range(length * 3)]


def merge_playlist_parts(access_token: str,
                         playlist_part_1: str, playlist_part_2: str, playlist_part_3: str = None,
                         number_of_songs: int = 25):

    # get songs of the playlists
    songs_part_1 = sAPI.get_playlist_items(access_token, playlist_part_1, limit=number_of_songs)
    print(f"Get songs - part 1: {songs_part_1}")
    songs_part_2 = sAPI.get_playlist_items(access_token, playlist_part_2, limit=number_of_songs)
    print(f"Get songs - part 2: {songs_part_2}")

    # convert to the ids
    ids_part_1: list[str] = sAPI.extract_ids_get_playlist_items(songs_part_1)
    ids_part_2: list[str] = sAPI.extract_ids_get_playlist_items(songs_part_2)

    # shuffle lists
    shuffle(ids_part_1)
    shuffle(ids_part_2)

    # check if there is a third playlist
    if playlist_part_3 is None:
        # for 2 playlists
        # merge lists
        merged_list: list[str] = arrange_elements(ids_part_1, ids_part_2)
    else:
        # for 3 playlists
        songs_part_3 = sAPI.get_playlist_items(access_token, playlist_part_3, limit=number_of_songs)
        print(f"Get songs - part 3: {songs_part_3}")
        ids_part_3: list[str] = sAPI.extract_ids_get_playlist_items(songs_part_3)
        shuffle(ids_part_3)
        # merge lists
        merged_list: list[str] = arrange_elements_3_playlists(ids_part_1, ids_part_2, ids_part_3)

    # convert ids to uris
    song_uris: list[str] = sAPI.convert_song_ids_to_uris(merged_list)

    # create new playlist
    playlist_name: str = f"Dohmän {date.today().strftime('%d.%m.')}"
    playlist = sAPI.create_playlist(access_token, playlist_name, public=True, description="")
    print(f"Create playlist: {playlist}")
    # save playlist id
    playlist_id = playlist['id']

    # fill playlist with songs
    # (multiple calls of add_items_to_playlist() are necessary since only 100 items can be added at once)
    total_track_amount = (number_of_songs * 2) if playlist_part_3 is None else (number_of_songs * 3)
    added_elements = []
    for i in range(((total_track_amount - 1) // 100) + 1):
        lower_bound = 100 * i
        upper_bound = (100 * i) + 100
        to_append = sAPI.add_items_to_playlist(access_token, playlist_id, song_uris[lower_bound:upper_bound])
        added_elements.append(to_append)
        print(f"Added elements: {to_append}")

    return added_elements
