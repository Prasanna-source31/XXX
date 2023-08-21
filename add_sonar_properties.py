from github import Github
import os

# Get the value of the secret variable from the environment
access_token = os.environ.get('SECRET_PYTHON2')



# Name of the source repository
source_repo_name = 'XXX'
# Path of the file to be copied within the source repository
source_file_path = 'sonar.properties'

# Name of the target organization
organization_name = 'Prasanna-source31'

# Initialize the GitHub API client
g = Github(access_token)

# Get the source repository
source_repo = g.get_repo(f'{organization_name}/{source_repo_name}')

# Get all repositories in the organization
org_repos = g.get_organization(organization_name).get_repos()

# Iterate over each repository and copy the file
for repo in org_repos:
    try:
        # Get the contents of the source file in the source repository
        source_file_content = source_repo.get_contents(source_file_path)
        
        # Create or update the file in each repository within the organization
        repo.create_file(source_file_path, f'Copying {source_file_path}', source_file_content.decoded_content)
        
        print(f'File copied to {repo.name}')
    except Exception as e:
        print(f'Error copying file to {repo.name}: {str(e)}')
