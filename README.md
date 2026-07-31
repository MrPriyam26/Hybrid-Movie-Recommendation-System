# 🎬 Hybrid Movie Recommendation System

A **Hybrid Movie Recommendation System** built with **Python**, **Machine Learning**, and **Streamlit** that recommends movies similar to a selected title. The recommendation engine combines **content-based similarity** with a **weighted IMDb-style rating** to provide more relevant and higher-quality recommendations.

---

## 📌 Features

* 🎥 Recommend movies similar to a selected movie
* 🧠 Hybrid recommendation algorithm

  * Content-Based Filtering using movie metadata
  * Weighted IMDb-style Rating
* ⭐ Displays movie ratings
* 🖼️ Fetches movie posters using the TMDB API
* 📖 Displays movie overview/description
* 🔍 Search movies using an interactive dropdown
* 🌐 Interactive web interface built with Streamlit

---

## 🛠️ Tech Stack

* **Programming Language:** Python
* **Frontend:** Streamlit
* **Libraries:**

  * Pandas
  * NumPy
  * Scikit-learn
  * NLTK
  * Requests
* **API:** TMDB (The Movie Database)

---

## 🧠 Recommendation Algorithm

This project uses a **Hybrid Recommendation System** consisting of two stages.

### 1️⃣ Content-Based Filtering

Movies are compared using the following features:

* Overview
* Genres
* Keywords
* Cast
* Director

These features are combined into a single **tags** column.

The tags are then processed using:

* Text Cleaning
* Porter Stemming
* CountVectorizer
* Cosine Similarity

---

### 2️⃣ Weighted Rating

Instead of recommending movies only based on similarity, the system also considers movie quality using:

* Vote Average
* Vote Count

The weighted rating is normalized and combined with cosine similarity.

Final Score:

```
Final Score =
0.7 × Similarity Score
+
0.3 × Normalized Weighted Rating
```

This helps prioritize both **similar** and **high-quality** movies.

---

## 📂 Project Structure

```
Movie-Recommendation-System/
│
├── app.py
├── create_similarity.py
├── movies.pkl
├── requirements.txt
├── README.md
├── .gitignore
│
├── datasets/
│   ├── tmdb_5000_movies.csv
│   └── tmdb_5000_credits.csv
│
└── screenshots/
```

> **Note:** `similarity.pkl` is not included because it exceeds GitHub's file size limit.

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/Movie-Recommendation-System.git

cd Movie-Recommendation-System
```

---

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 3. Generate the similarity matrix

```bash
python create_similarity.py
```

This creates:

* `movies.pkl`
* `similarity.pkl`

---

### 4. Add your TMDB API Key

Open **app.py**

Replace

```python
API_KEY = "YOUR_TMDB_API_KEY"
```

with your own TMDB API key.

You can get a free API key from:

https://developer.themoviedb.org/

---

### 5. Run the application

```bash
streamlit run app.py
```

---

## 📸 Screenshots

### Home Page

<img width="1920" height="1020" alt="HOME" src="https://github.com/user-attachments/assets/9eab6800-9d37-4de4-b8db-dde13eddcb9d" />

### Recommendations

<img width="1920" height="1020" alt="RECOMMENDATIONS" src="https://github.com/user-attachments/assets/58e8d829-43b6-4ae1-94dc-53970f536604" />

## 📊 Dataset

Dataset used:

**TMDB 5000 Movie Dataset**

Files:

* tmdb_5000_movies.csv
* tmdb_5000_credits.csv

---

## 🚀 Future Improvements

* 🎞️ Movie trailers
* ❤️ Favorite movies
* 👤 User authentication
* 🎭 Filter recommendations by genre
* 📅 Release year filter
* 🌙 Dark mode
* ☁️ Cloud deployment
* 🤖 Collaborative Filtering
* 🧠 Deep Learning-based recommendation system

---

## 👨‍💻 Author

**Shwet Priyam**

* Computer Science Engineering Student
* Passionate about AI, Machine Learning, and Data Science

---

## ⭐ Support

If you found this project helpful, consider giving it a ⭐ on GitHub.


