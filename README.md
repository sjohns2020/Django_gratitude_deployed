# Django_gratitude_deployed

BRIEF: 

Tech Stack
Python
Django
Django_rest_framework
AWS
Docker
Fly.io
React


MVP

Create and deploy a gratitude app for businesses so users are able to authenticate and leave notes of gratitude for specific staff with pictures.  
This is a full stack Django app that should have an admin portal built in Django, have an integrated API that will have a React front end
for a UI for users. 


EXTENSIONS

Build a React Front end


FEATURES:

The admin users should be able to review all gratitude posts and create, update and delete them. 
Users should be able to authenticate.
The app should have an integrated admin website and an API using django_rest_framework to allow a future React application to connect to it. 
The app should have a s3 bucket to store images and documents on the cloud. 
The app should be deployed.


LEARNINGS
I learned how to use Django_rest_framework to create an API endpoint so my app could have an admin portal in Django and a separate front end in React.
I learned how to use Django's in-built authentication allowing access to the front-end React app allowing access to specific endpoints once authenticated.
I learned how to configure Docker and how to deploy my Django app using fly.io. 



I deployed my gratitude django full stack app with postresql and an s3 bucket to fly.io
