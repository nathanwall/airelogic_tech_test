# airelogic_tech_test

## Installation 

### Manual
From the root folder of the project: <br/>
`pip install poetry`<br/>
`poetry install` </br>

### Docker
From the root folder of the project: <br/>
`docker build --no-cache -t airelogic_tech_test -f Dockerfile .`<br/>

## Tests
From the root folder of the project: </br>
`pytest tests`

## Starting the API

### Manual
`uvicorn api:app --host 0.0.0.0 --port 8080`<br/>

### Docker
`docker run -it --rm -p 8080:8080 -e SERVER_HOST=0.0.0.0 -e SERVER_PORT=8080 --name airelogic_tech_test airelogic_tech_test:latest`<br/>

### docker-compose
`docker-compose -f docker-compose.yaml up`<br/>

## Calling the API

### OpenAPI
Once the application has been started: 
- From a browser navigate to `localhost:8080/docs`
- Select the `/average_lyrics` drop down menu
- Select `Try it out`
- Enter an artist name in the `artist` parameter field
- Select `Execute`

### curl
Once the application has been started:
- From a command line do `curl -X GET "http://localhost:8080/average_lyrics?artist=artist name"`

## logging
Logging is output to `app.log` in the root folder of the project. The log level can be changed by changing the `--log-level` argument at run-time. By default it is set to `warning`. Setting the log level `info` will output extra logging.

## API Documentation
OpenAPI (Swagger) docs comes as standard with FastAPI applications. To access simply navigate to `localhost:8080/docs`

## Issues
- Due to the speed of the referencing APIs the results can be a little slow and timings may vary
- The MusicBrainz API is rate limited to 1 request per second
- The lyrics.ova API doesn't have entries for lesser known artists or tracks
- The lyrics returned from the lyrics.ova API can vary for the same input data (see Britney Spears - Soda Pop) which can mean that the average varies