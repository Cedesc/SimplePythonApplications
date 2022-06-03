
# tokens.txt file should include the 3 tokens from the following links exactly in this sequence
# from https://developer.spotify.com/console/get-playlist-tracks/
# from https://developer.spotify.com/console/post-playlists/
# from https://developer.spotify.com/console/post-playlist-tracks/
with open('tokens.txt', "r") as file:
    lines = file.read().split("\n")
    GET_PLAYLIST_ITEMS_TOKEN: str = lines[0]
    CREATE_PLAYLIST_TOKEN: str = lines[1]
    ADD_ITEMS_TO_PLAYLIST_TOKEN: str = lines[2]
