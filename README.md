# New_Project_Python
# Development Environment Setup

This guide provides step-by-step instructions to set up your Python development environment for creating a Flask server and documenting your endpoints using Swagger.

## Prerequisites

Make sure you have Python 3.12.1 installed on your system. Additionally, we recommend using Visual Studio Code as your text editor for an enhanced development experience.

### 1. Install Python

- **1.1 Install Python 3.12.1**

   Download and install Python 3.12.1 from the [official website](https://www.python.org/downloads/release/python-3121/).

- **1.2 Add Python Environment Variables**

   Add the following environment variables to your system:

   - Variable: `PYTHONPATH`
     - Value: `C:\Users\Julio Freitas\AppData\Local\Programs\Python\Python312`

   - Variable: `SCRIPTS`
     - Value: `C:\Users\Julio Freitas\AppData\Local\Programs\Python\Python312\Scripts`

### 2. Install Visual Studio Code

- **2.1 Install Visual Studio Code**

   Download and install Visual Studio Code from the [official website](https://code.visualstudio.com/).

## Flask Project Configuration

### 3. Create a Python File

- **3.1 Create a file named `nome.py`**

### 4. Install Flask Framework

- **4.1 In the VS Code Terminal, install the Flask framework**

   Run the following command:
   ```bash
   pip install Flask
5. Install VS Studio Installer
5.1 Install VS Studio Installer

Install the tools for C and C++ development.

6. Install HTTPie Framework
6.1 In the VS Code Terminal, install the HTTPie framework

Run the following command:
pip install httpie

7. Create a GET Call in the nome.py File
from flask import Flask

server = Flask(__name__)

@server.route('/pessoas')
def buscar_pessoas():
    return "retorno de uma pessoa"

server.run()

8. Test the GET Call
8.1 Execute the following command in the VS Code Terminal
http -v get http://localhost:5000/pessoas

9. Start the Flask Server
9.1 In the Command Prompt, execute the following command
flask run

10. Check the Return in the Terminal
10.1 Observe the message in the terminal
Running on http://127.0.0.1:5000

11. Access the Endpoint in the Browser
11.1 Open the browser and access the following URL
http://127.0.0.1:5000/pessoas

12. Specify the Call with OpenAPI
12.1 Install the flask-pydantic-spec package

Run the following command:
pip install flask-pydantic-spec

12.2 Access the Swagger documentation

Open the browser and go to:
http://127.0.0.1:5000/apidoc/swagger

Now you have a configured environment to develop APIs with Flask, test HTTP calls, and document your endpoints using Swagger. Enjoy coding!