import enum


class Genre(enum.Enum):
    NOVEL = 'novel'
    COMEDY = 'comedy'


class Book:
    def __init__(self, price: float, title: str, genre: Genre):
        if not (isinstance(price, float) & isinstance(title, str) & isinstance(genre, Genre)):
            raise TypeError

        if price < 0:
            raise ValueError('Price should be positive')

        self._price = price
        self._title = title
        self._genre = genre

    @property
    def price(self) -> float:
        return self._price

    @property
    def title(self) -> str:
        return self._title

    @property
    def genre(self) -> Genre:
        return self._genre

    def __eq__(self, other):
        if not isinstance(other, Book):
            raise ValueError(f'{other} is not Book')
        return self._genre == other._genre and self._price == other._price and self._title == other._title

    def __hash__(self):
        return hash((self._title, self._price, self._genre))
