# Bootstrapped Django

Templated Django installation.

To start, it includes
- a basic project structure with default base/homepage html files
- a static dir for loading css & js files
- bower with some default libraries (these are loaded in {{project_name}}/base.html)

Installation
------------

    cd /to/empty/directory \# *i.e. {{project_name}}.com*
    virtualenv env
    source ./env/bin/activate
    pip install django
    django-admin startproject --template=https://github.com/jamie-w/django-bootstrapped/master/zipball --extension=py,json,.bowerrc {{project_name}}
    cd {{project_name}}
    source ./bootstrap

Open the browser to 


