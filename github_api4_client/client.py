#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""A client that queries Github's API v4"""
import json

import requests

__author__ = "Michael Lane"
__email__ = "mikelane@gmail.com"
__copyright__ = "Copyright 2017, Michael Lane"
__license__ = "MIT"


class Client:
    def __init__(self, token):
        self.token = token
        self.endpoint = 'https://api.github.com/graphql'  # Github's GraphQL endpoint
        self.headers = {'Authorization': f'Bearer {token}'}

    def query(self, query):
        assert isinstance(query, str)
        data = {'query': query}
        return requests.post(url=self.endpoint, data=json.dumps(data), headers=self.headers)


if __name__ == '__main__':
    pass
