# Wordcount API


## Getting started
### Set up Environment
    conda create --name wordcount python=3.7
    conda activate wordcount
    python setup.py install
   
### Start API server
    ./start.sh 

### Check for health
     curl -X 'GET' 'http://localhost:8000/health/'
### Counting Request Example
    curl -X 'GET' 'http://localhost:8000/count/' -H 'accept: application/json' -H 'Content-Type: application/json' -d '{"url":"https://www.bbc.co.uk/"}'

## Testing
### Run Test
    coverage run -m pytest
### Coverage report
    coverage report -m    

        Name                                   Stmts   Miss  Cover   Missing
    --------------------------------------------------------------------
    app/__init__.py                            0      0   100%
    app/api/__init__.py                        0      0   100%
    app/api/api_v1/__init__.py                 0      0   100%
    app/api/api_v1/api.py                      5      0   100%
    app/api/api_v1/endpoints/__init__.py       0      0   100%
    app/api/api_v1/endpoints/count.py         14      0   100%
    app/api/api_v1/endpoints/health.py         6      0   100%
    app/api/config.py                          9      0   100%
    app/main.py                                8      0   100%
    app/schemas/__init__.py                    1      0   100%
    app/schemas/count.py                       4      0   100%
    app/services/counter.py                    5      0   100%
    app/services/scraper.py                   17      0   100%
    app/test_main.py                          45      0   100%
    --------------------------------------------------------------------
    TOTAL                                    114      0   100%

## API Documentation 
When the server is running, on a browser:

    localhost:8000/docs
Postman API documentation is also available: 

    https://go.postman.co/workspace/My-Workspace~1d760d7f-0159-446e-864d-5a1415976a83/collection/12154423-f5d90fe5-0da8-4969-91b6-92a063ca0505?action=share&creator=12154423
## Docker
### Build Docker
    .build_docker.sh

### Run Docker
    docker run -p 8000:8000 wordcount

## Tech stack 
Beautiful Soup
- Powerful library that makes static web scraping by traversing the DOM

FastAPI  
- Excellence performance 
- Easy too set to get API backend up and running. 
- Testing framework and API doc frontend is easy for development.  

Coverage 
- tools to run your test suite and gather data
- easy to install and easy to run from the command line

## Distributed system design
When the input text is small, the bottle neck of the service is from `requests.get(url)` as it is making a get request. 

But as the input text grows, the bottle neck will shift to `Scraper` and `Wordcoutner`. It will still scale linearly. As `text_string_to_list` pass through the text string two times, its performance should grow in O(n).  The python built in `Counter` grows in O(n) too. 

