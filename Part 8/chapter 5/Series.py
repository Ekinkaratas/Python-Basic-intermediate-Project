class Series:
    def __init__ (self,movie_name : str, seasons_number : int, genre_list : list, rating : int=0) :
        if seasons_number <= 0 :
            raise ValueError("season number must be greater than 0")
        self.set(movie_name, genre_list, seasons_number, rating)

    def set(self,movie_name, genre_list, seasons_number=1, rating=0):
        self.name = movie_name
        self.season = seasons_number
        self.genres = ",".join(genre_list)
        self.rating = rating
    
        if self.rating !=0 :
            self.rating_count = 1
        else : 
            self.rating_count = 0

    def rate(self,rating : int =0):
        if rating < 0 or rating > 5 :
           raise ValueError("raiting should be between 0 and 5")
        
        self.rating += rating
        self.rating_count += 1 

    def __str__(self):
        return f"{self.name} ({self.season} seasons) \ngenres: {self.genres} \n{'no rating' if self.rating == 0 else f'{self.rating_count} ratings, average {self.rating / self.rating_count} points'}"


def minimum_grade(rating: float, series_list: list) -> list:
    new_list = []
    for values in series_list:
        if values.rating >= rating:
            new_list.append(values)
    return new_list

def includes_genre(genre: str, series_list: list) -> list:
    new_list = []
    for values in series_list:
        if genre in values.genres:
            new_list.append(values)
    return new_list

if __name__ == "__main__":
    s1 = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
    s1.rate(5)

    s2 = Series("South Park", 24, ["Animation", "Comedy"])
    s2.rate(3)

    s3 = Series("Friends", 10, ["Romance", "Comedy"])
    s3.rate(2)

    series_list = [s1, s2, s3]

    print("a minimum grade of 4.5:")
    for series in minimum_grade(4.5, series_list):
        print(series.name)

    print()
    
    print("genre Comedy:")
    for series in includes_genre("Comedy", series_list):
        print(series.name)
