# HASKI Backend System

This is the offical Repository for the HASKI (Hochschullehre: Adaptiv, selbstgesteuert, KI-gestützt) Backend.
It will provide all necessary tools for creating and recommending learning paths and learning elements for the students, who will use the system.
This is a joint project from three bavarian universities:

Ostbayerische Technische Hochschule Regensburg

Technische Hochschule Aschaffenburg

Hochschule Kempten

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
### Crypto
In order for the system to verify requests, JWTs with RS256 signed signature will be used. Therefore create two files which hold public and private key in PEM format:
- keys/public.pem
- keys/private.pem
### Project
- Create a new conda environment using `conda env create -f environment.yml`
- Activate the environment: `conda activate haskibackend`
- Run `pip install -r .\requirements_pip.txt`
- Run the app using `flask run`
