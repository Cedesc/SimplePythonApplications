from spotifyV2.logic.calculateNewlyAdded.calculateNewlyAddedTracks import get_percentage_of_truly_new_tracks
from spotipyRequests.SpotipyRequests import SpotipyRequests

# Docu https://developer.spotify.com/documentation/web-api
# Dashboard https://developer.spotify.com/dashboard


new_playlist = "0SIloxUdG344oDiIbLtJKg"
old_playlists = [
    "38gQ00jyC5bs1sll5PVYCi",
    "0ksBuAHs1AE9OtRQTksJ62",
    "7rL7cPOPJxLUYm7nrWRwXP",
    "6m4bhGtAOAy4NvyChbpHaS",
    "1iR6gomo3Z17GBs4UyISJM"
]


NEW_PLAYLIST = new_playlist
OLD_PLAYLISTS = old_playlists


if __name__ == '__main__':
    # create instance of SpotipyRequests
    sp_reqs = SpotipyRequests()

    # calculate percentage of truly new songs
    percentage = get_percentage_of_truly_new_tracks(
        sp_reqs,
        NEW_PLAYLIST,
        OLD_PLAYLISTS
    )

    print(f"The percentage of truly new songs is {percentage}")
