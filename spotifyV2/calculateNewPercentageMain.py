from spotifyV2.logic.calculateNewlyAdded.calculateNewlyAddedTracks import get_percentage_of_truly_new_tracks
from spotipyRequests.SpotipyRequests import SpotipyRequests

# Docu https://developer.spotify.com/documentation/web-api
# Dashboard https://developer.spotify.com/dashboard


new_playlist = "2oTgILV5TT4gnxeaS8aKIm"
old_playlists = [
    "2ep6habZRalXyYSos9YvCA",
    "23BUjbevO4zQdvg4nfPqiI"
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
