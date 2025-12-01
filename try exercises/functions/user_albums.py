def make_album(artist_name, album_title):
    album = {'artist': artist_name, 'title': album_title}
    return(album)
while True:
    #Enter artist name and album title
    print("\nEnter the artist name and album title: ")
    print("(enter 'q' to quit)")

    artist_name = input("Enter artist name: ")
    if artist_name == 'q':
        break

    album_title = input("Enter album name: ")
    if album_title == 'q':
        break