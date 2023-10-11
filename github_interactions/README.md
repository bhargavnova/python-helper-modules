# GitHub Interactions

This Python script allows you to interact with GitHub using the GitHub REST API and the PyGitHub library. You can perform various GitHub actions right from your command line. Here are some of the functionalities this tool provides:

1. **Create a New Repository**: Create a new GitHub repository with a name, description, and the option to make it private or public.
2. **List User Repositories**: List repositories of a GitHub user. Simply enter the username, and it will display the user's repositories.
3. **Fork a Repository**: Fork another user's GitHub repository. Provide the username and the repository name you want to fork.
4. **Clone a Repository**: Clone a GitHub repository to your local machine. Enter the repository's URL and the local directory path.
5. **Add Collaborators**: Add collaborators to a GitHub repository. You'll need the owner's username, the repository name, and the collaborator's username.
6. **Remove Collaborators**: Remove collaborators from a GitHub repository. Similar to adding collaborators, provide the owner's username, repository name, and the collaborator's username.

## Usage

1. Clone this repository or download the script (`github_interactions.py`) to your local machine.
2. Create a Personal Access Token (PAT) on GitHub following the [GitHub Token Creation Guide](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token).
3. Open the `Token.py` file and replace `"YOUR_PAT_HERE"` with your Personal Access Token:

   ```python
   personal_access_token = "YOUR_PAT_HERE"
   ```
4. Run the script by executing `python github_interactions.py` in your terminal.
5. Choose the desired action by entering the corresponding number.
6. Follow the prompts and provide the required information as requested by the script.

## Prerequisites

- Python 3.x
- Required Python libraries: `os`, `git`, `requests`, `github`

## Note

- This tool is for educational and demonstration purposes. Be cautious while handling access tokens and personal information.

Feel free to explore more functionalities or contribute to this project!

**Enjoy your GitHub interactions with this program!**
