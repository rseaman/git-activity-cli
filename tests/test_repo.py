from lib.ghutils import Repo


class TestRepo:

    def test_repo_init(self):
        assert type(Repo('rseaman/git-activity-cli')) == Repo
