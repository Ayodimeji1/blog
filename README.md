
# Project Title

A FastAPI blog. 
 

## Introduction
This simple blog was built with FastAPI. The sole aim of t his project is to improve my FastAPI proficiency.
## Tech Stack

 Python, FastAPI

**Server:** Uvicorn


## Setup
Clone the repo git clone https://github.com/Ayodimeji1/blog.git

Checkout to the task branch git checkout -b <NAME_OF_NEW_BRANCH>

Run: git pull origin main
## Installation

# macOS and linuxOS
python3 -m venv venv

# windowsOS using python alias
py -m venv venv

# activate on macOS and linuxOS
source venv/bin/activate

# activate on Windows (cmd.exe)
venv\Scripts\activate.bat

# activate on Windows (PowerShell)
venv\Scripts\Activate.ps1

pip install -r requirements.txt

uvicorn blog.main:app --reload

    
## Running 
uvicorn blog.main:app --reload
