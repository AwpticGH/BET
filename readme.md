# Backend Developer Test for Soul Parking
## Simple Todo API App

### Notice
This application will keep on being updated until the deadline of the test has reached it's end. Please check the commit history for any changes made.

### Technologies Used for Development
1. flask
2. Postman

### API URLs
1. /todo (POST) Create TODO [x]
2. /todo (GET) Get all TODO [x]
3. /todo/<id> (GET) Get TODO by ID [x]
4. /todo/<id> (PUT) Update TODO [x]
5. /todo/<id>/finish Finish TODO [x]
6. /todo/<id> (DELETE) Soft delete TODO [x]

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

**NOTE This collection is used for testing as there is no sensitive data used. Please don't judge :) I'm not gonna be spilling secret keys if they're important**

### Architecture
The application is built using Flask, a micro web framework for Python. The application is structured based on the MVC (Model-View-Controller) pattern with a little customization by seperating the controllers and routes logic based on HTTP methods (GET, POST, PUT, DELETE). The config module contains DataConfig which is used to hold variables for Data Persistence. The models module contains the Todo class which is used to represent the TODO object. The controllers module contains the controller classes used to perform actions on data. Lastly, the routes module contains the logic for dealing with HTTP requests.