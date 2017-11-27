import configparser
import unittest

import definitions
from github_api4_client.client import Client

__author__ = "Michael Lane"
__email__ = "mikelane@gmail.com"
__copyright__ = "Copyright 2017, Michael Lane"
__license__ = "MIT"


class TestClient(unittest.TestCase):
    def setUp(self):
        config = configparser.ConfigParser()
        with open(definitions.SETTINGS_PATH, 'r') as settings_file:
            config.read_file(settings_file)
        token = config['github.com']['token']

        self.client = Client(token)

    def test_get_basic_valid_response(self):
        query = '''
        {
            viewer {
                login
            }
        }'''

        response = self.client.query(query)
        response_json = response.json()

        self.assertIn('data', response_json, 'Expected key "data" not found')
        self.assertIn('viewer', response_json['data'], 'Expected key "viewer" not found')
        self.assertIn('login', response_json['data']['viewer'], 'Expected key "login" not found')
        self.assertNotIn('error', response_json, 'Found unexpected error in response')

    def test_find_issue_id(self):
        query = '''
        {
            repository(owner:"octocat", name:"Hello-World") {
                issue(number:349) {
                    id
                }
            }
        }'''

        response = self.client.query(query)
        response_json = response.json()

        self.assertNotIn('error', response_json, 'Found unexpected error in response')
        self.assertEqual(response_json['data']['repository']['issue']['id'], 'MDU6SXNzdWUyMzEzOTE1NTE=')


if __name__ == '__main__':
    unittest.main()
