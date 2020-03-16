# Attainia Assessment
### Getting Started
I work on a Windows machine. The instructions should be mostly the same. On other machines replace 'py' with 'python3'/'python'  
Clone this repository: 
```git clone git@github.com:richardswei/attainiaapp.git```

### Set up the Django REST Framework API
This install depends on pip, make sure you have it by running:  
  ```pip -V```  
I also use virtualenvwrapper for easier virtual env management: <https://virtualenvwrapper.readthedocs.io/en/latest/>   
Make a new virtual environment:  
  ```mkvirtualenv <INSERT desired environment name here>```  
Install dependencies:  
  ```run pip install -r requirements.txt```  
Seed the sqlite database:  
  ```run py manage.py loaddata users.json```  
Make the migrations:  
  ```run py manage.py migrate```  
Run the server:  
  ```run py manage.py runserver```  

Navigate to <http://localhost:8000/api/v1/users/> to see the users.  
To get the list of users that have logged on at least once:  
<http://localhost:8000/api/v1/users/?status=active>  
To get the list of users that never logged on:  
<http://localhost:8000/api/v1/users/?status=dormant>

### Set up the Vue frontend
Open another terminal tab

From project root, cd into the vue app:  
  ```cd user-activity-app/```  
Install dependencies:  
  ```run npm install```  
Run the app:  
  ```run npm run serve``` 

### Run the Application
Navigate to <http://localhost:8080/> to see the application.
If no data appears in the table, make sure both servers are running in separate terminal tabs.

