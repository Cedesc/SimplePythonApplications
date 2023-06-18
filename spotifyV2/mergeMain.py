from spotifyV2.logic.merging.mergePlaylists import create_merged_playlist
from spotipyRequests.SpotipyRequests import SpotipyRequests

# Docu https://developer.spotify.com/documentation/web-api
# Dashboard https://developer.spotify.com/dashboard

# todo write one line that formats the original link to the id directly below the attribute (and overwrite it)
christians_dohmaen_part_id \
    = "23BUjbevO4zQdvg4nfPqiI"  # https://open.spotify.com/playlist/23BUjbevO4zQdvg4nfPqiI?si=ac7bf20bb4a44683
robins_dohmaen_part_id \
    = "1OgD3pMv23u5EKIRTZwWby"  # https://open.spotify.com/playlist/1OgD3pMv23u5EKIRTZwWby?si=980fb4faeb4e4213

wump = "5pVmijmcJ5COlfEgJ9KM44"
tatata = "1QbpcsQMHoVPKnb9qII2XQ"
watson = "10m4SPaR1AePngKCn7jIsz"


PLAYLIST_1 = wump
PLAYLIST_2 = tatata
NUMBER_OF_SONGS = 33
PLAYLIST_3 = watson


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
