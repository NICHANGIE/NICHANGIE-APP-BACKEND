# Nichangie-app

Welcome to Nichangie-app, a Django-based web API.

## Installation

Follow these steps to set up Nichangie-app on your local machine:

### Prerequisites

- Python 3.x installed on your system (https://www.python.org/downloads/)
- Git installed on your system (https://git-scm.com/downloads/)

### Clone the Repository

1. Open your terminal and navigate to the directory where you want to store the project.
2. Run the following command to clone the repository to your local machine:


      ```git clone git remote add origin https://github.com/NICHANGIE/NICHANGIE-APP-BACKEND.git```



### Create a Virtual Environment
Change into the project directory:

   ```cd nichangie-app```

Create a virtual environment:

```python -m venv venv```

Activate the virtual environment:

On Windows:


```venv\Scripts\activate```


On macOS and Linux:

```source venv/bin/activate```

### Install Requirements
While in the project directory and with the virtual environment activated, install the required Python packages:

```pip install -r requirements.txt```

### Apply Migrations
Run the following commands to apply database migrations and create the database:


```python manage.py makemigrations```

```python manage.py migrate```

### Run the Server
#### Start the development server:


```python manage.py runserver```

The server should now be running at http://localhost:8000/.

# Contribution guidelines
To contribute, follow these steps:

Fork the repository on GitHub.

Clone your forked repository to your local machine.

```git clone https://github.com/NICHANGIE/NICHANGIE-APP/BACKEND```

Create a new branch for your feature or bug fix:


``` git checkout -b feature-or-bug-fix-branch```

Make your changes, commit them, and push to your forked repository:

```git add .```

```git commit -m "commit message" ```

```git push origin feature-or-bug-fix-branch```