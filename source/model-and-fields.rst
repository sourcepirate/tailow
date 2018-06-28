Models and Fields
=================

Model represents the schema of your database. To create a model you have to subclass the `Document`_ class.

.. code-block:: python

     from tailow.document import Document
     from tailow.fields import *

     class Login(Document):
        username = StringField()
        password = StringField()

        class Meta:
          name = "users"
          unique = ["username"]


Fields
======

- StringField
- IntegerField
- ReferenceField
- DateTime
- ListField
