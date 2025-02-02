# UGAHacks6-Project

### Investing Group Chat Webapp

### How to code in the Github 
Everyone in the team should have their own branch in github. if you are working on your own enhancements to the program, then work on your specific branch before working on the main branch. This will protect everyone from not destroying each others code.

### Steps to start coding
We are gonna be using a django framework to structure our webapp. follow the below steps to get the project working.  

1) Download this git folder into a place you can work in your computer.  In the terminal, type this in and it should be available on your computer:  
```
git clone https://github.com/noahaus/UGAHacks6-Project.git
```
2) Download python3 if you do not have it  
3) install pipenv if you do not have it  
```
pip3 install pipenv
```  
4) run the following in the terminal (where the location is the github folder you downloaded). This will allow you to start using the web framework django:  
```
pipenv shell  
```    
NOTE: If you are getting an error at this step, your python version may not match the Pipfile python version. go into the Pipfile and make this change if needed:
```
[[source]]
url = "https://pypi.org/simple"
verify_ssl = true
name = "pypi"

[packages]
django = "~=3.1.0"

[dev-packages]

[requires]
python_version = "3.7.7" <--------- Change the version here.
```
5) To start the web app, type in this command in the same folder, this will create a server that hosts the web app:  
```
python manage.py runserver
```  
6) After you run the command, you should see something like this:   
```
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).

You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
February 06, 2021 - 00:46:45
Django version 3.1.6, using settings 'config.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```  

You just turned on the web server, which can host the web app we are creating. to test if it is working properly, go to your browser and go to the address http://127.0.0.1:8000/ 
  
    
![default django page](https://djangoforbeginners.com/images/00_welcome31.png)  
  
    
For another explanation of this, check out https://djangoforbeginners.com/images/00_welcome31.png. Follow this tutorial to the end to learn how to add your own HTML to the webframework. 
Congratulations, you now can interact with the web app and make different edits!
