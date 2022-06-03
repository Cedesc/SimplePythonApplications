from mergeToDohmaen import merge_playlist_parts
import tokenProvider as tP


christians_dohmaen_part_id = "23BUjbevO4zQdvg4nfPqiI"
robins_dohmaen_part_id = "1OgD3pMv23u5EKIRTZwWby"


PLAYLIST_1 = christians_dohmaen_part_id
PLAYLIST_2 = robins_dohmaen_part_id

NUMBER_OF_SONGS = 25



if __name__ == '__main__':

    merge_playlist_parts(tP.GET_PLAYLIST_ITEMS_TOKEN,
                         tP.CREATE_PLAYLIST_TOKEN,
                         tP.ADD_ITEMS_TO_PLAYLIST_TOKEN,
                         PLAYLIST_1,
                         PLAYLIST_2,
                         number_of_songs=NUMBER_OF_SONGS)
