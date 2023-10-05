import json_extractor

# Extract JSON data from a URL
json_data = json_extractor.extract_from_url("https://example.com")

# Extract JSON data from an HTML string
json_data = json_extractor.extract_from_html("<html><body><script>{'hello': 'world!'}</script></body></html>")

# Extract JSON data from an HTML file
json_data = json_extractor.extract_from_file("sample.html")
