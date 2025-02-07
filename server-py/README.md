# Python Rate Limiter

## Authors
Sean Ippolito 
<br>
Sean Celik
<br>
Sean Pearce

## Setup

Youtube tutorial https://www.youtube.com/watch?v=HTx18uyyHw8&t=1s watch this for help

Install `pyenv` for your operating system to control the python version `3.12.1` which will be used for this project. The .python-version file controls the current version of python we are using.

Run the command to install the local virtualenv `python -m venv .venv`

You can validate you are in the correct venv by running the command `which python` in a bash terminal or alternatively `get-command python` in Windows Powershell. This command should point to the .venv path in this project directory.

If you are using the VSCode there are a few steps to follow in order to setup your working env. You must select the interperter in `${workspaceFolder}\\server-py\\.venv\\Scripts\\python.exe`, alternatively you can set this in your `.vscode/settings.json` file like below 

```
{
    "python.terminal.activateEnvironment": true,
}
```


You may also want to create a `launch.json` file in the `.vscode` directory in order to launch the project from the IDE's debugger. Below is the recommended settings for this file

```
"configurations": [
        
        {
            "name": "Python Debugger: Flask",
            "type": "debugpy",
            "request": "launch",
            "module": "flask",
            "env": {
                "FLASK_APP": "src/app.py",
                "FLASK_ENV": "development",
                "FLASK_DEBUG": "1"
            },
            "args": [
                "run",
                "--no-debugger",
                "--no-reload"
            ],
            "jinja": true,
            "justMyCode": false
        },
    ],
```

To install new pip packages run  `pip install -r requirements.txt`

To run the server from an integrated terminal in the VSCode editor you must be in the `server-py/src` directory and run the following command 

`python -m flask run`


If you are using an IDE other than VSCode, like pycharm, make sure to include the IDE specific settings folder in the .gitignore


## Goals
Implement a simple rate limiter in python with a UI that can toggle between 5 different techniques.

UI should also allow user to edit the amount of requests for a given time frame.

UI will be in a separate React Project which will be linked here when created.

Unit tests and stress testing will also be applied to tests large requests.

Future developement would entail running this in a multi server cloud based environment.

Refer to issues for work that needs to be done.

Refer to project board for and wiki for additonal details on development. 

