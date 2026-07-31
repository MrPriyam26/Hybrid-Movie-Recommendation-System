import numpy as np
import pandas as pd
import ast
import pickle

from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

print("Loading datasets...")

movies = pd.read_csv("datasets/tmdb_5000_movies.csv")
credits = pd.read_csv("datasets/tmdb_5000_credits.csv")

print("Merging datasets...")

movies = movies.merge(credits, on="title")

movies = movies[
    [
        "movie_id",
        "title",
        "overview",
        "genres",
        "keywords",
        "cast",
        "crew",
        "vote_average",
        "vote_count",
        "popularity",
    ]
]

movies.dropna(inplace=True)
movies.drop_duplicates(inplace=True)


def convert(text):
    L = []
    for i in ast.literal_eval(text):
        L.append(i["name"])
    return L


def convert_cast(text):
    L = []
    counter = 0

    for i in ast.literal_eval(text):
        if counter != 5:
            L.append(i["name"])
            counter += 1
        else:
            break

    return L


def fetch_director(text):
    L = []

    for i in ast.literal_eval(text):
        if i["job"] == "Director":
            L.append(i["name"])
            break

    return L


def convert_keywords(text):
    L = []

    for i in ast.literal_eval(text):
        L.append(i["name"])

    return L


def collapse(L):
    L1 = []

    for i in L:
        L1.append(i.replace(" ", ""))

    return L1


ps = PorterStemmer()


def stem(text):
    y = []

    for i in text.split():
        y.append(ps.stem(i))

    return " ".join(y)


print("Processing features...")

movies["genres"] = movies["genres"].apply(convert)
movies["keywords"] = movies["keywords"].apply(convert_keywords)
movies["cast"] = movies["cast"].apply(convert_cast)
movies["director"] = movies["crew"].apply(fetch_director)

movies["genres"] = movies["genres"].apply(collapse)
movies["keywords"] = movies["keywords"].apply(collapse)
movies["cast"] = movies["cast"].apply(collapse)
movies["director"] = movies["director"].apply(collapse)

movies["overview"] = movies["overview"].apply(lambda x: x.split())

movies["tags"] = movies.apply(
    lambda row: row["overview"]
    + row["genres"]
    + row["keywords"]
    + row["cast"]
    + row["director"],
    axis=1,
)

new_df = movies[
    [
        "movie_id",
        "title",
        "tags",
        "vote_average",
        "vote_count",
        "popularity",
    ]
]

new_df["tags"] = new_df["tags"].apply(lambda x: " ".join(x))
new_df["tags"] = new_df["tags"].apply(lambda x: x.lower())
new_df["tags"] = new_df["tags"].apply(stem)

print("Creating vectors...")

cv = CountVectorizer(
    max_features=5000,
    stop_words="english",
)

vectors = cv.fit_transform(new_df["tags"]).toarray()

print("Calculating cosine similarity...")

similarity = cosine_similarity(vectors)

print("Saving files...")

pickle.dump(new_df, open("movies.pkl", "wb"))
pickle.dump(similarity, open("similarity.pkl", "wb"))

print("\nDone!")
print("movies.pkl saved successfully.")
print("similarity.pkl saved successfully.")