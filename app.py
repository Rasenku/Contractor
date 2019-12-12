from bson import ObjectId
from flask import Flask, render_template, redirect, url_for, request
from pymongo import MongoClient
import os


app = Flask(__name__)



host = os.environ.get('MONGODB_URI', 'mongodb://localhost:27017/AnimeArtStore')
client = MongoClient(host=f'{host}?retryWrites=false')
db = client.get_default_database()


animes = db.animes


@app.route('/')
def animes_ndex():
    """Homepage for what you want to search."""
    return render_template('animes_index.html', animes=animes.find())




@app.route('/animes/<anime_id>')
def animes_show(anime_id):
    """Show the info for each Anime Art."""
    anime = animes.find_one({'_id': ObjectId(anime_id)})
    return render_template('animes_show.html', anime=anime)


@app.route('/animes/new')
def animes_new():
    '''This is for a Anime Art listing'''
    return render_template('animes_new.html',anime={}, title='Add a Anime Art')

@app.route('/animes', methods=['POST'])
def animes_submit():
    ''' add new anime art to the database and redirect to that anime's page '''
    anime =  {
        'name': request.form.get('name'),
        'description': request.form.get('description'),
        'image': request.form.get('image')
    }
    anime_id = animes.insert_one(anime).inserted_id
    return redirect(url_for('animes_show', anime_id=anime_id))


@app.route('/animes/<anime_id>/edit')
def anime_edit(anime_id):
    ''' form to edit a Anime Art listing '''
    anime = animes.find_one({'_id': ObjectId(anime_id)})
    return render_template('animes_edit.html', anime=anime, title='Edit Listing')

@app.route('/animes/<anime_id>', methods=['POST'])
def animes_update(anime_id):
    ''' add updated info of an anime art to the database and redirect to that anime art's  page '''
    updated_anime = {
        'name': request.form.get('name'),
        'description': request.form.get('description'),
        'image': request.form.get('image')
    }
    animes.update_one(
        {'_id': ObjectId(anime_id)},
        {'$set': updated_anime})
    return redirect(url_for('animes_show', anime_id=anime_id))




@app.route('/animes/<anime_id>/delete', methods=['POST'])
def animes_delete(anime_id):
    ''' delete a anime art from the database, redirect to the home page '''
    animes.delete_one({'_id': ObjectId(anime_id)})
    return redirect(url_for('animes_show', anime_id=anime_id))

@app.route('/AboutAnime')
def AboutAnime():
    """Return homepage."""
    return render_template('AboutAnime.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
