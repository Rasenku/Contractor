from bson import ObjectId
from flask import Flask, render_template, redirect, url_for, request
from pymongo import MongoClient
import os


app = Flask(__name__)



host = os.environ.get('MONGODB_URI', 'mongodb://localhost:27017/AnimeArtStore')
client = MongoClient(host=f'{host}?retryWrites=false')
db = client.get_default_database()


anime = db.anime


@app.route('/')
def index():
    """Homepage for what you want to search."""
    return render_template('index.html', anime=anime.find())


@app.route('/anime/<anime_id>')
def anime_show(anime_id):
    """Return homepage."""
    AnimeArt = anime.find_one({'_id': ObjectId(AnimeArt_id)})
    return render_template('anime_show.html', anime=anime)


@app.route('/anime/new')
def anime_new():
    '''This is for a listing'''
    return render_template('anime_new.html',anime={}, title='Add a Anime Art')



@app.route('/AboutAnime')
def AboutAnime():
    """Return homepage."""
    return render_template('AboutAnime.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
