from sqlalchemy import Column, String, Integer, Date, Numeric, ForeignKey, Table, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

# base class for declarative models
Base = declarative_base()

# Artist model
class Artist(Base):
    __tablename__ = 'artist'

    id: int = Column(Integer, primary_key=True)
    real_name: str = Column(String(255))
    stage_name: str = Column(String(255), nullable=False, unique=True)
    music_genre: str = Column(String(255))
    country_of_origin: str = Column(String(255))
    email: str = Column(String(255), unique=True)
    instagram_handle: str = Column(String(30), unique=True)

    # Relationships
    albums = relationship("Album", back_populates="artist", cascade="all, delete-orphan")
    events = relationship("Event", secondary="artist_event", back_populates="artists")
    services = relationship("Service", secondary="artist_service", back_populates="artists")

    def __repr__(self):
        return f"<Artist(stage_name='{self.stage_name}', real_name='{self.real_name}')>"


# Album model
class Album(Base):
    __tablename__ = 'album'

    id: int = Column(Integer, primary_key=True)
    title: str = Column(String(255), nullable=False)
    release_date: Date = Column(Date)
    artist_id: int = Column(Integer, ForeignKey('artist.id', ondelete='CASCADE'), nullable=False)

    # Relationships
    artist = relationship("Artist", back_populates="albums")
    songs = relationship("Song", back_populates="album", cascade="all, delete-orphan")
    studios = relationship("Studio", secondary="album_studio", back_populates="albums")

    def __repr__(self):
        return f"<Album(title='{self.title}', artist_id={self.artist_id})>"

# Song model
class Song(Base):
    __tablename__ = 'song'

    id: int = Column(Integer, primary_key=True)
    title: str = Column(String(255), nullable=False)
    duration: int = Column(Integer)
    album_id: int = Column(Integer, ForeignKey('album.id', ondelete='CASCADE'), nullable=False)

    # Relationships
    album = relationship("Album", back_populates="songs")
    producers = relationship("Producer", secondary="song_producer", back_populates="songs")
    songwriters = relationship("Songwriter", secondary="songwriter_song", back_populates="songs")

    def __repr__(self):
        return f"<Song(title='{self.title}', album_id={self.album_id})>"

# Songwriter model
class Songwriter(Base):
    __tablename__ = 'songwriter'

    id: int = Column(Integer, primary_key=True)
    name: str = Column(String(255), nullable=False)
    country_of_origin: str = Column(String(255))
    music_genre: str = Column(String(255))

    # Relationships
    songs = relationship("Song", secondary="songwriter_song", back_populates="songwriters")

    def __repr__(self):
        return f"<Songwriter(name='{self.name}')>"

# Producer model
class Producer(Base):
    __tablename__ = 'producer'

    id: int = Column(Integer, primary_key=True)
    name: str = Column(String(255), nullable=False)
    specialty: str = Column(String(255))

    # Relationships
    songs = relationship("Song", secondary="song_producer", back_populates="producers")

    def __repr__(self):
        return f"<Producer(name='{self.name}')>"

# Studio model
class Studio(Base):
    __tablename__ = 'studio'

    id: int = Column(Integer, primary_key=True)
    name: str = Column(String(255), nullable=False)
    address: str = Column(String)

    # Relationships
    albums = relationship("Album", secondary="album_studio", back_populates="studios")

    def __repr__(self):
        return f"<Studio(name='{self.name}')>"

# Event model
class Event(Base):
    __tablename__ = 'event'

    id: int = Column(Integer, primary_key=True)
    name: str = Column(String, nullable=False)
    event_date: Date = Column(Date)
    location: str = Column(String(255), nullable=False)
    address: str = Column(String)

    # Relationships
    artists = relationship("Artist", secondary="artist_event", back_populates="events")

    def __repr__(self):
        return f"<Event(name='{self.name}', location='{self.location}')>"

# Service model
class Service(Base):
    __tablename__ = 'service'

    id: int = Column(Integer, primary_key=True)
    name: str = Column(String(255), nullable=False)
    description: str = Column(String)
    price: float = Column(Numeric(10,2), nullable=False)

    # Relationships
    artists = relationship("Artist", secondary="artist_service", back_populates="services")

    def __repr__(self):
        return f"<Service(name='{self.name}', price={self.price})>"

# Association tables
song_producer = Table('song_producer', Base.metadata,
    Column('song_id', Integer, ForeignKey('song.id', ondelete='CASCADE'), primary_key=True),
    Column('producer_id', Integer, ForeignKey('producer.id', ondelete='SET NULL'), primary_key=True)
)

album_studio = Table('album_studio', Base.metadata,
    Column('album_id', Integer, ForeignKey('album.id', ondelete='CASCADE'), primary_key=True),
    Column('studio_id', Integer, ForeignKey('studio.id', ondelete='SET NULL'), primary_key=True)
)

artist_event = Table('artist_event', Base.metadata,
    Column('artist_id', Integer, ForeignKey('artist.id'), primary_key=True),
    Column('event_id', Integer, ForeignKey('event.id'), primary_key=True)
)

songwriter_song = Table('songwriter_song', Base.metadata,
    Column('songwriter_id', Integer, ForeignKey('songwriter.id'), primary_key=True),
    Column('song_id', Integer, ForeignKey('song.id'), primary_key=True),
    Column('role', String)
)

artist_service = Table('artist_service', Base.metadata,
    Column('artist_id', Integer, ForeignKey('artist.id'), primary_key=True),
    Column('service_id', Integer, ForeignKey('service.id'), primary_key=True)
)
