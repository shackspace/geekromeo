
===========
 Geekromeo
===========

Info
====

*Geekromeo Django Edition* was started at a Python-Django-Workshop in the `shackspace <http://shackspace.de>`_.



Load fixtures
=============

::

  ./manage.py loaddata profiles profiles/fixtures/pony.yaml
  ./manage.py loaddata profiles profiles/fixtures/codinglanguage.yaml


Bootstrap project
=================

(using `virtualenvwrapper <http://virtualenvwrapper.readthedocs.org/en/latest/>`_

::

  mkvirtualenv geekromeo
  pip install -r pip-requirements.txt
  

create database

::

  python manage.py syncdb


run:

::

  python manage.py runserver
