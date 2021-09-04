from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
    Float
)

from .meta import Base


class Playlist(Base):
    __tablename__ = 'playlist'
    id = Column(Text, primary_key=True)
    title = Column(Text)
    danceability = Column(Float)
    energy = Column(Float)
    key = Column(Integer)
    loudness = Column(Float)
    mode = Column(Integer)
    acousticness = Column(Float)
    instrumentalness = Column(Float)
    liveness = Column(Float)
    valence = Column(Float)
    tempo = Column(Float)
    duration_ms = Column(Integer)
    time_signature = Column(Integer)
    num_bars= Column(Integer)
    num_sections= Column(Integer)
    num_segments= Column(Integer)
    class_name = Column('class', Integer)
    start_rating = Column(Integer)
