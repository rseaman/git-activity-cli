#!/usr/bin/env python3

"""
GitHub Activity CLI

This command-line utility will do one of two things when given a GitHub repository name:
* Return the names/version numbers of the three latest releases.
* Return the title and number of the three most recent pull requests.

Note that repository names must be in GitHub's <owner>/<repo> format!

Usage:
    gac.py release <repo> [--results=<results>] [-v]
    gac.py pr <repo> [--results=<results>] [-v]

Options:
    -h, --help                         Show this message
    -r <results>, --results=<results>  The number of results to return, up to 30 [default: 3]
    -v                                 Verbosity, use for more logging
"""

import logging
import sys

from docopt import docopt
from schema import Schema, And, Use, SchemaError
from lib.ghutils import Repo


def main():
    args = docopt(__doc__)
    num_results = int(args['--results'])

    # Set up logging level according to verbosity
    if args['-v']:
        log_level = logging.INFO
    else:
        log_level = logging.ERROR

    logging.basicConfig(filename='logs/gac.log', level=log_level)

    # Validate input
    # TODO: Validate that repo contains a '/' and is of a reasonable length!
    schema = Schema([{
        '--results': And(Use(int), lambda n: 1 <= n <= 30, error='--results must be an integer between 1 and 30!')
    }])

    try:
        schema.validate([{'--results': args['--results']}])
    except SchemaError as e:
        logging.error(f'Invalid input, please see --help: {e}')
        print("Invalid input, see logs!")
        sys.exit(1)

    # Create repo object to work with
    repo = Repo(args['<repo>'])

    if args['release']:
        for i in repo.get_releases(num_results):
            print(f"Title: {i['title']}\tTag Name: {i['tag_name']}\n")
    if args['pr']:
        for i in repo.get_pull_requests(num_results):
            print(f"Number: {i['number']}\tTitle: {i['title']}\n")


if __name__ == "__main__":
    main()
