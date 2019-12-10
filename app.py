from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

@app.route('/')
def index():
    """Return homepage."""
    return render_template('index.html')


@app.route('/anime')
def anime():
    """Return homepage."""
    return render_template('anime.html')


@app.route('/AboutAnime')
def AboutAnime():
    """Return homepage."""
    return render_template('AboutAnime.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
