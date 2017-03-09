import media
import fresh_tomatoes

# define the list instance of movie
avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1489037869449&di=cde4fd4ac4c45648b1031a7ed16e2503&imgtype=0&src=http%3A%2F%2Fimg2-ak.lst.fm%2Fi%2Fu%2F300x300%2Fc25f35ebbacc4920975b04a472f3f6c9.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")
	
transformer = media.Movie("Transformer",
	                      "Transformers: The Last Knight",
	                      "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1488988756927&di=93160e236bb484c7637cfccd4f2740d7&imgtype=0&src=http%3A%2F%2Ftvj.5law.cn%2Ftv-Uploads%2Fvod%2F2016-07-30%2F579c2a4c8a50b.jpg",
	                      "https://www.youtube.com/watch?v=153G7QEBK1I")

kong = media.Movie("Kong",
	               "Kong: Skull Island",
	               "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1488994552874&di=f31a17bd67e35a88fb1d29cecf253418&imgtype=0&src=http%3A%2F%2Fcdn.iciba.com%2Fnews%2F2016%2F0126%2F20160126110632204.jpg",
	               "https://www.youtube.com/watch?v=x8qPsAYQKuA")

movies = [avatar, transformer, kong]

# call function show the list of movies in the website 
fresh_tomatoes.open_movies_page(movies)
