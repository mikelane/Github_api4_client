# Imports
import unittest

__author__ = "Michael Lane"
__email__ = "mikelane@gmail.com"
__copyright__ = "Copyright 2017, Michael Lane"
__license__ = "MIT"


class TestClient(unittest.TestCase):
    def setUp(self):
        client = Client(token)

    def test_get_basic_valid_response(self):
        query = '''
        {
            viewer {
                login
            }
        }'''

        response = client.query(query)

        self.assertIn('data', response, 'Expected key "data" not found')
        self.assertIn('viewer', response['data'], 'Expected key "viewer" not found')
        self.assertIn('login', response['data']['viewer'], 'Expected key "login" not found')
        self.assertNotIn('error', response, 'Found unexpected error in response')

    def test_find_issue_id(self):
        query = '''
        {
            repository(owner:"octocat", name:"Hello-World") {
                issue(number:349) {
                    id
                }
            }
        }'''

        response = client.query(query)

        self.assertNotIn('error', response, 'Found unexpected error in response')
        self.assertEqual(response['data']['repository']['issue']['id'], 'MDU6SXNzdWUyMzEzOTE1NTE=')


if __name__ == '__main__':
    pass