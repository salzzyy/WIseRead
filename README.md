# WiseRead

WiseRead is a book recommendation system built using Python and Flask. It provides personalized book suggestions based on a user's input, utilizing machine learning techniques such as cosine similarity for finding similar books. The app also allows users to view popular books and their details.

## Features

- **Popular Books**: Displays a list of popular books with details like title, author, rating, and image.
- **Book Recommendations**: Users can input a book title, and the system will recommend similar books based on cosine similarity.
- **Flask-based Web App**: Built with Flask, a lightweight Python web framework, to serve the application.

## Tech Stack

- **Python**: A programming language for the backend.
- **Flask**: Web framework for building the application.
- **Numpy**: For numerical operations.
- **Scikit-learn**: For machine learning and similarity scoring.
- **Pickle**: For saving and loading preprocessed data.
- **HTML/CSS**: For frontend interface.

## Setup

### Prerequisites

Make sure you have the following installed:

- Python 3.x
- pip (Python package installer)

### Install Dependencies

1. Clone the repository:

    ```bash
    git clone https://github.com/salzzyy/WIseRead.git
    cd WIseRead
    ```

2. Create a virtual environment (optional but recommended):

    ```bash
    python -m venv venv
    ```

3. Activate the virtual environment:
   - **Windows**:
     ```bash
     .\venv\Scripts\activate
     ```
   - **Mac/Linux**:
     ```bash
     source venv/bin/activate
     ```

4. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

### Running the Application

To run the application locally:

```bash
python app.py
DATASET-  https://www.kaggle.com/datasets/arash...
