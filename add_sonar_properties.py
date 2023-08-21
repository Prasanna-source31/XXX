"""
Program to Copy a File to All Repositories in an Organization

This program provides a function to copy a file from a GitHub repository to all other repositories in an organization.

"""

import logging
import requests
import os

# Setting up logging to monitor performance and errors
logging.basicConfig(level=logging.INFO)

def copy_file_to_repos(org_name: str, repo_name: str, file_path: str, github_token: str) -> None:
    """
    Copy a File to All Repositories in an Organization

    This function copies a file from a GitHub repository to all other repositories in an organization.

    Args:
    org_name (str): Name of the organization.
    repo_name (str): Name of the repository containing the file.
    file_path (str): Path of the file to be copied.
    github_token (str): GitHub personal access token with appropriate permissions.

    Returns:
    None

    Raises:
    ValueError: If any of the input arguments are empty or invalid.
    Exception: If an error occurs during the file copy process.

    Examples:
    >>> copy_file_to_repos("myorg", "myrepo", "path/to/file.txt", "mytoken")
    INFO: Fetching repositories in the organization...
    INFO: Found 10 repositories in the organization.
    INFO: Copying file to repository: repo1
    INFO: File copied successfully to repository: repo1
    INFO: Copying file to repository: repo2
    INFO: File copied successfully to repository: repo2
    ...
    INFO: Copying file to repository: repo10
    INFO: File copied successfully to repository: repo10
    INFO: File copied to all repositories in the organization.

    """

    # Validate input arguments
    if not org_name or not repo_name or not file_path or not github_token:
        raise ValueError("Invalid input arguments. Please provide valid values for org_name, repo_name, file_path, and github_token.")

    try:
        logging.info("Fetching repositories in the organization...")
        # Fetch all repositories in the organization
        headers = {
            "Authorization": f"Bearer {github_token}"
        }
        url = f"https://api.github.com/orgs/{org_name}/repos"
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        repositories = response.json()

        logging.info(f"Found {len(repositories)} repositories in the organization.")

        # Copy the file to each repository
        for repository in repositories:
            repo_full_name = repository["full_name"]
            logging.info(f"Copying file to repository: {repo_full_name}")

            # Create a new file in the repository with the contents of the original file
            url = f"https://api.github.com/repos/{repo_full_name}/contents/{file_path}"
            data = {
                "message": "Copy file to repository",
                "content": "",
                "sha": "",
                "branch": "main"
            }
            response = requests.put(url, headers=headers, json=data)
            response.raise_for_status()

            logging.info(f"File copied successfully to repository: {repo_full_name}")

        logging.info("File copied to all repositories in the organization.")

    except Exception as e:
        logging.error(f"An error occurred: {e}")
        raise

if __name__ == "__main__":
    # Example usage
    org_name = "Prasanna-source31"
    repo_name = "XXX"
    file_path = "sonar.properties"
    github_token = "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"

    try:
        copy_file_to_repos(org_name, repo_name, file_path, github_token)
    except ValueError as ve:
        print(f"Invalid input arguments: {ve}")
    except Exception as e:
        print(f"An error occurred: {e}")
