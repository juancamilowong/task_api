# task_api
API for task management

- [task\_api](#task_api)
  - [Prerequisites](#prerequisites)
  - [INSTALLATION](#installation)
    - [Install](#install)
    - [Run](#run)
    - [Debug](#debug)
  - [Features](#features)
    - [Create task:](#create-task)
    - [Get all taks:](#get-all-taks)
    - [Get task by id:](#get-task-by-id)
    - [Get task by status:](#get-task-by-status)
    - [Update task:](#update-task)
    - [Delete task:](#delete-task)

## Prerequisites

Before you begin ensure you have the following installed:

- Python 3.10 or higher
- poetry

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