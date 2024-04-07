from imdb import IMDb

class GetRating:
    def __init__(self, title):
        self.title = title
        self.ia = IMDb()

    def get_rating(self):
        try:
            search_results = self.ia.search_movie(self.title)
            
            if search_results:
                movie = self.ia.get_movie(search_results[0].movieID)
                return movie.data['rating']
            else:
                print("No search results found for the movie.")
        except Exception as e:
            print(f"An error occurred: {e}")

        print("Try again with a valid combination of title and release year")
        return None
