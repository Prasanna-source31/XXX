import requests

def copy_file(org_name, repo_name, file_path):
  url = "https://api.github.com/repos/{}/{}/contents/{}".format(org_name, repo_name, file_path)
  headers = {"Authorization": "bearer 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"}
  response = requests.post(url, headers=headers)

  if response.status_code == 201:
    print("File copied successfully")
  else:
    print("Error copying file")

org_name = "Prasanna-source31"
repo_name = "XXX"
file_path = "sonar.properties"

copy_file(org_name, repo_name, file_path)
