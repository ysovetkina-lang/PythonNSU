print("Введите плей-лист папы:")
songs = [input() for _ in range(5)]

print("Плей-лист мамы:")
for song in reversed(songs):
    print(song)