class Point:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def set_coord(self, x, y):
        self.__x = x
        self.__y = y

    def get_coord(self):
        return self.__x, self.__y


pg = Point(5, 10)
pg.__x = 300
pg.__y = "mag"
pg.set_coord(100, 555)
# print(pg.__x, pg.__y)

print(pg.get_coord())
