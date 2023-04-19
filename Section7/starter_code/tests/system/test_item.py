from models.store import StoreModel
from models.user import UserModel
from models.item import ItemModel
from tests.base_test import BaseTest
import json


class ItemTest(BaseTest):
    def setUp(self):
        super(ItemTest, self).setUp() # launch setUp from BaseTest before launch setUp from here.
        # Else our new setUp will override setUp form BaseTest

        with self.app() as client:
            with self.app_context():
                UserModel('test', '1234').save_to_db()
                auth_request = client.post('/auth', data=json.dumps({'username': 'test', 'password': '1234'}),
                                           headers={'Content-Type': 'application/json'})
                auth_token = json.loads(auth_request.data)['access_token']
                self.access_token = f'JWT {auth_token}'

    def test_get_item_no_auth(self):
        with self.app() as client:
            with self.app_context():
                response = client.get('/item/test')

                self.assertEqual(response.status_code, 401) # 401 because we're not authorized

    def test_get_item_no_found(self):
        with self.app() as client:
            with self.app_context():
                response = client.get('/item/test', headers={'Authorization': self.access_token})

                self.assertEqual(response.status_code, 404)

    def test_get_item(self):
        with self.app() as client:
            with self.app_context():
                StoreModel('test').save_to_db()
                ItemModel('test', 19.99, 1).save_to_db()
                response = client.get('/item/test', headers={'Authorization': self.access_token})

                self.assertEqual(response.status_code, 200)

    def test_delete_item(self):
        with self.app() as client:
            with self.app_context():
                StoreModel('test').save_to_db()
                ItemModel('test', 19.99, 1).save_to_db()
                response = client.delete('/item/test')

                self.assertEqual(response.status_code, 200)
                self.assertDictEqual({'message': 'Item deleted'}, json.loads(response.data))

    def test_create_item(self):
        with self.app() as client:
            with self.app_context():
                StoreModel('test').save_to_db()

                response = client.post('/item/test', json={'price': 19.99, 'store_id': 1})

                self.assertEqual(response.status_code, 201)
                self.assertDictEqual({'name': 'test', 'price': 19.99}, json.loads(response.data))

    def test_create_duplicate(self):
        with self.app() as client:
            with self.app_context():
                StoreModel('test').save_to_db()
                ItemModel('test', 19.99, 1).save_to_db() # create a new item

                response = client.post('/item/test', json={'price': 19.99, 'store_id': 1}) # create a new item

                self.assertEqual(response.status_code, 400)
                self.assertDictEqual({'message': "An item with name \'test\' already exists."}, json.loads(response.data))

    def test_put_item(self):
        with self.app() as client:
            with self.app_context():
                StoreModel('test').save_to_db()

                response = client.put('/item/test', json={'price': 19.99, 'store_id': 1})

                self.assertEqual(response.status_code, 200)
                self.assertIsNotNone(ItemModel.find_by_name('test').price, 19.99)
                self.assertEqual(ItemModel.find_by_name('test').store_id, 1)
                self.assertDictEqual({'name': 'test', 'price': 19.99}, json.loads(response.data))

    def test_put_update_item(self):
        with self.app() as client:
            with self.app_context():
                StoreModel('test').save_to_db()
                ItemModel('test', 3.99, 1).save_to_db() # incorrect price to check update

                self.assertIsNotNone(ItemModel.find_by_name('test').price, 3.99)

                response = client.put('/item/test', json={'price': 19.99, 'store_id': 1})

                self.assertEqual(response.status_code, 200)
                self.assertIsNotNone(ItemModel.find_by_name('test').price, 19.99)
                self.assertEqual(ItemModel.find_by_name('test').store_id, 1)
                self.assertDictEqual({'name': 'test', 'price': 19.99}, json.loads(response.data))

    def test_item_list(self):
        with self.app() as client:
            with self.app_context():
                StoreModel('test').save_to_db()
                ItemModel('test', 19.99, 1).save_to_db()

                response = client.get('/items')

                self.assertDictEqual({'items': [{'name': 'test', 'price': 19.99}]}, json.loads(response.data))

