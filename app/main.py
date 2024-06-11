from app import app
from flask import render_template
import pandas as pd
import traceback
import os

@app.route('/')
def home():
    try:
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        data_path = os.path.join(base_dir, 'data', 'reddit_posts_final.csv')
        df = pd.read_csv(data_path)
        return render_template('index.html', posts=df.to_dict(orient='records'))
    except Exception as e:
        error_message = f"An error occurred: {e}\n{traceback.format_exc()}"
        return error_message, 500

