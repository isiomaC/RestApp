# Simple Api Service

##Usage

Response will be in the format below 

```json
{
	"data": " Data Object containing information about the response",
	"message":" Message about the request" 
}
```

### Play ping pong with the Api

`GET /ping`

**Response**

```json
{
	"data": " Data Object containing information about the response",
	"message":" Message about the request" 
}
```

-`200 Ok` on success

### Get System version

`GET /system`

**Response**

```json
{
	"data": " Data Object containing information about the response",
	"message":" Message about the request" 
}
```

-`200 Ok` on success

### Get information about a picture hosted on pond5

`GET /mediainfo/<id>` on success


**Response**

```json
{
	"data": " Data Object containing information about the response",
	"message":" Message about the request" 
}
```

-`200 Ok` on success


##How to run

**Download project from github reposiotory**

- `Clone the repo with git clone <git address>`


**Build and Run docker container**

Build the docker image with the command below

- `docker images build -t restapp .`

Run container with command

- `docker container run -p 5000:5000 -name <Image_name> restapp:latest`

Visit locahost:5000 to view the Api results





