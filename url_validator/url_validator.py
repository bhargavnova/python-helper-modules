import re
import requests


def is_valid(url):
    # Regular expression pattern to validate URLs
    url_pattern = re.compile(
        r'^(https?|ftp)://'  # Scheme (http/https/ftp)
        r'(([A-Za-z0-9.-]+)\.([A-Za-z]{2,63}))'  # Domain (e.g., example.com)
        r'(:\d+)?'  # Port (optional)
        r'(/.*)?$'  # Path (optional)
    )
    return re.match(url_pattern, url) is not None


def is_accessible(url):
    try:
        response = requests.head(url)
        return response.status_code < 400
    except requests.exceptions.RequestException:
        return False


def validate(url):
    if not is_valid(url):
        return False, False  # URL is not valid, not accessible

    return True, is_accessible(url)