from flask import Flask, render_template, request
import pickle
import numpy as np

# Load the dataset from the pickle file
popular_df = pickle.load(open("popular.pkl", "rb"))
pt = pickle.load(open("pt.pkl", "rb"))
books = pickle.load(open("books.pkl", "rb"))
similarity_score = pickle.load(open("similarity_score.pkl", "rb"))


# Initialize the Flask web server
app = Flask(__name__)


@app.route("/")
def index():
    return render_template(
        "index.html",
        book_name=list(popular_df["Book-Title"].values),
        author=list(popular_df["Book-Author"].values),
        image=list(popular_df["Image-URL-M"].values),
        votes=list(popular_df["book_rating_count"].values),
        rating=list(popular_df["avg_ratings"].values),
    )


@app.route("/recommended_books", methods=["POST"])
def recommend():
    user_input = request.form.get("user_input")
    
    # Check if user_input exists in pt.index
    index_array = np.where(pt.index == user_input)[0]
    if len(index_array) == 0:
        return render_template("recommend.html", error="Book not found. Please enter a valid book title.")

    index = index_array[0]  # Safe to access

    similar_items = sorted(
        list(enumerate(similarity_score[index])), key=lambda x: x[1], reverse=True
    )[1:9]

    data = []
    for i in similar_items:
        item = []
        temp_df = books[books["Book-Title"] == pt.index[i[0]]]
        item.extend(list(temp_df.drop_duplicates("Book-Title")["Book-Title"].values))
        item.extend(list(temp_df.drop_duplicates("Book-Title")["Book-Author"].values))
        item.extend(list(temp_df.drop_duplicates("Book-Title")["Image-URL-M"].values))

        data.append(item)

    return render_template("recommend.html", data=data)

@app.route("/recommend")
def recommend_ui():
    return render_template("recommend.html")


if __name__ == "__main__":
    app.run(debug=True)
