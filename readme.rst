
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

* use virtualenv
* pip install -r requirements.txt
* python manage.py syncdb
* python manage.py runserver
