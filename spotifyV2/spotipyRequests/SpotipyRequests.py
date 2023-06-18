import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Spotify API https://developer.spotify.com/documentation/web-api/reference/get-an-album


class SpotipyRequests:

    def __init__(self):
        client_id = os.getenv("CLIENT_ID")
        client_secret = os.getenv("CLIENT_SECRET")
        redirect_uri = 'http://localhost:8080/callback'
        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
            client_id=client_id,
            client_secret=client_secret,
            redirect_uri=redirect_uri,
            scope='playlist-modify-private playlist-modify-public user-library-read'
        ))
        self.user_name = os.getenv("USER_NAME")

    # todo With a playlist of >100 elements, not all elements can be retrieved.
    #  Implement the solutions of calculateNewlyAddedTracks._track_is_in_playlist or
    #  mergePlaylists._create_playlist_with_elements and look at the other methods for similar problems
    def get_playlist_items(self, playlist_id: str, limit: int = 100, offset: int = 0):
        return self.sp.playlist_items(
            playlist_id=playlist_id,
            fields=None,
            limit=limit,
            offset=offset,
            market=None,
            additional_types=("track", "episode")
        )

    def create_playlist(self, name: str, public: bool = True, description: str = ""):
        return self.sp.user_playlist_create(
            user=self.user_name,
            name=name,
            public=public,
            collaborative=False,
            description=description
        )

    def add_items_to_playlist(self, playlist_id: str, uris: list[str]):
        return self.sp.playlist_add_items( playlist_id=playlist_id, items=uris, position=None)

    def get_number_of_tracks_in_playlist(self, playlist_id):
        return self.sp.playlist(playlist_id=playlist_id)['tracks']['total']

    def get_top_songs(self, time_range: str = 'short_term', limit: int = 50, offset: int = 0):
        # return self.sp.current_user_top_tracks(limit=limit, offset=offset, time_range=time_range)
        return self.sp.current_user_top_tracks()
        # todo look in docu and find the needed scope for this request
        #  https://developer.spotify.com/documentation/web-api/reference/get-audio-features

    def get_liked_songs(self, limit: int = 50, offset: int = 0):
        return self.sp.current_user_saved_tracks(limit=limit, offset=offset, market=None)

    def get_total_track_amount_of_liked_tracks(self, response: dict):
        raise Exception("Not yet implemented")
