## Installation

python .\src\app\app.py



## What to do more for production environment 
- Add test coverage
- Uncomment a code line for getting elastic-search uri from os environment.

infrastructure/elastic_search.py 
```python
uri = es_uri or os.getenv('ES_URI') 
```

