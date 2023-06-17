from random import shuffle
from datetime import date


def _arrangeElements(list1: list[str], list2: list[str]) -> list[str]:
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


def _arrangeElementsForThreePlaylists(list1: list[str], list2: list[str], list3: list[str]) -> list[str]:  # todo test
    """
    Merges three lists two one.

    Example:
        list1 = [ 1 , 2 , 3 ] \n
        list2 = [ first , second , third ] \n
        list3 = [ eins , zwei , drei ] \n
        result = [ 1 , first , eins , 2 , second , zwei , 3 , third , drei ]

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


def createMergedPlaylist(apiReq, playlist1: str, playlist2: str, playlist3: str = None,
                         numberOfSongs: int = 25, public: bool = True, description: str = ""):
    """
    """
    # extract ids and merge the id lists
    mergedIdsList: list[str] = _mergePlaylists(apiReq, playlist1, playlist2, playlist3, numberOfSongs)

    # create playlist with the elements of the merged ids
    return _createPlaylistWithElements(apiReq, mergedIdsList, playlist3 is not None, numberOfSongs, public, description)


def _mergePlaylists(apiReq, playlist1: str, playlist2: str, playlist3: str,
                    numberOfSongs: int) -> list[str]:
    """
    """
    # get tracks of the playlists
    tracks1 = apiReq.getPlaylistItems(playlist1, limit=numberOfSongs)
    print(f"LOG: Get songs - part 1: {tracks1}")
    tracks2 = apiReq.getPlaylistItems(playlist2, limit=numberOfSongs)
    print(f"LOG: Get songs - part 2: {tracks2}")

    # convert to the ids
    ids1: list[str] = idsOfTracks(tracks1)
    ids2: list[str] = idsOfTracks(tracks2)

    # shuffle lists
    shuffle(ids1)
    shuffle(ids2)

    # check if there is a third playlist
    if playlist3 is not None:
        # get tracks of third playlist
        tracks3 = apiReq.getPlaylistItems(playlist3, limit=numberOfSongs)
        print(f"LOG: Get songs - part 3: {tracks3}")
        # convert to the ids
        ids3: list[str] = idsOfTracks(tracks3)
        # shuffle list
        shuffle(ids3)
        # merge all three lists
        mergedIdsList: list[str] = _arrangeElementsForThreePlaylists(ids1, ids2, ids3)
    else:
        # merge both lists
        mergedIdsList: list[str] = _arrangeElements(ids1, ids2)

    return mergedIdsList


def _createPlaylistWithElements(apiReq, mergedIdsList: list[str], threePlaylists: bool,
                                numberOfSongs: int, public: bool, description: str) -> list:
    """
    """
    # convert ids to uris
    songUris: list[str] = convertTrackIdsToUris(mergedIdsList)

    # create new empty playlist
    playlistName: str = f"Dohmän {date.today().strftime('%d.%m.')}"
    playlist = apiReq.createPlaylist(playlistName, public=public, description=description)
    print(f"LOG: Create playlist: {playlist}")
    # save playlist id
    playlistId = playlist['id']

    # fill playlist with songs
    # (multiple calls of add_items_to_playlist() are necessary since only 100 items can be added at once)
    totalTrackAmount = (numberOfSongs * 2) if threePlaylists else (numberOfSongs * 3)
    addedElements = []
    for i in range(((totalTrackAmount - 1) // 100) + 1):
        lowerBound = 100 * i
        upperBound = (100 * i) + 100
        toAppend = apiReq.addItemsToPlaylist(playlistId, songUris[lowerBound:upperBound])
        addedElements.append(toAppend)
        print(f"LOG: Added elements: {toAppend}")

    return addedElements


# Mapper functions  todo delete if mapper can be imported

def idsOfTracks(tracks: dict) -> list[str]:
    """
    """
    return list(map(lambda track: track['track']['id'], tracks['items']))


def idsOfTopTracks(tracks: dict) -> list[str]:  # todo really needed ?
    """
    """
    return list(map(lambda track: track['id'], tracks['items']))


def convertTrackIdsToUris(ids: list[str]) -> list[str]:
    """
    """
    return [f"spotify (legacy):track:{song_id}" for song_id in ids]


def getTotalAmountOfTracksInLikedTracks(response: dict) -> int:
    """
    Currently the result is lower than the actual amount since I have
    liked songs that aren't in Spotify, like 'Motiva' by 'Bladesa'.
    """
    return response['total']
