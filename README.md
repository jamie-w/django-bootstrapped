# Bootstrapped Django

Templated Django installation.

To start, it includes
- a basic project structure with default base/homepage html files
- a static dir for loading css & js files
- bower with some default libraries (these are loaded in {{project_name}}/base.html)

Installation
------------

    cd /to/empty/directory # *i.e. {{project_name}}.com*
    pip install django
    django-admin startproject --template=https://github.com/jamie-w/django-bootstrapped/archive/standard-install.zip --extension=py,json,.bowerrc,bootstrap {{project_name}}
    cd {{project_name}}
    source bootstrap

Open the browser to 127.0.0.1:8000 and you should see "Hello World" 


