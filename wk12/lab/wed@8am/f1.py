"""
This app will allow a user to collect
and sort records (cd's)

"""
import os
import zipfile
class Record:
    def __init__(self, name, artist, num_songs, genre, release_date):
        self.name = name
        self.artist = artist
        self.num_songs = num_songs
        self.genre = genre
        self.release_date = release_date

    def save(self):
        file_name = f"{self.artist.replace(' ', '_')}_{self.name.replace(' ', '_')}.txt"
        with open(file_name, "w") as fo:
            fo.write(self.__str__().replace(", ", "\n"))
        return file_name
    def __str__(self):
        return f"Name: {self.name}, Artist: {self.artist}, Genre: {self.genre}"


class PersonalCollection:
    def __init__(self):
        self.albums = list()
    def add_album(self, album):
        if isinstance(album, Record):
            self.albums.append(album)
    def get_album_by_genre(self, genre):
        matched_albums = list()
        for album in self.albums:
            if album.genre == genre:
                matched_albums.append(album)
        return matched_albums

    def save_all(self):
        for album in self.albums:
            album.save()

    def save_as_zip(self):
        with zipfile.ZipFile("collection.zip", "w") as zfo:
            album_names = []
            for album in self.albums:
                album_name = album.save()
                zfo.write(album_name)
                album_names.append(album_name)

            for album in album_names:
                os.remove(album)



my_collection = PersonalCollection()
my_collection.add_album(Record("Dirt", "Alice in Chains", 12, "Grunge", 1992))
my_collection.add_album(Record("Test", "Singer", 10, "Pop", 2000))

for match in my_collection.get_album_by_genre("Grunge"):
    print(match)
#my_collection.save_all()
my_collection.save_as_zip()