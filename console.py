import pdb
from models.album import Album
from models.artist import Artist

import repositories.album_repository as album_repository
import repositories.artist_repository as artist_repository

album_repository.delete_all()
artist_repository.delete_all()

artist1 = Artist("Michael Jackson")
artist_repository.save(artist1)

artist2 = Artist("Nightwish")
artist_repository.save(artist2)

album1 = Album("Ghosts", "Pop", artist1)
album_repository.save(album1)

album2 = Album("Thriller", "Pop", artist1)
album_repository.save(album2)


# artist_repository.select(artist1.id)

# TEST for artist by id
# artist_by_id = artist_repository.select(artist1.id)
# print(artist_by_id.__dict__)

# TEST for select all artists
# artists_list = artist_repository.select_all()

# for artist in artists_list:
#     print(artist.__dict__)

# TEST for select all albums
# album_list = album_repository.select_all()

# for album in album_list:
#     print(album.__dict__)
#     print(album.artist.__dict__)

# TEST for album by id
# album_by_id = album_repository.select(album1.id)
# print(album_by_id.__dict__)
# print(album_by_id.artist.__dict__)

# TEST for delete
# album_repository.delete(2)

# TEST for selecting all albums by a specific artist

albums_by_artist = album_repository.select_all_by_artist(artist1)

for album in albums_by_artist:
    print(album.__dict__)
    print(album.artist.__dict__)

# print(artist1.__dict__)
# print(album1.__dict__)

# pdb.set_trace()