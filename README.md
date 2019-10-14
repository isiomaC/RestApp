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
	"data": " Data object containing information about the response",
	"message":" Message about the request" 
}
```

-`200 Ok` on success

### Get System version

`GET /system`

**Response**

```json
{
	"data": " Data object containing information about the response",
	"message":" Message about the request" 
}
```

-`200 Ok` on success

### Get information about a picture hosted on pond5

`GET /mediainfo/<id>` on success


**Response**

```json
{
	"data": " Data object containing information about the response",
	"message":" Message about the request" 
}
```

-`200 Ok` on success


##How to run

**Download project from github reposiotory**

Make a new directory and clone the project into that directory

- `git clone <git address>`


**Build and Run docker container**

Build the docker image with the command below

- `docker images build -t <new_directory_name> .`

Run container with command

- `docker container run -p 5000:5000 -name <container_name> <new_directory_name>:latest`

`The new directory name and container_name can be anything you like`

Visit locahost:5000 to view the Api results





