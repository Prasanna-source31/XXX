import requests
import base64
import os

# Set your GitHub organization name and access token
organization = "Prasanna-source31"
access_token = os.environ.get("PYTHON_SECRET")

source_file_url = 'https://github.com/Prasanna-source31/XXX/blob/main/sonar.properties'

def get_repos():
    url = f"https://api.github.com/orgs/{organization}/repos"
    headers = {
        "Authorization": f"Bearer {access_token}"
    }

    response = requests.get(url, headers=headers)
    repos = response.json()
    return repos

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
    properties_response = requests.get(source_file_url)
    if properties_response.status_code == 200:
        source_properties_content = properties_response.text
        repos = get_repos()
        print(f"Number of repos: {len(repos)}")  # Check the number of repositories
        for repo in repos:
            if isinstance(repo, dict) and 'name' in repo:
                print(f"Adding properties to repo: {repo['name']}")
                add_sonar_properties(repo['name'], source_properties_content)
    else:
        print(f"Failed to fetch SonarQube properties from {source_file_url}")


