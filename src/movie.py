import pickle

class MovieList():
    def __init__(self):
        self.movies = {}

    def add_user(self, user_id):
        if user_id not in self.movies:
            self.movies[user_id] = set()

    def add_movies(self, user_id, movie_name):
        if user_id not in self.movies:
            self.add_user(user_id)
        self.movies[user_id].add(movie_name)

    def get_movies(self, user_id):
        return self.movies.get(user_id, [])
    
    def remove_movies(self, user_id, movie_name):
        if user_id in self.movies and movie_name in self.movies[user_id]:
            self.movies[user_id].remove(movie_name)

    def save(self, filename='movies.pkl'):
        """Save the movie tracker to a file."""
        with open(filename, 'wb') as f:
            pickle.dump(self, f)

    @classmethod
    def load(cls, filename='movies.pkl'):
        """Load the movie tracker from a file."""
        try:
            with open(filename, 'rb') as f:
                return pickle.load(f)
        except FileNotFoundError:
            return cls()  # Return a new, empty tracker if the file doesn't exist