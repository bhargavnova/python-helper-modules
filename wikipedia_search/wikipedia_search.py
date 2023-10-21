import requests


class NoSearchResultsError(Exception):
    pass


class SearchFailedError(Exception):
    pass


class InvalidLanguageError(Exception):
    pass


def get_valid_languages():
    """
    Fetch the list of valid language codes from Wikipedia.
    Returns a list of language codes.
    """
    response = requests.get("https://en.wikipedia.org/w/api.php", params={
        "action": "query",
        "meta": "siteinfo",
        "siprop": "languages",
        "format": "json"
    })

    if response.status_code == 200:
        data = response.json()
        valid_languages = [lang["code"] for lang in data["query"]["languages"]]
        return valid_languages
    else:
        # Handle API request error
        raise NoSearchResultsError("API resquest Error for languages list")


def check_if_valid_language(lang: str) -> bool:
    # Get the list of valid languages
    valid_languages = get_valid_languages()

    if lang in valid_languages:
        return True
    else:
        return False


def generate_url(title: str, lang: str = "en") -> str:
    """
    Generate an url for a given title and language.

    :param title: The title of the Wikipedia article.
    :param lang: The language for Wikipedia. Default is 'en' (English).
    :return: a mla_citation string with url
    """
    url = f"https://{lang}.wikipedia.org/wiki/{title}"

    forma = {" ": "_",
             "(": "%28",
             ")": "%29"}

    for key, value in forma.items():
        url = url.replace(key,value)

    return url


def wikipedia_search(query: str, lang: str = "en"):
    """
    Search Wikipedia for a given query.
    :param query: The search query.
    :param lang: The language for Wikipedia. Default is 'en' (English).
    :param links: dict. The links for the Wikipedia search. Default is None
    """

    # check if lang is a valid language
    if not check_if_valid_language(lang):
        raise InvalidLanguageError("Invalid language : {lang}")

    # Prepare the search URL with the given query
    search_url = f"https://{lang}.wikipedia.org/w/api.php"
    params = {
        "action": "query",
        "format": "json",
        "list": "search",
        "srsearch": query
    }

    # Send an HTTP GET request to the Wikipedia search API
    response = requests.get(search_url, params=params)
    data = response.json()

    # Check if search failed
    if "query" not in data or "search" not in data["query"]:
        raise SearchFailedError("Wikipedia search failed.")

    # Get the search results
    search_results = data["query"]["search"]

    # Check if there is no result found
    if not search_results:
        raise NoSearchResultsError("No search results found.")

    # return the links
    return {result['title']: generate_url(result['title'], lang) for result in search_results}


if __name__ == "__main__":

    res = wikipedia_search(query="python", lang="en")  # pragma: no cover
    print(res)  # pragma: no cover
