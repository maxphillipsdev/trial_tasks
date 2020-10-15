"""Entry point for the web app."""
import os

from flask import Flask, render_template


app = Flask(__name__, template_folder='public')


@app.route('/')
def index():
    """Serve the frontend."""
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='127.0.0.1',
            port=8000,
            debug=os.getenv('DEBUG', False))
