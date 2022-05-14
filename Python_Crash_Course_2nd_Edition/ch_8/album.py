def make_album(artist, title, song_numbers=None):
    album = {"artist": artist, "title": title}
    if song_numbers:
        album['song_numbers'] = song_numbers
    return album

musician = make_album('산울림', '산울림 5집', song_numbers=13)
print(musician)

musician = make_album('서태지', '산울림 1집')
print(musician)

musician = make_album('Psy', '싸이 1집')
print(musician)