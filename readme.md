# Backend Developer Test for Soul Parking
## Simple Todo API App

### Technologies Used for Development
1. flask
2. Postman

### API URLs
1. /todo (POST) Create TODO []
2. /todo (GET) Get all TODO []
3. /todo/<id> (GET) Get TODO by ID []
4. /todo/<id> (PUT) Update TODO []
5. /todo/<id>/finish Finish TODO []
6. /todo/<id> (DELETE) Soft delete TODO []

### TODO Object/Model
- id: unique ID (auto-increment)
- title: title of the TODO list
- description: description of the TODO list
- finished_at: timestamp of when the TODO list is finished
- created_at: timestamp of when the TODO list is created
- updated_at: timestamp of when the TODO list is updated at
- deleted_at: timestamp of when the TODO list is deleted
**Note** Timestamp is in the format of *d-m-Y H:i:s (07-11-2024 20:22:32)* 