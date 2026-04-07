from datetime import datetime

class Message:
    def __init__(self, user, text, time_str):
        self.user = user
        self.text = text
        self.time = datetime.strptime(time_str, '%H:%M')

    def __str__(self):
        return f"[{self.time.strftime('%H:%M')}] {self.user}: {self.text}"

    def __len__(self):
        return len(self.text)

    def __gt__(self, other):
        return self.time < other.time  # старіше = менший час



messages = [
    Message("Viktor", "Привіт!", "10:23"),
    Message("Anna", "Як справи?", "10:25"),
    Message("Oleg", "Все добре", "10:20")
]


print("До сортування:")
for msg in messages:
    print(msg)

messages.sort()

print("\nПісля сортування:")
for msg in messages:
    print(msg)



from typing import List

class Song:
    def __init__(self, name:str, author:str):
        self._name = name
        self._author = author

    def __eq__(self, other):
        if isinstance(other, Song):
            return self._name == other._name and self._author == other._author
        return False

    def __str__(self):
        return f"{self._name} - {self._author}"

class Playlist:
    def __init__(self, songs:List[Song]):
        self._songs = songs

    def __len__(self):
        return len(self._songs)

    def __contains__(self, item):
        return item in self._songs

    def __iter__(self):
        return iter(self._songs)

    def add_song(self, song:Song):
        self._songs.append(song)

    def remove_song(self, song:Song):
        if song in self._songs:
            self._songs.remove(song)




song1 = Song("Imagen", "John Lennon")
song2 = Song("Bohemian Rhapsody", "Queen")
song3 = Song("Imagen", "John Lennon")
song4 = Song("Twisted transister", "Korn")
playlist = Playlist([song1, song2, song3])

playlist.add_song(song4)
playlist.remove_song("Imagen")

for song in playlist:
    print(song)
print(song1 in playlist)



class Cart:
    def __init__(self, items=None):
        self.items = items if items else []
        self.total = sum(item[1] for item in self.items)

    def __str__(self):
        result = "Товари в кошику:\n"
        for name, price in self.items:
            result += f"{name} - {price} грн\n"
        result += f"Загальна сума: {self.total} грн"
        return result

    def __len__(self):
        return len(self.items)

    def __add__(self, other):
        new_items = self.items + other.items
        return Cart(new_items)


cart1 = Cart([("Телефон", 10000), ("Навушники", 2000)])
cart2 = Cart([("Мишка", 500), ("Клавіатура", 1500)])

print("Кількість товарів в cart1:", len(cart1))
print("Кількість товарів в cart2:", len(cart2))

print(cart1)

print(cart2)

cart3 = cart1 + cart2

print("Кількість товарів:", len(cart3))
print(cart3)
