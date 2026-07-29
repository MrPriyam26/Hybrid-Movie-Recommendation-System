# 🎬 Hybrid Movie Recommendation System

A movie recommendation web application built with **Python**, **Scikit-learn**, and **Streamlit**. The system recommends movies similar to a selected title using a hybrid approach that combines **content-based similarity** with **weighted movie ratings** for more relevant recommendations.

## 🚀 Features

* 🔍 Search and select a movie
* 🎯 Get the Top 5 similar movie recommendations
* 🖼️ Display movie posters using the TMDB API
* ⭐ Show movie ratings
* 📖 Display movie overviews
* ⚡ Interactive web interface built with Streamlit

## 🛠️ Tech Stack

* Python
* Pandas
* NumPy
* Scikit-learn
* Streamlit
* TMDB API
* Pickle

## 📂 Project Structure
Hybrid-Movie-Recommendation-System/
│
├── app.py
├── movies.pkl
├── similarity.pkl
├── requirements.txt
├── README.md
└── .gitignore


## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/your-username/Hybrid-Movie-Recommendation-System.git
cd Hybrid-Movie-Recommendation-System
```

Install the required packages:

```bash
pip install -r requirements.txt
```

Create an environment variable named `TMDB_API_KEY` and set it to your TMDB API key.

Generate the similarity matrix:
python create_similarity.py


Run the application:

```bash
streamlit run app.py
```


## 📸 Screenshots

<img width="1920" height="1020" alt="HOME" src="https://github.com/user-attachments/assets/9eab6800-9d37-4de4-b8db-dde13eddcb9d" />
<img width="1920" height="1020" alt="RECOMMENDATIONS" src="https://github.com/user-attachments/assets/58e8d829-43b6-4ae1-94dc-53970f536604" />






## 🙌 Acknowledgements

* TMDB API for movie metadata and posters
* Streamlit for the interactive web application framework
