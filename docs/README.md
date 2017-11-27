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

Currently, there is a single hard-coded query in `main.py`. To see the query in action, do `python3 main.py` from the
command line. 
