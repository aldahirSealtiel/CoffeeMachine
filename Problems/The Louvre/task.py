class Painting:
    museum = "Louvre"

    def __init__(self, title, painter, year_of_creation):
        self.title = title
        self.painter = painter
        self.year_of_creation = year_of_creation


my_painting = Painting(input(), input(), input())
print('"{0}" by {1} ({2}) hangs in the {3}.'.format(my_painting.title, my_painting.painter,
                                                    my_painting.year_of_creation, Painting.museum))
