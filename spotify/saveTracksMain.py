from saveTopAndLikedTracks import createTopTracksSave, createLikedTracksSave
from tokenProvider import TokenProvider

# Settings for saving the top tracks
TIME_RANGE = 'short_term'   # 'short_term' = 4 weeks , 'medium_term' = 6 months , 'long_term' = all time
NUMBER_OF_SONGS_TOP_TRACKS = 50


if __name__ == '__main__':

    tp = TokenProvider()
    # tp.readTokenFromTXTFile()
    tp.generateAccessToken()

    createLikedTracksSave(tp.access_token)
    createTopTracksSave(tp.access_token, time_range=TIME_RANGE, number_of_songs=NUMBER_OF_SONGS_TOP_TRACKS)
