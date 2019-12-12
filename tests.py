from unittest import TestCase, main as unittest_main, mock
from app import app
from bson.objectid import ObjectId




sample_AnimeArt_id = ObjectId('5df18bcab9002a663a47cc76')
sample_AnimeArt = {
    'name': 'Sample Drawing',
    'description': 'Girl outside',
    'image': 'https://i.pinimg.com/564x/a3/c1/26/a3c1268580fe864c4028db7af2e04884.jpg'

}
sample_form_data = {
    'name': sample_AnimeArt['name'],
    'description': sample_AnimeArt['description'],
    'image': sample_AnimeArt['image']
}





class AnimeArtTests(TestCase):
    """Flask tests."""
    def setUp(self):
        """Stuff to do before every test."""

        # Get the Flask test client
        self.client = app.test_client()

        # Show Flask errors that happen during tests
        app.config['TESTING'] = True

    def test_index(self):
        result = self.client.get('/')
        self.assertEqual(result.status, '200 OK')

    def test_new(self):
        result = self.client.get('/animes/new')
        self.assertEqual(result.status, '200 OK')

    @mock.patch('pymongo.collection.Collection.find_one')
    def test_show_animes(self, mock_find):
        """Test showing a single playlist."""
        mock_find.return_value = sample_AnimeArt

        result = self.client.get(f'/animes/{sample_AnimeArt_id}')
        self.assertEqual(result.status, '200 OK')

    @mock.patch('pymongo.collection.Collection.update_one')
    def test_update_animes(self, mock_update):
        result = self.client.post(f'/animes/{sample_AnimeArt_id}', data=sample_form_data)

        self.assertEqual(result.status, '302 FOUND')
        mock_update.assert_called_with({'_id': sample_AnimeArt_id}, {'$set': sample_AnimeArt})

    @mock.patch('pymongo.collection.Collection.delete_one')
    def test_delete_piece(self, mock_delete):
        form_data = {'_method': 'DELETE'}
        result = self.client.post(f'/animes/{sample_AnimeArt_id}/delete', data=form_data)
        self.assertEqual(result.status, '302 FOUND')
        mock_delete.assert_called_with({'_id': sample_AnimeArt_id})

if __name__ == '__main__':
    unittest_main()
