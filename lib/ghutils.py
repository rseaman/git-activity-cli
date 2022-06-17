"""
Utilities for accessing Github functionality
"""

import logging

from typing import List
from github import Github


class Repo:
    def __init__(self, repo_name: str) -> None:
        # Get token from file, create Github object
        try:
            with open("token.txt", 'r') as f:
                self.gh = Github(f.read())
        except OSError as e:
            logging.error("Error retrieving Personal Access Token (PAT) from token.txt",
                          "\nPlease add PAT as single line in token.txt",
                          f"\nError: {e}")
            raise

        # Now that we have the Github object, get the repo itself
        self.repo = self.gh.get_repo(repo_name)

    def get_pull_requests(self, num_res: int) -> List:
        # Pulling from 'all' for now rather than 'open', using default sort of 'created' and 'desc'
        # See: http://docs.github.com/en/rest/reference/pulls
        # TODO: Allow for pulling more pages
        pulls_page = self.repo.get_pulls(state='all').get_page(0)

        # Only try to pull up to the total count of results available, otherwise we'll get a KeyError
        iterations = self.count_safety_check(num_res, pulls_page)

        results = []

        for i in range(iterations):
            results.append({'title': pulls_page[i].title,
                            'number': pulls_page[i].number})

        return results

    def get_releases(self, num_res: int) -> List:
        # See: https://docs.github.com/en/rest/releases/releases
        # TODO: Allow for pulling more pages
        releases_page = self.repo.get_releases().get_page(0)

        # Only try to pull up to the total count of results available, otherwise we'll get a KeyError
        iterations = self.count_safety_check(num_res, releases_page)

        results = []

        # Set title and tag_name. Version was requested, but while GitHub doesn't specify a version number in their
        #   schema for releases, the title OR tag_name is usually responsible for that.
        for i in range(iterations):
            results.append({'title': releases_page[i].title,
                            'tag_name': releases_page[i].tag_name})

        return results

    @staticmethod
    def count_safety_check(count, results):
        total_count = len(results)

        if count < total_count:
            return count
        else:
            return total_count
