from os import path

from setuptools import setup, find_packages

here = path.abspath(path.dirname(__file__))

setup(
    name='Github_api4_client',
    version='0.1alpha',
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    url='https://github.com/mikelane/github_api4_client',
    license='MIT',
    author='Michael Lane',
    author_email='mikelane@gmail.com',
    description='A script for querying the Github GraphQL API',

    # https://packaging.python.org/distributing/#classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Internet :: WWW/HTTP',

        # License should match License above
        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3.6',
    ],

    keywords='github, graphql, graphene, api',
    install_requires=[
        'configparser',
        'requests'
    ],
    setup_requires=[
        'configparser',
        'requests'
    ]
)