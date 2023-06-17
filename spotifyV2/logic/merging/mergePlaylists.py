from random import shuffle
from datetime import date
from spotifyV2.mapper.mapperFunctions import ids_of_tracks, convert_track_ids_to_uris


def _arrange_elements(list1: list[str], list2: list[str]) -> list[str]:
    """
    Merges two lists two one.

    Example:
        list1 = [ 1 , 2, 3 ] \n
        list2 = [ first , second , third ] \n
        result = [ 1 , first , 2 , second , 3 , third ]

    Raises:
        Exception: If the lists haven't the same length
    """
    length: int = len(list1)

    # check if the length of the lists are equal
    if length != len(list2):
        raise Exception("Lists are not the same length.")

    return [list1[i // 2] if i % 2 == 0
            else list2[i // 2]
            for i in range(length * 2)]


def _arrange_elements_for_three_playlists(list1: list[str], list2: list[str], list3: list[str]) -> list[str]:
    """
    Merges three lists two one.

    Example:
        list1 = [ 1 , 2 , 3 ] \n
        list2 = [ first , second , third ] \n
        list3 = [ one , two , three ] \n
        result = [ 1 , first , one , 2 , second , two , 3 , third , three ]

    Raises:
        Exception: If the lists haven't the same length
    """
    length: int = len(list1)

    # check if the length of the lists is equal
    if length != len(list2) or length != len(list3):
        raise Exception("Lists are not the same length.")

    return [list1[i // 3] if i % 3 == 0
            else (list2[i // 3] if i % 3 == 1
            else list3[i // 3])
            for i in range(length * 3)]


def create_merged_playlist(sp_req, playlist1: str, playlist2: str, playlist3: str = None,
                           number_of_songs: int = 25, public: bool = True, description: str = ""):
    """
    """
    # extract ids and merge the id lists
    merged_ids_list: list[str] = _merge_playlists(sp_req, playlist1, playlist2, playlist3, number_of_songs)

    # create playlist with the elements of the merged ids
    playlist_name, playlist_url = _create_playlist_with_elements(
        sp_req,
        merged_ids_list,
        playlist3 is not None,
        number_of_songs,
        public,
        description
    )

    # print name and link to the newly created playlist
    print(f"Created playlist \"{playlist_name}\" ({playlist_url})")
    return


def _merge_playlists(sp_req, playlist1: str, playlist2: str, playlist3: str,
                     number_of_songs: int) -> list[str]:
    """
    """
    # get tracks of the playlists
    tracks1 = sp_req.get_playlist_items(playlist1, limit=number_of_songs)
    print(f"LOG: Get songs - part 1: {tracks1}")
    tracks2 = sp_req.get_playlist_items(playlist2, limit=number_of_songs)
    print(f"LOG: Get songs - part 2: {tracks2}")

    # convert to the ids
    ids1: list[str] = ids_of_tracks(tracks1)
    ids2: list[str] = ids_of_tracks(tracks2)

    # shuffle lists
    shuffle(ids1)
    shuffle(ids2)

    # check if there is a third playlist
    if playlist3 is not None:
        # get tracks of third playlist
        tracks3 = sp_req.get_playlist_items(playlist3, limit=number_of_songs)
        print(f"LOG: Get songs - part 3: {tracks3}")
        # convert to the ids
        ids3: list[str] = ids_of_tracks(tracks3)
        # shuffle list
        shuffle(ids3)
        # merge all three lists
        merged_ids_list: list[str] = _arrange_elements_for_three_playlists(ids1, ids2, ids3)
    else:
        # merge both lists
        merged_ids_list: list[str] = _arrange_elements(ids1, ids2)

    return merged_ids_list


def _create_playlist_with_elements(sp_req, merged_ids_list: list[str], three_playlists: bool,
                                   number_of_songs: int, public: bool, description: str) -> tuple[str, str]:
    """
    Returns:
        Name and URL of the newly created playlist.
    """
    # convert ids to uris
    song_uris: list[str] = convert_track_ids_to_uris(merged_ids_list)

    # create new empty playlist
    playlist_name: str = f"Dohmän {date.today().strftime('%d.%m.')}"
    playlist = sp_req.create_playlist(playlist_name, public=public, description=description)
    print(f"LOG: Create playlist: {playlist}")
    # save playlist id
    playlist_id = playlist['id']

    # fill playlist with songs
    # (multiple calls of add_items_to_playlist() are necessary since only 100 items can be added at once)
    total_track_amount = (number_of_songs * 2) if three_playlists else (number_of_songs * 3)
    added_elements = []
    for i in range(((total_track_amount - 1) // 100) + 1):
        lower_bound = 100 * i
        upper_bound = (100 * i) + 100
        to_append = sp_req.add_items_to_playlist(playlist_id, song_uris[lower_bound:upper_bound])
        added_elements.append(to_append)
        print(f"LOG: Added elements: {to_append}")

    # returns the name and the URL of the newly created playlist
    return playlist['name'], playlist['external_urls']['spotify']
