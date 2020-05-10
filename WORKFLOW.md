## Setup and running of project (Backend)
- Fork the repo and clone it.
- Go in the repo and setup virtualenvironment using <br>
```python -m venv env``` 
- Then activate the environment using <br>
    On Windows
```source env/Scripts/activate```
    On MacOS/Linux
```source env/bin/actiavte```
- At the root of your project directory <br>
```bash 
pip install -r requirements.txt
```

- Rename ```.env.example``` to ```.env```
- Put the ```.env``` file in ```/engbook ```set secret key for your django project.
- You can use [https://djecrety.ir/] to generate your secret key
- Set ```DEBUG = True``` during development in ```.env``` file

- After the above setup, run <br>
```python engbook/manage.py makemigrations```
```python engbook/manage.py migrate```

- Start the backend server 
```python engbook/manage.py runserver```
Runs the backend server at default port ```8000```.<br />
Open [http://localhost:8000](http://localhost:8000) to view it in the browser.

The page will reload if you make edits.<br />

## Setup and running of project (Frontend)
- At your root directory run `npm install` to install all the dependencies
- Start react dev server
- ```npm run dev```

Runs the app in the development mode.<br />
Open [http://localhost:8000](http://localhost:8000) to view it in the browser.


#### Note
- If you are adding any new requirements for the project, make sure that you are adding it to ```requirements.txt```
- Use only ```npm install package_name``` to add new packages to the frontend part.