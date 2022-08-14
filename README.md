# Wordcount API


## Getting started
### Set up Environment
    conda create --name wordcount python=3.7
    conda activate wordcount
    python setup.py install
   
### Start API server
    uvicorn app.main:app --reload

### Request
    curl -X 'GET' 'http://localhost:8000/count/' -H 'accept: application/json' -H 'Content-Type: application/json' -d '{"url":"https://www.bbc.co.uk/"}'

### Run Test
    python -m pytest

### Build Docker
    ./build_scripts/build_docker.sh

### Run Docker
    docker run --env-file .env -p 8000:8000 contilio/modelapi
    docker run -p 8000:8000 wordcount

