import unittest
import json
from app import app


class RESTTest(unittest.TestCase):

    def setUp(self) -> None:
        self.app = app
        self.client = self.app.test_client()

        self.post_data = {
            "quote_id": 599,
            "author": "Friedrich Nietzsche, Twilight of the Idols",
            "quote": "Without music, life would be a mistake."
        }
        
        self.post_data_negative = {
            "quote_id": 1,
            "author": "Anonimus",
            "quote": "Dummy quote."
        }
        
        self.put_edit_data = {
            "quote_id": 9,
            "author": "Anonymous",
            "quote": "There are no words."
        }

        self.put_create_data = {
            "quote_id": 12,
            "author": "Groucho Marx",
            "quote": "I find television very educating."
                     "Every time somebody turns on the set, "
                     "I go into the other room and read a book."
        }

    def test_get_quotes(self):
        response = self.client.get(path='/api/v1/quotes', content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_get_quote(self):
        response = self.client.get(path='/api/v1/quotes/1', content_type='application/json')
        self.assertEqual(response.status_code, 200)
        
    def test_get_quote_negative(self):
        response = self.client.get(path='/api/v1/quotes/99999', content_type='application/json')
        self.assertEqual(response.status_code, 404)

    def test_create_quote(self):
        response = self.client.post(path='api/v1/quotes/599',
                                    data=json.dumps(self.post_data),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 201)

    def test_create_quote_negative(self):
        response = self.client.post(path='api/v1/quotes/1',
                                    data=json.dumps(self.post_data_negative),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_edit_quote(self):
        response = self.client.put(path='api/v1/quotes/9',
                                   data=json.dumps(self.put_edit_data),
                                   content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_create_put_quote(self):
        response = self.client.put(path='api/v1/quotes/12',
                                   data=json.dumps(self.put_create_data),
                                   content_type='application/json')
        self.assertEqual(response.status_code, 201)

    def test_delete_quote(self):
        response = self.client.delete(path='/api/v1/quotes/11', content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def tearDown(self) -> None:
        pass


if __name__ == '__main__':
    unittest.main()
