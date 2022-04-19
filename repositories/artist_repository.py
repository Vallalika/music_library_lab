from db.run_sql import run_sql

from models.artist import Artist
from models.album import Album


def save(artist):
    sql = "INSERT INTO artists (name) VALUES (%s) RETURNING *"
    values = [artist.name]
    result = run_sql(sql, values)
    id = result[0]['id']
    artist.id = id
    return artist

def delete_all():
    sql = "DELETE FROM artists"
    run_sql(sql)

def select_all():
    artists = []

    sql = "SELECT * FROM artists"
    results = run_sql(sql)

    for result in results:
        artist = Artist(result['name'], result['id'] )
        artists.append(artist)
    return artists

def select(id):
    artist = None
    sql = "SELECT * FROM artists WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        artist = Artist(result['name'], result['id'] )
    return artist

def update(artist):
    sql = "UPDATE artists SET name = (%s) WHERE id = %s"
    values = [artist.name, artist.id]
    run_sql(sql, values)

def delete(artist):
    sql = "DELETE FROM artists WHERE id = %s"
    values = [artist.id]
    run_sql(sql, values)