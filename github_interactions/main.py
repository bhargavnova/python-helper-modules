import os
import git
import requests
from github import Github
from Token import personal_access_token

headers = {"Authorization": f"Bearer {personal_access_token}", "Accept": "application/vnd.github.v3+json"}
baseUrl = "https://api.github.com"

# Create a repository
def create_repo():
    repoName = input("Enter the repository name: ")
    repoDescription = input("Enter the repository description:")
    privateRepo = input('Private Repo? (True/False): ')  # Private or public, default is False

    create_repo_url = f"{baseUrl}/user/repos"
    jsonData = {
        "name": repoName,
        "description": repoDescription,
        "auto_init": True,
        "private": privateRepo
    }
    
    response = requests.post(create_repo_url, headers = headers, json = jsonData)
    if response.status_code == 201:
        print("Repository created successfully ✅")
    else:
        print("Failed to create a repository ❌", response.status_codes)
        print("Response Content:", response.text)

#List different user's repositories
def list_repos():
    userName = input("Enter username: ")
    user_repo_url = f"{baseUrl}/user/{userName}/repos"
    response = requests.get(user_repo_url, headers = headers)

    if response.status_code == 200:
        reposList = response.json
        print("User Repositories:")
        for repo in reposList:
            print(repo["name"])
    else:
        print("Request Failed")

#Fork repositories
def fork_repo():
    userName = input("Enter the username: ")
    repoName = input("Enter the repo name: ")
    url = f"{baseUrl}/repos/{userName}/{repoName}/forks"
    response = requests.post(url, headers = headers)

    if response.status_code == 202:
        print(f"Repository {repoName} forked successfully ✅")
    else:
        print(f"Failed to fork repository ❌: {repoName}")
        print("Response Content:", response.text)

#Cloning repository
def clone_repo():
    repo_url = input("Enter the repo's URL to clone: ")
    local_path = input("Enter the local directory path to clone: ")
    
    if not os.path.exists(local_path):
        os.makedirs(local_path)
    
    try:
        repo = git.Repo.clone_from(repo_url, local_path)
        print("Repository cloned successfully ✅")
    except git._exc.GitCommandError as e:
        print(f"Failed to clone the repo ❌ ({e})")

#Add collaborators to a project
def add_collaborators():
    g = Github(personal_access_token)
    owner = input("Enter the GitHub Username of the repository's owner: ")
    repoName = input("Enter the name of the repository: ")
    userName = input("Enter the GitHub Username of the collaborator: ")

    repoInfo = f"{owner}/{repoName}"
    try:
        repo = g.get_repo(repoInfo)
        repo.add_to_collaborators(userName, "push")
        print(f"{userName} was added as the collaborator to {repoName} ✅")
    except Exception as e:
        print(f"Failed to add {userName} as a collaborator ❌: {str(e)}")

#Remove collaborators from a project
def remove_collaborators():
    g = Github(personal_access_token)
    owner = input("Enter the GitHub Username of the repository's owner: ")
    repoName = input("Enter the name of the repository: ")
    userName = input("Enter the GitHub username of the collaborator: ")

    repoInfo = f"{owner}/{repoName}"
    try:
        repo = g.get_repo(repoInfo)
        repo.remove_from_collaborators(userName)
        print(f"{userName} removed as a collaborator from {repoName} ✅")
    except Exception as e:
        print(f"Failed to remove {userName} as a collaborator ❌: {str(e)}")

def main():
    while True:
        print("======================================================")
        print("Github Interactions:")
        print("1. Create a new Repo")
        print("2. List user repositories list")
        print("3. Fork a repository")
        print("4. Clone a repository")
        print("5. Adding colaborators")
        print("6. Remove collaborators")
        ## Continue adding more interactions

        print("0. Exit")
        print("======================================================")
        
        userChoice = int(input("Enter your choice:"))

        if userChoice == 1:
            create_repo()
        elif userChoice == 2:
            list_repos()
        elif userChoice == 3:
            fork_repo()
        elif userChoice == 4:
            clone_repo()
        elif userChoice == 5:
            add_collaborators()
        elif userChoice == 6:
            remove_collaborators()
        ## Continue adding more down here

        elif userChoice == 0:
            print("Exiting the program!! ")
        else:
            print("Invalid choice. Try again!!")


if __name__ == "__main__":
    main()