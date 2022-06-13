#!/usr/bin/env python3

"""
GitHub Activity CLI

This command-line utility will do one of two things when given a GitHub repository name:
* Return the names/version numbers of the three latest releases.
* Return the title and number of the three most recent pull requests.

Usage:
    gac.py release <repo> [--results=<num_results>]
    gac.py pr <repo> [--results=<num_results>]

Options:
    -r <num_results> --results=<num_results>  The number of results to return [default: 3]
"""

from docopt import docopt
from schema import Schema

def main():
    pass