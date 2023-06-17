from apiRequests.ApiRequestHandler import ApiRequestHandler
from credentials.AuthenticationManager import AuthenticationManager
from logic.mergePlaylists import createMergedPlaylist

# Docu https://developer.spotify.com/documentation/web-api
# Dashboard https://developer.spotify.com/dashboard


christians_dohmaen_part_id = "23BUjbevO4zQdvg4nfPqiI"
robins_dohmaen_part_id = "1OgD3pMv23u5EKIRTZwWby"   # Robins neue Playlist: "Dohmän-Teil [Robin]"

PLAYLIST_1 = christians_dohmaen_part_id
PLAYLIST_2 = robins_dohmaen_part_id
NUMBER_OF_SONGS = 25
PLAYLIST_3 = None


if __name__ == '__main__':  # todo doesnt work because of missing user authorization
    # create access token
    token: str = AuthenticationManager().accessToken

    # create ApiRequestHandler
    apiReqs = ApiRequestHandler(token)

    # create merged playlist
    createMergedPlaylist(
        apiReqs,
        PLAYLIST_1,
        PLAYLIST_2,
        playlist3=PLAYLIST_3,
        numberOfSongs=NUMBER_OF_SONGS,
        public=True,
        description=""
    )
