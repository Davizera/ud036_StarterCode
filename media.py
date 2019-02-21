import webbrowser
class Movie():
    def __init__(self,title,movie_storyline,poster_img,trailer_ytb):
        self.title  =   title
        self.storyline  =   movie_storyline
        self.poster_image_url   =   poster_img
        self.trailer_youtube_url    =   trailer_ytb
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
    
    def show_img(self):
        webbrowser.open(self.poster_image_url)

print(Movie.show_trailer.__module__,Movie.show_trailer.__name__)