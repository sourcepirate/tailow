Create and update
===============

Create
------

.. code-block:: python
   
   import asyncio
   from tailow.document import Document
   from tailow.fields import *

   class Login(Document):
     username = StringField()
     password = StringField()

     class Meta:
       name = "users"
       unique = ["username"]
    

    async def saveit():
       l = Login(username="sourcepirate", password="onepiece")
       await l.save()
       print(l._id)

    loop = asyncio.get_event_loop()
    loop.run_until_complete(saveit())

Saving models using `save`_ method.

Update
------

.. code-block:: python

   import asyncio
   from tailow.document import Document
   from tailow.fields import *

   class Login(Document):
     username = StringField()
     password = StringField()

     class Meta:
       name = "users"
       unique = ["username"]
    

    async def saveit():
       l = Login(username="sourcepirate", password="onepiece")
       await l.save()
       print(l._id)
       l.username = "ananta"
       await l.save()

    loop = asyncio.get_event_loop()
    loop.run_until_complete(saveit())
   