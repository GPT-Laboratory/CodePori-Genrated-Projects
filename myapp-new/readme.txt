OpenAi: the code is using the "gpt-3.5-turbo-16k" for chatgpt calls.
the api key is in : static/scripts.js file. you can the model and api key here.

Python Instruction:

- Create conda enviornment

- install these pip package before running the project:
	pip install flask

- how to run the project: 
	- Open cmd in the project directory
	- Activate the conda enviornment
	- Run this command:  flask --app app run
	- Project run on this: localhost:5000/

Project information:
	- Project consist on three pages: login, register, index
	- username and password is stored in this file: user_info.txt
	- username and password format for storage file: username-password (Note: don't use "-" when creating new user.)
	- default user: email: admin , password: admin

Project Functionality:
	- User can Register new account by using username and password.
	- can't regiter duplicate account with same username
	- chat gpt can be used on index page