import requests

def get_org_repos(org_name):
  url = "https://api.github.com/orgs/{}/repos".format(org_name)
  headers = {"Authorization": "bearer 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"}
  response = requests.get(url, headers=headers)

  if response.status_code == 200:
    return response.json()
  else:
    raise Exception("Error getting repos: {}".format(response.status_code))

org_name = "Prasanna-source31"

repos = get_org_repos(org_name)

for repo in repos:
  print(repo["name"])
