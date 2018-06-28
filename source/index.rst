.. tailow documentation master file, created by
   sphinx-quickstart on Wed Jun 27 23:47:33 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to tailow's documentation!
==================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   model-and-fields
   create-update
   querying


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`


Why tailow ?
------------

If you are looking for an Mongodb ORM with asyncio support. Then tailow serves good for you.

Connecting
----------

.. code-block:: python
     
     from tailow import connect

     connect("mongodb://username:password@localhost:27017/", "test", loop=<asyncio_loop>)

An optional `loop` keyword argument is added to support the explicit asyncio loop.


Defining Documents
------------------

.. code-block:: python
    
    from tailow.fields import *
    from tailow.document import Document

    class Student(Document):
       
       id = IntegerField()
       name = StringField()
       age = IntegerField()

       class Meta:
         name = "students"
         unique = ["id"]

Inherit the document class to define your own schemes. Document also support `Meta` attributes
to further customize the Document and add indexes.


Meta Table properties
----------------------

indexes
  list represents the fields to be indexed

unique
  list of fields which has unique indexes

name
  alternate name of the collection