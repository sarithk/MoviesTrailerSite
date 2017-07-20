import fresh_tomatoes
import media

# Create movie instances of Movie class.
# Arguments are passing title, year, storyline, image and trailer youtube url.
cast_away = media.Movie("Cast Away", "2000",
                        "Chuck, a top international manager for FedEx, \
                        and Kelly, a Ph.D. student, are in love and heading \
                        towards marriage. Then Chuck's plane to Malaysia \
                        ditches at sea during a terrible storm. He's the only \
                        survivor, and he washes up on a tiny island with \
                        nothing but some flotsam and jetsam from the \
                        aircraft's cargo.",
                        "https://upload.wikimedia.org/wikipedia/en/a/a7/Cast_away_film_poster.jpg",  # noqa
                        "https://www.youtube.com/watch?v=mlyukwSk66o")

ice_age = media.Movie("Ice Age", "2002",
                      "With the impending ice age almost upon them, a \
                      mismatched trio of prehistoric critters – Manny the \
                      woolly mammoth, Diego the saber-toothed tiger and Sid \
                      the giant sloth – find an orphaned infant and decide to \
                      return it to its human parents. Along the way, the \
                      unlikely allies become friends but, when enemies \
                      attack, their quest takes on far nobler aims.",
                      "https://upload.wikimedia.org/wikipedia/en/3/3c/Ice_Age_%282002_film%29_poster.jpg",  # noqa
                      "https://www.youtube.com/watch?v=5utbt2Ycenw")

nacho_libre = media.Movie("Nacho Libre", "2006",
                          "Nacho Libre is loosely based on the story of Fray \
                          Tormenta (\"Friar Storm\"), aka Rev. Sergio \
                          Gutierrez Benitez, a real-life Mexican Catholic \
                          priest who had a 23-year career as a masked \
                          luchador. He competed in order to support the \
                          orphanage he directed.",
                          "https://upload.wikimedia.org/wikipedia/en/3/35/Nachopost.jpg",  # noqa
                          "https://www.youtube.com/watch?v=wptRqr6Ma_E")

kung_fu_panda = media.Movie("Kung Fu Panda", "2008",
                            "When the Valley of Peace is threatened, lazy Po \
                            the panda discovers his destiny as the \"chosen \
                            one\" and trains to become a kung fu hero, but \
                            transforming the unsleek slacker into a brave \
                            warrior won't be easy. It's up to Master Shifu \
                            and the Furious Five -- Tigress, Crane, Mantis, \
                            Viper and Monkey -- to give it a try.",
                            "https://upload.wikimedia.org/wikipedia/en/7/76/Kungfupanda.jpg",  # noqa
                            "https://www.youtube.com/watch?v=hUMaIR5Ubd4")

up = media.Movie("Up", "2009",
                 "Carl Fredricksen spent his entire life dreaming of \
                 exploring the globe and experiencing life to its fullest. \
                 But at age 78, life seems to have passed him by, until a \
                 twist of fate gives him a new lease on life.",
                 "https://upload.wikimedia.org/wikipedia/en/0/05/Up_%282009_film%29.jpg",  # noqa
                 "https://www.youtube.com/watch?v=BDCSncUZxvs")

the_martian = media.Movie("The Martian", "2015",
                          "During a manned mission to Mars, Astronaut Mark \
                          Watney is presumed dead after a fierce storm and \
                          left behind by his crew. But Watney has survived \
                          and finds himself stranded and alone on the hostile \
                          planet. With only meager supplies, he must draw \
                          upon his ingenuity, wit and spirit to subsist and \
                          find a way to signal to Earth that he is alive.",
                          "https://upload.wikimedia.org/wikipedia/en/c/cd/The_Martian_film_poster.jpg",  # noqa
                          "https://www.youtube.com/watch?v=XQnYm5MG1x0")

# Add movie instances to movies array.
movies = [cast_away, ice_age, nacho_libre, kung_fu_panda, up, the_martian]

# Call open_movies_page function of fresh_tomatoes module.
fresh_tomatoes.open_movies_page(movies)
