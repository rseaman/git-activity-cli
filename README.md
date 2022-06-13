# git-activity-cli
Short take-home project.

This utility is explicitly for gathering data from GitHub's REST API via simple CLI commands.
# Installation
This utility can be run on Linux, OS X, or Windows (but only in WSL)

1. Install and configure Python3 and pip3.
1. `cd` to this repository's directory.
1. Run `pip3 install -r requirements.txt`
1. Make sure `gac.py` is executable! `chmod u+x gac.py`

# Usage
Run `gac.py` to see the utility's help screen.

It will default to returning 3 results for either Releases or PRs, but this can be overridden with `-r #`.
