# JSON extractor  
  
This module extracts JSON data from `<scripts>` HTML tag 
  
## Features  
- Extracts JSON data from all `<script>` tags on a single page.  
- You can extract JSON data from URL, *.html file or from HTML string  
  
## Usage  
  
For first install requirements with `pip install -r requirements.txt`  
  
```python  
import json_extractor  
  
# Extract JSON data from a URL  
json_data = json_extractor.extract_from_url("https://example.com")  
  
# Extract JSON data from an HTML string  
json_data = json_extractor.extract_from_html("<html><body><script>{'hello': 'world!'}</script></body></html>")  
  
# Extract JSON data from an HTML file  
json_data = json_extractor.extract_from_file("sample.html")  
```