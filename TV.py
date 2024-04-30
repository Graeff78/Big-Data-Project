class TV:
    """ contains all the attributes of a TV show """
    def __init__(self, item):
        self.adult = item["adult"]
        self.backdrop = item["backdrop_path"]
        self.air_date = item["first_air_date"]
        self.genre_ids = item["genre_ids"]
        self.id = item["id"]
        self.name = item["name"]
        self.country = item["origin_country"]
        self.lang = item["original_language"]
        self.original = item["original_name"]
        self.overview = item["overview"]
        self.pop = item["popularity"]
        self.poster = item["poster_path"]
        self.voteavg = item["vote_average"]
        self.votecnt = item["vote_count"]

#help(TV)


