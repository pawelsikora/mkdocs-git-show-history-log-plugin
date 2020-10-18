from git import Git, Repo

class GitInfo:
    def __init__(self):
        self.g = Git()
        self.r = Repo()
    
    def get_commits_for_file(self, path, count):
        return list(self.r.iter_commits('--all', max_count=count, paths=path))

    def get_tag_for_commit(self, commit):
        return next((tag for tag in self.r.tags if tag.commit == commit), None)
