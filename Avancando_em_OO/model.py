from abc import ABC
from dataclasses import dataclass,field
from collections.abc import MutableSequence


class MutablePlaylist(MutableSequence):
    pass


@dataclass()
class Shows:
    __name : str
    __year : int
    __likes : int = field(default=0)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name.title()

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, year):
        self.__year = year

    def like(self):
        self.__likes += 1

    @property
    def likes(self):
        return self.__likes

    def __str__(self):
        return f'Name: {self.__name} - Year: {self.__year} - Likes: {self.__likes}'


class Movie(Shows):

    def __init__(self, name, year, duration):
        super().__init__(name, year)
        self.__duration = duration

    @property
    def duration(self):
        return self.__duration

    @duration.setter
    def duration(self, duration):
        self.__duration = duration

    def __str__(self):
        return f'Name: {self.name} - Year: {self.year} - Likes: {self.likes} - Duration: {self.__duration}'


class Serie(Shows):

    def __init__(self, name, year, seasons):
        super(Serie, self).__init__(name, year)
        self.__seasons = seasons

    @property
    def seasons(self):
        return self.__seasons

    @seasons.setter
    def seasons(self, seasons):
        self.__seasons = seasons

    def __str__(self):
        return f'Name: {self.name} - Year: {self.year} - Likes: {self.likes} - Seasons: {self.__seasons}'


# Herdando o comportamento de uma lista para ser iteravel
class Playlist():
    def __init__(self, name, shows):
        self.__name = name.title()
        self.__shows = shows

    def __getitem__(self, item):
        return self.__shows[item]

    def __len__(self):
        return len(self.__shows)

    @property
    def getShows(self):
        return self.__shows

    # @property
    # def size(self):
    #     return len(self.__shows)


# movies = MutablePlaylist()

avengers = Movie("avengers", 2017, 130)
avengers.like()
avengers.like()
peakyBlinders = Serie("peaky blinders", 2018, 5)
peakyBlinders.like()
matrix = Movie("matrix", 2003, 153)
matrix.like()
matrix.like()
matrix.like()
matrix.like()
quennsGambit = Serie("The Queen's Gambit", 2020, 1)
quennsGambit.like()
quennsGambit.like()
playlist = Playlist("Favoritos", [avengers, matrix, peakyBlinders, quennsGambit])
for programa in playlist:
    print(programa)
print(len(playlist))
