class Band:
    # albums = [] -> why is not here
    def __init__(self, name):
        self.name = name
        self.albums = []  # but instead is here

    def add_album(self, album):
        if album in self.albums:  # fix to album without .name
            return f"Band {self.name} already has {album.name} in their library."

        self.albums.append(album)
        return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self, album_name: str):
        for album in self.albums:
            if album.name == album_name:
                if album.published:
                    return "Album has been published. It cannot be removed."

                self.albums.remove(album_name)
                return f"Album {album_name} has been removed."  # why not album.name

        return f"Album {album_name} is not found." # why not self.name

    def details(self):
        i = f" Band {self.name}\n"
        for album in self.albums:
            i += album.details() + "\n"

        return i.strip()