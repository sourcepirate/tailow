Querying
========

Querying can be done via `filter`_ , `find`_, `get`_ method.


filter
  filter the query and converts.

find
  awaits for the results from server.

get
  awaits for one result from server


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
    
    async def findit():
       l = await Login.objects.filter(username="sathya").get()
       print(l.password)
    
    async def find_bulk():
       l = await Login.objects.filter(username="sathya").find()
       print(l)

    loop = asyncio.get_event_loop()
    loop.run_until_complete(find_bulk())
    loop.run_until_complete(findit())

Using special Operators
-----------------------

Tailow also support query operator via `filter`_ function.

.. code-block:: python
   
   Login.objects.filter(username__in=["source","pirate"]).find()