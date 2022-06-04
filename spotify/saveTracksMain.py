from saveTopAndLikedTracks import createTopTracksSave
from tokenProvider import TokenProvider


TIME_RANGE = 'short_term'   # 'short_term' = 4 weeks , 'medium_term' = 6 months , 'long_term' = all time
NUMBER_OF_SONGS_TOP_TRACKS = 50


if __name__ == '__main__':

    tp = TokenProvider()
    # tp.readTokensFromFile()
    tp.generateTokens()

    createTopTracksSave(tp.get_playlist_items_token,
                        tp.create_playlist_token,
                        tp.add_items_to_playlist_token,
                        time_range=TIME_RANGE,
                        number_of_songs=NUMBER_OF_SONGS_TOP_TRACKS)
