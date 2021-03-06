from pyramid.renderers import render_to_response
from pyramid.view import view_config
import pyramid.httpexceptions as exc
from requests import Response
from sqlalchemy.exc import SQLAlchemyError

from ..models import Playlist
MIN_RATING = 1
MAX_RATING = 5
def result_dict(data_set):
    if isinstance(data_set, list):
        data_set = [dict(zip(row.keys(), row)) for row in data_set]

    result_list = []
    for data in data_set:
        data_details = {}
        for column, value in data.items():
            data_details[column] = value
        result_list.append(data_details)
    return result_list


@view_config(route_name='get_playlist', request_method='GET')
def get_playlist(request):
    try:
        result= request.dbsession.query(Playlist).\
            with_entities(Playlist.id, Playlist.title, Playlist.danceability,
                        Playlist.energy,Playlist.key,Playlist.loudness,
                        Playlist.mode,Playlist.acousticness,Playlist.instrumentalness,
                        Playlist.liveness,Playlist.valence,Playlist.tempo,
                        Playlist.duration_ms,Playlist.time_signature,Playlist.num_bars,
                        Playlist.num_sections,Playlist.num_segments,Playlist.class_name).all()
    except SQLAlchemyError as e:
        raise exc.HTTPInternalServerError()
    except Exception as e:
        raise exc.HTTPBadRequest()
    else:
        return render_to_response('vivpro_assignment:templates/playlist.jinja2',
                              {"result":result_dict(result)}, request=request)


@view_config(route_name='get_song_by_title', request_method='GET')
def get_song_by_title(request):
    try:
        result= request.dbsession.query(Playlist).\
            with_entities(Playlist.id, Playlist.title, Playlist.danceability,
                        Playlist.energy,Playlist.key,Playlist.loudness,
                        Playlist.mode,Playlist.acousticness,Playlist.instrumentalness,
                        Playlist.liveness,Playlist.valence,Playlist.tempo,
                        Playlist.duration_ms,Playlist.time_signature,Playlist.num_bars,
                        Playlist.num_sections,Playlist.num_segments,Playlist.class_name,
                          Playlist.start_rating).\
            filter(Playlist.title==request.matchdict["title"]).all()
    except SQLAlchemyError as e:
        raise exc.HTTPInternalServerError()
    except Exception as e:
        raise exc.HTTPBadRequest()
    else:
        return render_to_response('vivpro_assignment:templates/playlist.jinja2',
                              {"result":result_dict(result)}, request=request)


@view_config(route_name='add_rating', request_method='PUT')
def add_rating(request):
    try:
        if not isinstance(request.json_body["star_rating"], int) or \
                not MIN_RATING <= request.json_body["star_rating"] <= MAX_RATING:
            raise exc.HTTPBadRequest()
        request.dbsession.query(Playlist).\
            filter(Playlist.title == request.json_body["title"]).\
            update({"start_rating": request.json_body["star_rating"]})
        request.dbsession.flush()
    except SQLAlchemyError as e:
        raise exc.HTTPInternalServerError()
    except Exception as e:
        raise exc.HTTPBadRequest()
    else:
        return exc.HTTPFound(location='http://localhost:6543/get-playlist/'+request.json_body["title"])