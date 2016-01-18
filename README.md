# Djangogram
[![Coverage Status](https://coveralls.io/repos/andela-ijubril/django-photo-application/badge.svg?branch=feature-effects&service=github)](https://coveralls.io/github/andela-ijubril/django-photo-application?branch=feature-effects)
[![Circle CI](https://circleci.com/gh/andela-ijubril/django-photo-application/tree/master.svg?style=svg)](https://circleci.com/gh/andela-ijubril/django-photo-application/tree/master)

A picture is worth a thousand words. Apply effects and share your pictures with djangogram.

### Technology used
Djangogram is built with the following stack:

* [Django](https://www.djangoproject.com/) - Django makes it easier to build better Web apps more quickly and with less code.
* [Twitter Bootstrap](http://getbootstrap.com/) - Great UI boilerplate for modern web apps
* [Jquery](https://jquery.com/) - The Write Less, Do More, JavaScript Library.
* [Pillow](https://github.com/python-pillow/Pillow/) - Pillow is the friendly PIL fork by Alex Clark and Contributors

#### Requirements
To install and run this application you need to have python installed on your system


### Installation
To install the build locally 
```
$ git clone https://github.com/andela-ijubril/django-photo-application.git
$ cd django-photo-application
$ pip install -r requirements.txt
```
Set Up your environment key
```
$ touch .env.yml
$ echo 'SECRET_KEY="any-key-you-wish"
```
### Run your build
```
$ python django-photo-application/manage.py runserver --settings=settings.development
```

### Running the test
To run your test
```
$ python manage.py test
```
### Coverage
```
$ coverage run manage.py test
$ coverage report

Contributing
============

This is an open source project. Anxiously waiting to get your feedback in the form of
[`issues`](https://github.com/andela-ijubril/django-photo-application/issues) and [`pull requests`](https://github.com/andela-ijubril/django-photo-application/pul) together we can help people express themselves through pictures.