from mergeToDohmaen import merge_playlist_parts
from tokenProvider import TokenProvider

# https://developer.spotify.com/console/post-playlists/


christians_dohmaen_part_id = "23BUjbevO4zQdvg4nfPqiI"

# robins_dohmaen_part_id = "0qjisSazVU8CRtd42Fbji4"  # Robins alte Playlist: "Dohmän"
robins_dohmaen_part_id = "1OgD3pMv23u5EKIRTZwWby"   # Robins neue Playlist: "Dohmän-Teil"



PLAYLIST_1 = christians_dohmaen_part_id
PLAYLIST_2 = robins_dohmaen_part_id
NUMBER_OF_SONGS = 25


if __name__ == '__main__':

    tp = TokenProvider()
    # tp.readTokenFromTXTFile()
    tp.generateAccessToken()

    merge_playlist_parts(tp.access_token,
                         PLAYLIST_1,
                         PLAYLIST_2,
                         number_of_songs=NUMBER_OF_SONGS)
