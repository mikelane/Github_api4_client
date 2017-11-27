#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import configparser
from pprint import pprint

import definitions
from github_api4_client.client import Client

__author__ = "Michael Lane"
__email__ = "mikelane@gmail.com"
__copyright__ = "Copyright 2017, Michael Lane"
__license__ = "MIT"

parser = argparse.ArgumentParser(description='''This script allows you to query Github's GraphQL API and to
introspect the result.''')
parser.add_argument('query', help='The filename of the query.')
args = parser.parse_args()

if __name__ == '__main__':
    config = configparser.ConfigParser()
    with open(definitions.SETTINGS_PATH, 'r') as settings_file:
        config.read_file(settings_file)
    token = config['github.com']['token']

    client = Client(token)

    with open(args.query, 'r') as query_file:
        query = query_file.read()

    response = client.query(query)
    response_json = response.json()
    pprint(response_json, compact=True)
