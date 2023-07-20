# HASKI Backend System

This is the offical Repository for the HASKI (Hochschullehre: Adaptiv, selbstgesteuert, KI-gestützt) Backend.
It will provide all necessary tools for creating and recommending learning paths and learning elements for the students, who will use the system.
This is a joint project from three bavarian universities:

Ostbayerische Technische Hochschule Regensburg

Technische Hochschule Aschaffenburg

Hochschule Kempten

The HASKI-Project is supported by the German Federal Ministry of Education and Research (BMBF), grant number 16DHBKI036, and the Bavarian State Ministry of Scie
The responsibility for the content of this publication remains with the authors.


## Purpose of the Project

The overall HASKI concept is designed to provide learners with adaptive self-directed learning.
These are the learning space, the adapted Learning Management System (LMS) and the HASKI system.
The actors are the learners and teachers.
The adaptive learner model adapts to the learner and not vice versa.
The domain model (documents, videos, podcasts, learning tasks, ...) is refined so that the tutorial model appropriately accommodates students with their different expectations and prior knowledge with tailored learning paths and feedback.
Adaptive learning and testing means that learners are presented with tasks that match their learning and skill level.
This is a condition of success for adaptive teaching and learning arrangements.
The overall HASKI concept is based on a blended learning approach.
Students receive learning materials via an LMS in which learning paths are created individually according to learner, tutor and domain models.
In this process, learners can determine how their learning process looks like depending on which learning path they choose.
All actions of the learners, as well as the solutions of the learning tasks and quizzes are transmitted to the HASKI system - an AI-supported software.
The HASKI system determines feedback from this, which is passed directly to the learners via the LMS.
The AI system also customizes learning paths for learners based on this data.
Furthermore, the HASKI system creates a report of the learning activities of the learners for the teachers.

## Technology

The Backend System is developed as a Python Web-App with the Flask Web Framework.
It will provide RESTful-API Endpoints for the communication.
The overall system follwos the principle of loose coupling and a layer-architecture.
The three models (student, domain, tutoring) are all seperated as an extra domain and therefore are loosely coupled.
The system will work with the Service-Layer-Pattern, the Unit-of-Work-Pattern and the Repository-Pattern.

## Development

We will follow some Gudielines for the Development.
These are:

• We will use Python 3.10 for our development.

• We will follow the Zen of Python.

• We will write idiomatic python code and follow the PEP8 style guide.

• For better code, we will use the library pycodestyle for linting.

• We will use Flask for the overall creation of the backend.

• We will create RESTful-APIs and document them with OAS 3.0.

• We will use the pytest library for our TDD.

• We will use TDD for all parts. No tests, no merge.

• The used libraries will be saved in a requirements.txt file, so that everyone will be able to directly install the necessary parts.

• Uses as many comments as necessary, as few as possible.

• The naming (of variables, functions, classes, etc.) should be self-explaining.

## Setup

- Create a new conda environment using `conda create --name HASKI-Backend --file requirements.txt`
- Activate the environment: `conda activate HASKI-Backend`
- Rename .flaskenv_template to .flaskenv and fill in the necessary information
- Create the database as explained in the DB Setup section
- Run the app using `flask run`

To create a new requirements file after installing a new library, please run the following command: `pip list --format=freeze > requirements.txt`

## DB Setup
For creating a (local) setup for the PostgreSQL Database for the HASKI project, you need to install PostgreSQL.
You can follow these tutorials:

https://www.postgresqltutorial.com/postgresql-getting-started/install-postgresql/

https://www.postgresqltutorial.com/postgresql-getting-started/connect-to-postgresql-database/

After the installation, you can run it on the CMD or the pgAdmin 4 application.
You first have to create a database.
Afterwards, you can use the `setup\Table_Setup.sql` Script for creating the table within your DB.

For the last step, you should check the `db_config.py` file and change the password for your set password.
Caution, there are two passwords set during the setup of PostgreSQL!
This is not the Masterpassword to unlock the pgAdmin 4, but the password for the superuser postgres!

## Running in Docker
This project includes a Pipeline, that will automatically create a Docker image in the repository when merging into the main branch.
This Docker image should always be the latest running version.
Please create a .env file first locally, so that it can be passed with docker run.
A template is provided in the .env_template file in this repository.
Start the Docker image as container with the following command:
`docker run -d -p 5000:5000 --env-file <path/to/.env-File> ghcr.io/haski-rak/haski-backend:main`

## Contribution
For contributing to the project, please work on the Issues and fulfill the requested tasks.
Before commiting, always run `python validate_script.py` in the root folder and check the output.
The test coverage should be as good as possible and there shouldn't be any information displayed by flake8, isort and black.
For checking the code quality, you can use Sonarqube (https://docs.sonarqube.org/latest/setup-and-upgrade/install-the-server/).
There shouldn't be any code smells left, when contributing to the project.

After a Pull Request, one of the Code Owners will check and give feedback before the merge is possible.