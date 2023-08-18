import requests
import base64
import os

# Set your GitHub organization name and access token
organization = "Prasanna-source31"
access_token = os.environ.get("PYTHON_SECRET")

# Set the source repository and file path in the main branch
source_repo = "XXX"
source_file_path = "./sonar.properties"

def get_repos():
    url = f"https://api.github.com/orgs/{organization}/repos"
    headers = {
        "Authorization": f"Bearer {access_token}"
    }

    response = requests.get(url, headers=headers)
    repos = response.json()
    return repos

def get_file_content(repo, file_path):
    url = f"https://api.github.com/repos/{organization}/{repo}/contents/{file_path}"
    headers = {
        "Authorization": f"Bearer {access_token}"
    }

    response = requests.get(url, headers=headers)
    content = response.json().get("content")
    if content:
        return base64.b64decode(content).decode("utf-8")
    return None

def add_sonar_properties(repo, properties_content):
    url = f"https://api.github.com/repos/{organization}/{repo['name']}/contents/sonar.properties"
    headers = {
        "Authorization": f"Bearer {access_token}"
    }

    encoded_content = base64.b64encode(properties_content.encode("utf-8")).decode("utf-8")
    data = {
        "message": "Add SonarQube properties",
        "content": encoded_content
    }

    response = requests.put(url, json=data, headers=headers)
    if response.status_code == 201:
        print(f"SonarQube properties added to {repo['name']}")
    else:
        print(f"Failed to add SonarQube properties to {repo['name']}: {response.text}")

if __name__ == "__main__":
    source_properties_content = get_file_content(source_repo, source_file_path)
    if source_properties_content is None:
        print(f"Failed to fetch SonarQube properties from {source_repo}")
    else:
        repos = get_repos()
        for repo in repos:
            add_sonar_properties(repo, source_properties_content)
