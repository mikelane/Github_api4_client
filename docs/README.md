# Client for the Github GraphQL API v4

This is a client that allows the user to make very basic queries to Github's GraphQL library.

### Installation

You should be able to simply run the following:

    python3 setup.py build
    python3 setup.py install 
    
You will need to set up a Personal Access Token on Github by following the directions found 
[here](https://help.github.com/articles/creating-a-personal-access-token-for-the-command-line/). Once you've done that, 
you must create a file in the root directory called `settings.ini`. Use the `example_settings.ini` file as an example of 
how to set up your `settings.ini` file.

### Usage

The script opens a file that contains the json objects to return portion of the query 
([See the documentation](https://developer.github.com/v4/guides/forming-calls/#about-query-and-mutation-operations)), 
reads the file in and makes the query. To run the script, do the following from the projet root:

    ./github_query <filename>

For example:

    ./github_query queries/ramda_pull_requests.query

To run the tests, use this command:

    python3 -m unittests -v github_api4_client/tests/*.py
    

