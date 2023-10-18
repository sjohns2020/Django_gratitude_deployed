# Django_gratitude_deployed

## BRIEF
- Create and deploy a Django application that allows admin to review graditude posted and use Django Rest Framework to build an API to connect up with a future React Native Frontend UI.  This is a fullstack Django app that should have an admin portal built in Django, have an integrated API with endpoints that will be used by a React Native frontend.

### MVP
- There should be an API built with Django Rest Framework, creating endpoints for future React Native Frontend.  
- The admin users should be able to review all gratitude posts and create, update and delete them. 
- Users should be able to authenticate.
- The app should use a postgreSQL database to persist data on the server. 
- The app should have an integrated admin website and an API using django_rest_framework to allow a future React application to connect to it. 

### EXTENSIONS
- Deploy the app using Fly
- The app should have a s3 bucket to store images and documents on the cloud. 
- Configure Docker to deploy the postgres database.

### STILL WORKING ON
- Build a React Native Frontend

### LEARNINGS
- How to use Django_rest_framework to create an API endpoint so my app could have an admin portal in Django and a separate front end in React.
- How to use Django's in-built authentication allowing access to the front-end React app allowing access to specific endpoints once authenticated.
- How to configure Docker and how to deploy my Django app using fly.io.


### Tech Stack
- Python
- Django
- Django_rest_framework
- postgreSQL
- AWS
- Docker
- Fly.io
- React


