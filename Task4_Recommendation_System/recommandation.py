import pandas as pd
import difflib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load dataset
movies = pd.read_csv("movie_dataset.csv")

# Features used for recommendation
selected_features = [
    "genres",
    "keywords",
    "tagline",
    "cast",
    "director"
]

# Replace missing values
for feature in selected_features:
    movies[feature] = movies[feature].fillna("")

# Create combined features
movies["combined_features"] = (
    movies["genres"] + " " +
    movies["keywords"] + " " +
    movies["tagline"] + " " +
    movies["cast"] + " " +
    movies["director"]
)

# Convert text into vectors
vectorizer = TfidfVectorizer()
feature_vectors = vectorizer.fit_transform(movies["combined_features"])

# Calculate similarity
similarity = cosine_similarity(feature_vectors)

# List of movie titles
list_of_all_titles = movies["title"].tolist()


def recommend_movies(movie_name):

    find_close_match = difflib.get_close_matches(movie_name, list_of_all_titles)

    if len(find_close_match) == 0:
        return []

    close_match = find_close_match[0]

    index_of_the_movie = movies[
        movies.title == close_match
    ]["index"].values[0]

    similarity_score = list(enumerate(similarity[index_of_the_movie]))

    sorted_similar_movies = sorted(
        similarity_score,
        key=lambda x: x[1],
        reverse=True
    )

    recommended_movies = []

    for movie in sorted_similar_movies[1:]:
        index = movie[0]

        title = movies[
            movies["index"] == index
        ]["title"].values[0]

        recommended_movies.append(title)

        if len(recommended_movies) == 10:
            break

    return recommended_movies


# Run in terminal (optional)
if __name__ == "__main__":

    movie_name = input("Enter your favourite movie: ")

    recommendations = recommend_movies(movie_name)

    print("\nMovies suggested for you:\n")

    for i, movie in enumerate(recommendations, start=1):
        print(f"{i}. {movie}")