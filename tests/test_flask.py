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

    def test_get_quotes(self):
        response = self.client.get(path='/api/v1/quotes', content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_get_quote(self):
        response = self.client.get(path='/api/v1/quotes/1', content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_create_quote(self):
        response = self.client.post(path='api/v1/quotes/599',
                                    data=json.dumps(self.post_data),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 201)

    def test_edit_quote(self):
        # TODO! Add test
        expected = 201
        self.assertEqual(expected, 201)

    def test_delete_quote(self):
        # TODO! Add test
        expected = 200
        self.assertEqual(expected, 200)

    def tearDown(self) -> None:
        pass


if __name__ == '__main__':
    unittest.main()
