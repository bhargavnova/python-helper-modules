import pytest
import requests
from wikipedia_search.wikipedia_search import (generate_url, wikipedia_search, NoSearchResultsError,
                                               InvalidLanguageError, SearchFailedError, get_valid_languages)


# Test generate_url function
def test_generate_url():
    # Test with different titles and languages
    assert generate_url("Python") == "https://en.wikipedia.org/wiki/Python"
    assert generate_url("Machine Learning", lang="fr") == "https://fr.wikipedia.org/wiki/Machine_Learning"

    # Test with special characters in the title
    assert (generate_url("Artificial Intelligence (AI)") ==
            "https://en.wikipedia.org/wiki/Artificial_Intelligence_%28AI%29")


# Test with different search queries
def test_wikipedia_search_with_valid_query():
    results = wikipedia_search("Python")
    assert isinstance(results, dict)
    assert "Python" in results


# Test with different languages
def test_wikipedia_search_with_different_language():
    results = wikipedia_search("Machine Learning", lang="fr")
    assert isinstance(results, dict)
    assert "Apprentissage automatique" in results


# Test with a query that should not return results
def test_wikipedia_search_with_no_results():
    with pytest.raises(NoSearchResultsError):
        wikipedia_search("ThisIsARandomUnlikelySearchQuery")


# Test with a query that triggers a search failure
def test_wikipedia_search_with_search_failure():
    with pytest.raises(SearchFailedError):
        wikipedia_search("")


# Test with an invalid language
def test_wikipedia_search_with_language_failure():
    with pytest.raises(InvalidLanguageError):
        wikipedia_search("Python", lang="invalid_language")


def test_get_valid_languages_request_error(monkeypatch):
    # Mock the requests.get() method to return a 404 status code
    def mock_requests_get(url, params):
        class MockResponse:
            def __init__(self, status_code):
                self.status_code = status_code

        return MockResponse(404)

    # Apply the mock to the requests.get() method
    monkeypatch.setattr(requests, 'get', mock_requests_get)

    # Ensure that calling get_valid_languages() raises NoSearchResultsError
    with pytest.raises(NoSearchResultsError):
        get_valid_languages()


# Run the tests
if __name__ == "__main__":
    pytest.main() # pragma: no cover
