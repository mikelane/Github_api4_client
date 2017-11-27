#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import configparser

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

    ramda_query = '''
    {
        repository(owner: "ramda", name: "ramda") {
            pullRequests(last:100) {
                edges {
                    node {
                        number
                        title
                        author {
                            login
                        }
                        state
                        createdAt
                        lastEditedAt
                        mergeable
                        merged
                        mergedAt
                        url
                        revertUrl
                        comments(last:100) {
                            edges {
                                node {
                                    author {
                                        login
                                    }
                                    bodyText
                                    createdAt
                                    lastEditedAt
                                    editor {
                                        login
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }'''

    response = client.query(ramda_query)
    print(response.json())
