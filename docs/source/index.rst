.. Fimbu documentation master file, created by
   sphinx-quickstart on Sat Mar 16 11:50:45 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Fimbu's documentation!
===================================

**Fimbu** (/fee'mboo/) is a thin functionnal layer over `litestar <https://docs.litestar.dev/>`_ and `edgy ORM <https://edgy.tarsild.io/>`_.
Fimbu isn't a framework; it's just a tool to abstract the **coupling** of Litestar and Edgy ORM. Additionally, it slightly improves developers' **experience**.


.. note::

   This project is under active development.


.. warning::
    Fimbu is a great tool for web developers, but it's not ideal for beginners 😠.
    Given that it is based on Litestar and Edgy ORM, you will need to know at least the basics of asynchronous programming and a little good knowledge of how ORMs such as Django ORM or SQLAlchemy work to be really comfortable.

============
Installation
============

To install fimbu, you have to type the next command.

.. code-block:: console
   
   $ pip install fimbu


This command will install the core dependecies of fimbu (litestar[standard]==2.5.5, edgy, aiosqlite, cryptography)

Install extra dependecies
*************************

For test depencies

.. code-block:: console

    $ pip install fimbu[testing]


This will command will install edgy[testing] and litestar[test]


Install mail dependecies

.. code-block:: console

    $ pip install fimbu[mail]


This will command will install the following packages:

* aiosmtplib
* dnspython
* email-validator
* redis
* blinker

Install all dependecies

.. code-block:: console

    $ pip install fimbu[all]

this will command will install the following packages:

* edgy[postgres,mysql,sqlite,testing]
* fimbu[mail]"
* fimbu[shell]
* litestar[annotated-types,attrs,brotli,cli,cryptography,jinja,jwt,mako,minijinja,opentelemetry,prometheus pydantic,redis,sqlalchemy,standard,structlog]

----

=================
Getting started
=================

Check version

.. code-block:: console

    $ fimbu version

Output

    |   Using Litestar app from env: 'fimbu.apps.main:app'
    |   Fimbu version: 0.2.1
    |   litestar: 2.5.5final0
    |   edgy: 0.9.2

Create a new project
********************

.. code-block:: console

    $ fimbu start-project hello


This command creates all project related files in the current directory.
if you want to change the directory give the '-d' or '--directory' option with the directory path.

Project structure
*****************

Fimbu is heavily inspired by Django and some parts of the code were directly adapted from Django.

    | .
    | :file:`Hello`
    |   ├── :file:`main.py`
    |   └── :file:`settings.py`
    | :file:`static`
    | :file:`templates`
    | :file:`fimbu.ini`


**Hello**
   this is the project directory, don't rename it even you can do it. this directory contains two files by default.

**main.py**
   this file contains the entrypoint of the projet, it's where you will the ASGI application.

**settings.py**
   Like django, this is the project settings file.

**static**
   Static files directory

**templates**
   Jinja Templates (default) directory


**fimbu.ini**
    This is the entrypoint for fimbu CLI, it helps to detect if the current directory is a fimbu project.


Create an application
*********************

.. code-block:: console

    $ fimbu start-app hello_app

This command creates a new application in the current directory.
if you want to change the directory give the '-d' or '--directory' option with the directory path.

.. important::
    ADD Application to the INSTALLED_APPS list in the settings file.

Application structure
*********************

    | apps.py
    | endpoints.py
    | models.py
    | tests.py


**apps.py**
    Application config file.

**endpoints**
    This file contains the routes of your application.

**models.py**
    Models for your application, but you can your models every you want, edgy will find them.

**tests.py**
    Put here your tests.


if you installed your app in the settings file. Now run like this:

.. code-block:: console

    $ fimbu run 


Now go to http://127.0.0.1:8000/hello_app


Happy coding ! 😂

----



.. toctree::
   :maxdepth: 2
   :caption: Contents

   Settings <settings>
   Command Line Interface <cli>
   Controlers & Routes <controlers>
   Databases <databases>
   Middlewares <middleware>
   Templates <templates>
   Static files <static>
   Plugins <plugins>
   Multitenancy <Multitenancy>
   Utils <utils>
   Deployment <deploy>
