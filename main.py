#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import collections
import configparser

import pandas as pd

import definitions
from github_api4_client.client import Client

__author__ = "Michael Lane"
__email__ = "mikelane@gmail.com"
__copyright__ = "Copyright 2017, Michael Lane"
__license__ = "MIT"

if __name__ == '__main__':
    config = configparser.ConfigParser()
    with open(definitions.SETTINGS_PATH, 'r') as settings_file:
        config.read_file(settings_file)
    token = config['github.com']['token']

    client = Client(token)

    # Get the first 100 pull requests
    query = '''
{
    repository(owner: "ramda", name: "ramda") {
        pullRequests(first: 100) {
            edges {
                node {
                    number
                    mergedAt
                }
                cursor
            }
            pageInfo {
                hasNextPage
                endCursor
            }
        }
    }
}'''

    response = client.query(query).json()

    edges = response['data']['repository']['pullRequests']['edges']

    data = collections.defaultdict(int)
    for edge in edges:
        date = pd.to_datetime(edge['node']['mergedAt'])
        if date:
            data[(date.year, date.week)] += 1

    # Get all the remaining pull requests
    while response['data']['repository']['pullRequests']['pageInfo']['hasNextPage']:
        cursor = response['data']['repository']['pullRequests']['pageInfo']['endCursor']
        query = f'''
{{
    repository(owner: "ramda", name: "ramda") {{
        pullRequests(first: 100, after: "{cursor}") {{
            edges {{
                node {{
                    number
                    mergedAt
                }}
                cursor
            }}
            pageInfo {{
                hasNextPage
                endCursor
            }}
        }}
    }}
}}
'''
        response = client.query(query).json()
        edges = response['data']['repository']['pullRequests']['edges']

        for edge in edges:
            date = pd.to_datetime(edge['node']['mergedAt'])
            if date:
                data[(date.year, date.week)] += 1

    # Convert data to a pandas dataframe for convenience
    dataframe = pd.DataFrame(data, index=['number of pull requests'])

    print(dataframe)
