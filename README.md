# task_api
API for task management

- [task\_api](#task_api)
  - [Prerequisites](#prerequisites)
  - [INSTALLATION](#installation)
    - [Install](#install)
    - [Run](#run)
    - [Debug](#debug)
  - [Database Scripts](#database-scripts)
  - [Features](#features)
    - [Create task:](#create-task)
    - [Get all taks:](#get-all-taks)
    - [Get task by id:](#get-task-by-id)
    - [Get task by status:](#get-task-by-status)
    - [Update task:](#update-task)
    - [Delete task:](#delete-task)
  - [Contributors](#contributors)

## Prerequisites

Before you begin ensure you have the following installed:

- Python 3.10 or higher
- poetry
- Mysql

## INSTALLATION
### Install
```
poetry install
```

### Run

```
poetry run flask --app app run
```
### Debug

```
poetry run flask --app app run --debug
```

## Database Scripts
```
CREATE TABLE tasksDB.task (
	id INTEGER auto_increment NOT NULL,
	description varchar(255) NOT NULL,
	status varchar(100) NULL,
	created_at DATE NULL,
	updated_at DATE NULL,
	CONSTRAINT task_PK PRIMARY KEY (id)
)
ENGINE=InnoDB
DEFAULT CHARSET=utf8mb4
COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE tasksDB.`user` (
	id INTEGER auto_increment NOT NULL,
	username varchar(100) NOT NULL,
	password varchar(255) NOT NULL,
	created_at DATE NULL,
	CONSTRAINT user_pk PRIMARY KEY (id)
)
ENGINE=InnoDB
DEFAULT CHARSET=utf8mb4
COLLATE=utf8mb4_0900_ai_ci;


```


## Features
### Create task: 
```
curl --location 'http://127.0.0.1:5000/api/tasks' \
--header 'Content-Type: application/json' \
--data '{
    "description": "Go to the GYMdsadsadadsa"
}'
```
### Get all taks: 
```
curl --location 'http://127.0.0.1:5000/api/tasks'
```
### Get task by id: 
```
curl --location 'http://127.0.0.1:5000/api/tasks/1'
```
### Get task by status: 
```
curl --location 'http://127.0.0.1:5000/api/tasks/status/IN-PROGRESS'
```
### Update task: 
```
curl --location --request PUT 'http://127.0.0.1:5000/api/tasks/3' \
--header 'Content-Type: application/json' \
--data '{
    "description": "UPDATED TASK",
    "status": "IN-PROGRESS"
}'
```
### Delete task: 
```
curl --location --request DELETE 'http://127.0.0.1:5000/api/tasks/2'
```

## Contributors

- [@juancamilowong](https://www.github.com/juancamilowong)