class Movie():
    """Creates a new Movie class instance

         Attributes:
         movie_title: movie's title
         release_year: release year string of the movie
         movie_storyline: storyline of the movie
         poster_image: URL string for the movie poster image
         trailer_youtube: youtube URL string for the movie trailer.
    """
    def __init__(self,
                 movie_title,
                 release_year,
                 movie_storyline,
                 poster_image,
                 trailer_youtube):
        """Initializes Movie class with title, storyline, image and trailer."""
        self.title = movie_title + " (" + release_year + ")"
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
