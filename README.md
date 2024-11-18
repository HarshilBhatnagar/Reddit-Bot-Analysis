

# Reddit Bot Analysis

This project analyzes bot usage for Indian political issues on Reddit.
subreddit = reddit.subreddit('india')
query = 'Modi OR Congress OR BJP OR Indian Politics'

## Project Structure

- `app/`: Contains the Flask application code and the HTML file.
  - `__init__.py`: Initializes the Flask application.
  - `main.py`: Contains the main route and logic for the application.
  - `templates/`: Contains the HTML templates for the Flask application.
    - `index.html`: The main HTML template for displaying the data.

- `data/`: Contains the data files.
  - `reddit_posts.csv`: CSV file containing the collected Reddit posts.

- `notebooks/`: Contains Jupyter notebooks for different steps of the project.
  - `data_collection.ipynb`: Jupyter notebook for collecting Reddit posts.
  - `data_preprocessing.ipynb`: Jupyter notebook for preprocessing the data.
  - `bot_detection.ipynb`: Jupyter notebook for bot detection.
  - `sentiment_analysis.ipynb`: Jupyter notebook for sentiment analysis.

- `requirements.txt`: Lists the dependencies for the project.

- `runtime.txt`: Specifies the Python runtime version for Heroku.

