"Biblioteka filmów i seriali"



class Movie:
    def __init__(self, title, year, genree, vievs):
        self.title = title
        self.year = year
        self.genree = genree
        self.vievs = vievs

        self.current_vievs = vievs
    def play(self, viev=1):
        self.current_vievs += viev
    def show(self):
        return f'{self.title} {self.year}'
    def get_movie():
        for i in Movie():
            i.append(movies)
    
class Serial(Movie):
    def __init__(self,episode, season, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.episode = episode
        self.season = season
    def show(self):
        return f'{self.title} E{self.episode}S{self.season}'
        
    def play(self, viev=1):
        self.current_vievs += viev


movie1 = Movie(title="The Shawshank Redemption", year="1994", genree="Drama", vievs=100)
movie2 = Movie(title="Raiders of the Lost Ark", year="1981", genree="Adventure", vievs=200)
movie3 = Movie(title="Christmas Vacation", year="1989", genree="Comedy", vievs=150)
movie4 = Movie(title="Alien", year="1979", genree="Horror", vievs=130)
movie5 = Movie(title="Forrest Gump", year="1994", genree="Drama", vievs=100)
movie6 = Serial(title="Breaking Bad", year="2008", episode="01", season="01" , genree="Drama", vievs=1)
movie7 = Serial(title="Band of Brothers", year="2001", episode="02", season= "02", genree="War", vievs=2)
movie8 = Serial(title="BoJack Horseman", year="2014", episode="03", season= "03", genree="Horror", vievs=3)
movie9 = Serial(title="Twin Peaks", year="1990", episode="04", season= "01", genree="Thriller", vievs=5)

shows = [movie1, movie2, movie3, movie4, movie5, movie6, movie7, movie8, movie9]
movies = []
series = []



movie1.play()
movie6.play()
print(movie1.show())
print(movie7.show())
print(movie1.current_vievs)
print(movie6.current_vievs)