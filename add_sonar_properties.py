import requests
token_variable = "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"
def get_org_repos(org_name):
  url = "https://api.github.com/orgs/{}/repos".format(org_name)
  headers = {"Authorization": "bearer {}".format(token_variable)}
  response = requests.get(url, headers=headers)
  return response.json()

def add_file_to_repos(file_path, org_name, repo_name):
  repos = get_org_repos(org_name)
  for repo in repos:
    if repo_name in repo:
      repo_url = "https://github.com/{}/{}".format(org_name, repo["name"])
      repo_clone_url = repo["clone_url"]
      cloned_repo = git.clone(repo_clone_url)
      git.add(file_path, cloned_repo)
      git.commit(message="Adding file to all repos", repo=cloned_repo)
      git.push(cloned_repo)

file_path = "sonar.properties"
org_name = "Prasanna-source31"
repo_name = "XXX"

add_file_to_repos(file_path, org_name, repo_name)
