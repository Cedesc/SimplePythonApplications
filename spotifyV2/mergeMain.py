from spotifyV2.logic.merging.mergePlaylists import create_merged_playlist
from spotipyRequests.SpotipyRequests import SpotipyRequests

# Docu https://developer.spotify.com/documentation/web-api
# Dashboard https://developer.spotify.com/dashboard

# For quick startup, read the README file
# todo add readme for quick setup after merge and with all things to take care (number of songs, links, third song, ...)
#  - add three env variables: SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET, USER_NAME

# todo write one line that formats the original link to the id directly below the attribute (and overwrite it)
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
    sp_reqs = SpotipyRequests()

    # create merged playlist
    create_merged_playlist(
        sp_reqs,
        PLAYLIST_1,
        PLAYLIST_2,
        playlist3=PLAYLIST_3,
        number_of_songs=NUMBER_OF_SONGS,
        public=True,
        description=""
    )
