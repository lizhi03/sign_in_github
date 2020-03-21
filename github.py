from api.repositories.repos import Repos


class Github():
    def __init__(self, **kwargs):
        self.api_root_url = "http://api.github.com"
        self.repos = Repos(self.api_root_url, **kwargs)


if __name__ == '__main__':
    r = Github(token="de4260ff9e5a21e64973cd55c693154c3b56a837")
    x = r.repos.list_your_repos()
    print(x.text)

    r = Github(username="lizhi03", password="LZwshh182")
    x = r.repos.list_your_repos()
    print(x.text)
