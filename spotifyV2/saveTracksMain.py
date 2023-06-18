from logic.saveTopAndLiked.saveTopAndLikedTracks import create_top_tracks_save, create_liked_tracks_save
from spotipyRequests.SpotipyRequests import SpotipyRequests

# Docu https://developer.spotify.com/documentation/web-api
# Dashboard https://developer.spotify.com/dashboard


# Settings for saving the top tracks
TIME_RANGE = 'short_term'   # 'short_term' = 4 weeks , 'medium_term' = 6 months , 'long_term' = all time
NUMBER_OF_SONGS_TOP_TRACKS = 50


if __name__ == '__main__':
    sp_req = SpotipyRequests()

    create_liked_tracks_save(sp_req)
    create_top_tracks_save(
        sp_req,
        time_range=TIME_RANGE,
        number_of_songs=NUMBER_OF_SONGS_TOP_TRACKS
    )
