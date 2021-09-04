def includeme(config):
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('get_playlist', '/get-playlist')
    config.add_route('get_song_by_title','get-playlist/{title}')