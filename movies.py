class Movie():
    """This class represents a movie """

    def __init__(self,movie_title,movie_storyline, poster_image, movie_trailer
        ,movie_rating):
        self.title = movie_title #: This is the movie title

        self.storyline = movie_storyline #: short description about the movie

        self.poster_image_url = poster_image #: url for the image file of the movie poster

        self.trailer_url = movie_trailer #: url for the video file of the movie trailer

        self.rating = movie_rating #: Movie rating

