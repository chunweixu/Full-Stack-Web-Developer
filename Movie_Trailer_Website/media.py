import webbrowser

class Movie():
	'''
	This class store movie related information
	'''

	def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
		'''
		Construct a new 'Movie' object
		: param movie_title: the title of movie
		: param movie_storyline: the storyline of movie
		: param poster_image: the image url of movie
		: param trailer_youtube: the trailer youtube url of movie
		: return: returns nothing
		'''
		self.title = movie_title
		self.storyline = movie_storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube
		

	def show_trailer(self):
		'''
		Show trailer in the webbrowser
		'''
		webbrowser.open(self.trailer_youtube_url)