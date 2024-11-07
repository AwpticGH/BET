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

### Data Persistence
Uses normal list (array) instead of a database as required by the test.

### Testing with Postman
You can use the following URL to get my API collection for testing the application.
https://api.postman.com/collections/22665825-4a237774-ea06-412e-be63-5d99fa075d77?access_key=PMAT-01JC3DEEWQQMK4X4T08TB6Z1RX