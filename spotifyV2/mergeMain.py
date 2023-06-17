from logic.mergePlaylists import createMergedPlaylist
from spotipyRequests.SpotipyRequests import SpotipyRequests

# Docu https://developer.spotify.com/documentation/web-api
# Dashboard https://developer.spotify.com/dashboard


christians_dohmaen_part_id \
    = "23BUjbevO4zQdvg4nfPqiI"  # https://open.spotify.com/playlist/23BUjbevO4zQdvg4nfPqiI?si=ac7bf20bb4a44683
robins_dohmaen_part_id \
    = "1OgD3pMv23u5EKIRTZwWby"  # https://open.spotify.com/playlist/1OgD3pMv23u5EKIRTZwWby?si=980fb4faeb4e4213


PLAYLIST_1 = christians_dohmaen_part_id
PLAYLIST_2 = robins_dohmaen_part_id
NUMBER_OF_SONGS = 25
PLAYLIST_3 = None


if __name__ == '__main__':
    # create instance of SpotipyRequests
    spReqs = SpotipyRequests()

    # create merged playlist
    createMergedPlaylist(
        spReqs,
        PLAYLIST_1,
        PLAYLIST_2,
        playlist3=PLAYLIST_3,
        numberOfSongs=NUMBER_OF_SONGS,
        public=True,
        description=""
    )

# todo migrate saveTopAndLikedTracks and SaveTracksMainLegacy
